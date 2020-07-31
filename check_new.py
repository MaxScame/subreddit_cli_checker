import json
import requests
import sys

default_subreddit = 'ru_mechmarket'
header = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }
params = { 'limit' : 10 }

def print_post(res):
    for post_data in res['data']['children']:
            if post_data['data']['link_flair_text'] == 'Продажа':
                print(f"Title: {post_data['data']['title']}\nText: {post_data['data']['selftext']}\n---------")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        subreddit = str(sys.argv[1])
    else:
        subreddit = default_subreddit

    print(f'Subreddit:', subreddit)
    try:
        with open('last.json', 'r') as f:
            last = f.read()
    except FileNotFoundError:
        print('No last check data.')
    
    try:
        r = requests.get(f'https://api.reddit.com/r/{subreddit}/new/', headers=header, params=params).text
        res = json.loads(r)
    except requests.exceptions.ConnectionError:
        print('Check internet connection')
        sys.exit()

    with open('last.json', 'w') as f:
        f.write(r)

    if len(last):
        last_json = json.loads(last)
        if res['data']['children'][0]['data']['title'] != last_json['data']['children'][0]['data']['title']:
            print_post(res)
        else:
            print('Meh, nothing new...')
    else:
        print_post(res)
