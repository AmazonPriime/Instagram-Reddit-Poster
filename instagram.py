# handles the logic for posting the memes to instagram
from instagrapi import Client
from util import Util
import pickle
import os


class Instagram:
    def __init__(self):
        self.instagram = Client()

    def new(self, user, password):
        self.instagram.login(user, password)
        self.save()

    def load(self, path='instagram.pkl'):
        fullpath = os.path.join(os.getcwd(), path)
        if os.path.exists(fullpath):
            with open(fullpath, 'rb') as f:
                self.instagram = pickle.load(f)
                return True
        print('Could not load instagram instance from path: ' + path)
        return False

    def save(self, path='instagram.pkl'):
        fullpath = os.path.join(os.getcwd(), path)
        with open(fullpath, 'wb') as f:
            pickle.dump(self.instagram, f)

    def post(self, uri, caption=''):
        path = Util.save_file(uri)
        if path.endswith('png'):
            path = Util.png_to_jpg(path)
        if path.endswith('gif'):
            path = Util.gif_to_mp4(path)
        if path.endswith('jpg'):
            self.instagram.photo_upload(path, caption)
        elif path.endswith('mp4'):
            self.instagram.video_upload(path, caption)
        Util.delete_file(path)
