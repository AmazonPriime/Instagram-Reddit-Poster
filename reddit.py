# handles the logic for gathering the memes and picking them
import pickle
import praw
import os


class Reddit:
    def __init__(self):
        self.reddit = None

    def new(self, cid, secret, user, password):
        self.reddit = praw.Reddit(
            client_id=cid,
            client_secret=secret,
            password=password,
            username=user,
            user_agent='Memescript by u/' + user
        )
        self.save()

    def load(self, path='reddit.pkl'):
        fullpath = os.path.join(os.getcwd(), path)
        if os.path.exists(fullpath):
            with open(fullpath, 'rb') as f:
                self.reddit = pickle.load(f)
                return True
        print('Could not load reddit instance from path: ' + path)
        return False

    def save(self, path='reddit.pkl'):
        fullpath = os.path.join(os.getcwd(), path)
        with open(fullpath, 'wb') as f:
            pickle.dump(self.reddit, f)

    def get_submissions(self, subreddits, number, filter='day'):
        subreddits = '+'.join(subreddits)
        submissions_generator = self.reddit.subreddit(
            subreddits).top(limit=number, time_filter=filter)
        submissions = []
        for submission in submissions_generator:
            if not submission.over_18:
                submissions.append({
                    'id': submission.id,
                    'author': submission.author.name,
                    'title': submission.title,
                    'upvotes': submission.score,
                    'upvote_ratio': submission.upvote_ratio,
                    'url': submission.url,
                    'permalink': submission.permalink
                })
        return submissions
