import httpx
import json

# URL for the specific Reddit post
post_url = "https://www.reddit.com/r/pennystocks/comments/1ho8m9j/ampx_the_battery_dark_horse_of_2025/.json"

headers = {
    'User-Agent': 'MyRedditScraper/0.1 by YourUsername'
}

try:

    response = httpx.get(post_url, headers=headers)
    print(f'Fetching "{response.url}"...')
    response.raise_for_status()

    post_data = response.json()

    # save to a .json file
    output_file = "output/reddit_post.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(post_data, file, indent=4)

    print(f"Post data saved to {output_file}")

except httpx.HTTPStatusError as e:
    print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
