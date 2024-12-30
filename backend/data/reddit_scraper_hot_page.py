import time
import httpx
import json

base_url = 'https://www.reddit.com/r/pennystocks/new.json'
after_post_id = None

dataset = []


headers = {
    'User-Agent': 'RandomUser'
}

# number of pages to fetch
for _ in range(1): 
    params = {
        'limit': 100,  #maximum posts per request
        'after': after_post_id  
    }

    # send the GET request
    try:
        response = httpx.get(base_url, params=params, headers=headers)
        print(f'Fetching "{response.url}"...')
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        break

    json_data = response.json()


    if 'data' not in json_data or 'children' not in json_data['data']:
        print("Invalid response structure. Stopping.")
        break


    dataset.extend([rec['data'] for rec in json_data['data']['children']])

   
    after_post_id = json_data['data'].get('after')
    if not after_post_id:  
        print("No more posts to fetch.")
        break


    time.sleep(2)

# data to a JSON file
if dataset:
    output_file = 'output/reddit_pennystocks.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=4)
    print(f"Data fetched and saved to {output_file}")
else:
    print("No data fetched.")



#This is csv format

# import time
# import httpx
# import pandas as pd

# base_url = 'https://www.reddit.com/r/pennystocks/hot.json'
# after_post_id = None

# dataset = []

# #  custom User-Agent header
# headers = {
#     'User-Agent': 'MyRedditScraper/0.1 by YourUsername'
# }

# #  pages to fetch
# for _ in range(5):  # Adjust the range as needed
#     params = {
#         'limit': 100,  
#         'after': after_post_id  
#     }

#     # Send the GET request
#     try:
#         response = httpx.get(base_url, params=params, headers=headers)
#         print(f'Fetching "{response.url}"...')
#         response.raise_for_status()
#     except httpx.HTTPStatusError as e:
#         print(f"HTTP error occurred: {e}")
#         break
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         break

#     # parse the response
#     json_data = response.json()

#     # valid response structure
#     if 'data' not in json_data or 'children' not in json_data['data']:
#         print("Invalid response structure. Stopping.")
#         break

#   
#     dataset.extend([rec['data'] for rec in json_data['data']['children']])

#    
#     after_post_id = json_data['data'].get('after')
#     if not after_post_id:  # Stop if there's no more data
#         print("No more posts to fetch.")
#         break

#     #  avoid rate limits
#     time.sleep(0.5)

# #  the data to a CSV file
# if dataset:
#     df = pd.DataFrame(dataset)
#     df.to_csv('reddit_pennystocks.csv', index=False)
#     print("Data fetched niceeeeee ")
# else:
#     print("Nooooo")
