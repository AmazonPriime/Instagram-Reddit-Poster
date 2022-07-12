import argparse
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(
    description='Tool to gather and post memes to instagram.')

parser.add_argument('--post', action='store_true',
                    help='Select meme from the folder and post to instagram.')

parser.add_argument('-n', metavar='int', default=30,
                    help='Number of memes to gather into memes folder.')

if __name__ == '__main__':
    args = parser.parse_args()
