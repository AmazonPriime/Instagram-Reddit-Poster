# Instagram Reddit Meme Poster Tool
Gathers memes from Reddit and posts them to Instagram.

### Usage
Clone the repository and then install all the required dependencies.
```bash
pip install -r requirements.txt
```

Update the contents of the `.env` file to reflect your account details.

You can obtain the Reddit Client ID (CID) and Secret by creating a [Reddit App](https://www.reddit.com/prefs/apps).

The usernames and passwords are the same that you use to login, if you experiences any issues authenticating you may need to disable 2FA. 

---

The available arguments for the tool are:

| Argument | Description | Default |
| --- | ----------- | --- |
| `-h, --help` | Shows help page showing the args and usage. | - |
| `--scrape`  | Used when you would like to use the scraping part of the tool to get memes/reddit submissions | - |
| `-n, --number`  | When using scrape, you can specify the number of posts to scrape - integer value | 48 |
| `-subs, --subreddits`  | When using scrape, you can provide a list of subreddits which are to be included when looking for memes/reddit submissions | memes |
| `--post` | Used when you would like to post to Instagram | - |
| `-tags, --hashtags` | When posting to Instagram you can provide a list of hashtags to be added to the post caption. | meme |

### Example Usage
Getting 20 memes from r/dankmemes, r/memes and r/funny:
```bash
python main.py --scrape -n 20 -subs dankmemes memes funny
```

Getting memes from r/dankmemes (using default number value):
```bash
python main.py --scrape -subs dankmemes
```

Getting memes from r/memes (using default subreddit value):
```bash
python main.py --scrape
```

Posting a meme to instagram with #meme #funny #lol:
```bash
python main.py --post -tags meme funny lol
```
