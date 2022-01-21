import requests
import pandas as pd


headers = {
    'authority': 'www.autolist.com',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^94^\\^, ^\\^Google',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'x-autolist-session-guid': 'c9fb9ffb-2c06-4468-a3d0-c26290c6994f',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4590.0 Safari/537.36',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.autolist.com/listings',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'ec=eyJlZGdlVXNlckFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk0LjAuNDU5MC4wIFNhZmFyaS81MzcuMzYifQ==; client_guid_timestamp=1602952f-d1bf-4936-82e3-cbdedfa11d2d.1627825394925; scavenger-a493=i2edJn8U8quG2BtrlZCXcua4KB62fcJRrAhaI/t9eYZNJczdHQYj3P0Y4s6myhEl4IbJl8vp9L0oN+SXDh2fFcTvJ/vA/hPyRJ0ohE6LnQGIee5ACCL3nGqW5xFg3QnijfTypiJhVgTfPjk3c81AtkxzR54e+BHqQL0DI6/oWNd7iIkgvHaWjuilZuITytvFV0IAUJ0bX041NuAIFpx8K90bzfPLeAKgkwc0lpwB3cLwm8NcNKMD3xELdjI6leANl5jZJ9KzZ3K+5J7nCpxnAynFJJt2e95bby70BTVZ0qdWtSWGgwFxEdjmesrF42H7EgAjt4LMIKDuRVtbhVwu/q/wUhPoUZvZb6F+CbFpxMXuZTpd27JmWUrboqGTfyS3Nr7gV1kl6hr+8w0aOlmo8NlrdmNRb0u51Ex4zu4JTymiAUsWvS9JhNr/uvk4GVvM3kafDQeKq7v+xHkB/lCvPkqLEifYP7VVan6h5ZmvaQTgULjs0N5JhUd76Pt6c/tY5R0v8R67gjgbvW8n/4Gqzw==; _sp_ses.8ca5=*; _gid=GA1.2.96049973.1627825395; _fbp=fb.1.1627825395573.409117512; __gads=ID=c459f8bf6d0987dd:T=1627825394:S=ALNI_MaW1epD3HNJsvJQTCnPWSJCcOdE_w; AMP_TOKEN=^%^24NOT_FOUND; sp-nuid=e4461948-a1a2-45a1-88f8-45c2889d9576; _gcl_au=1.1.519751617.1627825557; _ga_152345333=GS1.1.1627825395.1.1.1627828426.0; _ga=GA1.2.2118379867.1627825395; cto_bundle=WV1etl8zMUc1cGt6WnZNSEZMYWhwNnJjUXpTYzQxVzZ6QzM5VE1tWXZFcjQ3ZWhrNTlETG1CemlUdmNFYUtIbXdCQTNFelJmY3h6QXA0SlVIZml0WVg2OWQxZlBPMmRqbExXNU9XZTM0V0VaR09tbHBvJTJGdERCb21zZUVKJTJCTG1vVzlDV0w2VjA0bDklMkJnRjdrMmZPUExmJTJGY0l6USUzRCUzRA; _gat=1; _sp_id.8ca5=d3d3f60d-371c-4289-92fe-1c6f66b4979f.1627825395.1.1627828912.1627825395.8bc1e545-8ca1-448e-b1ba-ec8d2c359ada',
    'if-none-match': 'W/^\\^c6f72fa4ef059e03ea0309ebd57c197d^\\^',
}

model = []
mileage = []
year = []
dealer_name = []
price = []

for i in range(1, 6):
    
    params = (
        ('make', 'Tesla'),
        ('zip', '198099'),
        ('location', 'Sankt-Peterburg'),
        ('latitude', '59.897206'),
        ('longitude', '30.2604628'),
        ('radius', '50'),
        ('page', str(i)),
    )

    # response variable for the get request
    response = requests.get('https://www.autolist.com/api/cwv/seo/listings', headers=headers, params=params)
    
    # json object
    results_json = response.json()
    
    # result items (20 times for each page)
    result_items = results_json['search_results']
    
    for result in result_items:
        # model
        model.append(result['model'])
        
        # mileage
        mileage.append(result['mileage'])
        
        # year
        year.append(result['year'])
        
        # dealer_name
        dealer_name.append(result['dealer_name'])
        
        # price
        price.append(result['price'])
    
tesla_multiple_df = pd.DataFrame({'Model': model, 'Mileage': mileage, 'Year': year,
                                  'Dealer Name': dealer_name, 'Price': price})

# Store Results in Excel
tesla_multiple_df.to_excel('tesla_multiple_pages.xlsx', index=False)


