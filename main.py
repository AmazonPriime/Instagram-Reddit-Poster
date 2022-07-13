import argparse
import json
import os
from reddit import Reddit
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(
    description='Tool to gather and post memes to instagram.')

parser.add_argument('--post', action='store_true',
                    help='Select random meme from list and post to instagram.')

parser.add_argument('-n', '--number', default=48, type=int,
                    help='Number of memes to gather into memes folder.')

parser.add_argument('-subs', '--subreddits', nargs='+', default=['memes'],
                    help='List of the different subreddits to be searched.')


def store_json(data, path):
    if type(data) == list or type(data) == dict:
        path = os.path.join(os.getcwd(), path)
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)


if __name__ == '__main__':
    args = parser.parse_args()

    if not args.post:
        reddit = Reddit()
        if not reddit.load(path='Reddit_Meme_Getter/reddit.pickle'):
            reddit.new(
                os.getenv('REDDIT_CID'),
                os.getenv('REDDIT_SECRET'),
                os.getenv('REDDIT_USERNAME'),
                os.getenv('REDDIT_PASSWORD')
            )
        submissions = reddit.get_submissions(args.subreddits, args.number)
        store_json(submissions, 'memes.json')
