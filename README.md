# Subreddit new post checker

Just checking to see if there's anything new.

### Requirements

__Requests__

```
pip install requests
```

### Usage

```bash
python check_new.py <subreddit>
```
* `subreddit` is optional argument

By default using [r/ru_mechmarket](https://www.reddit.com/r/ru_mechmarket/), but you may change this in `default_subreddit` string variable [`check_new.py`](/check_new.py#L5).

### Project tree

```
.
├─── check_new.py   # Main script
├─── (last.json)    # Last request dump
└─── server.py      # For handly check of Json
```