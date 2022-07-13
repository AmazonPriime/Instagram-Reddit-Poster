import argparse
import random
import os
from reddit import Reddit
from instagram import Instagram
from util import Util
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(
    description='Tool to gather and post memes to instagram.')

parser.add_argument('--scrape', action='store_true',
                    help='Find and store new memes/submissions from reddit.')

parser.add_argument('-n', '--number', default=48, type=int,
                    help='Number of memes to gather into memes folder.')

parser.add_argument('-subs', '--subreddits', nargs='+', default=['memes'],
                    help='List of the different subreddits to be searched.')

parser.add_argument('--post', action='store_true',
                    help='Select random meme from list and post to instagram.')

parser.add_argument('-tags', '--hashtags', nargs='+', default=['meme'],
                    help='List of different hashtags to be added to caption.')


if __name__ == '__main__':
    args = parser.parse_args()
    used_ids = Util.load_json('used_id.json')
    if not used_ids:
        used_ids = []

    if args.scrape:
        reddit = Reddit()
        if not reddit.load():
            reddit.new(
                os.getenv('REDDIT_CID'),
                os.getenv('REDDIT_SECRET'),
                os.getenv('REDDIT_USERNAME'),
                os.getenv('REDDIT_PASSWORD')
            )
        submissions = reddit.get_submissions(
            args.subreddits, args.number, used_ids)
        Util.store_json(submissions, 'memes.json')

    if args.post:
        instagram = Instagram()
        if not instagram.load():
            instagram.new(
                os.getenv('INSTA_USERNAME'),
                os.getenv('INSTA_PASSWORD')
            )
        submissions = Util.load_json('memes.json')
        if not submissions:
            exit()
        if len(submissions) == 0:
            print('There are no submissions available.')
            exit()
        random_index = random.randint(0, len(submissions) - 1)
        submission = submissions[random_index]
        caption = f'"{submission.get("title")}"\n - '
        caption += submission.get("author") + ' from Reddit \n\n'
        caption += ' '.join(map(lambda x: f'#{x}', args.hashtags))
        instagram.post(submission.get('url'), caption)
        del submissions[random_index]
        Util.store_json(used_ids + [submission.get('id')], 'used_id.json')
        Util.store_json(submissions, 'memes.json')
