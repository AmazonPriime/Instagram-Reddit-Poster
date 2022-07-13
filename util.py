# helper functions used in various places
import os
import io
import json
import requests
from PIL import Image
import moviepy.editor as mp


class Util:
    def store_json(data, path):
        if type(data) == list or type(data) == dict:
            path = os.path.join(os.getcwd(), path)
            with open(path, 'w') as f:
                json.dump(data, f, indent=2)

    def load_json(path):
        path = os.path.join(os.getcwd(), path)
        if os.path.exists(path):
            with open(path) as f:
                data = json.load(f)
            return data
        print('JSON file not found: ' + path)

    def save_file(uri):
        type = uri.split('.')[-1]
        path = os.path.join(os.getcwd(), 'temp.' + type)
        response = requests.get(uri)
        with open(path, 'wb') as f:
            f.write(response.content)
        return path

    def png_to_jpg(path):
        with open(path, 'rb') as f:
            image = Image.open(io.BytesIO(f.read()))
            image.convert('RGB').save(path.replace('.png', '.jpg'), "JPEG")
        os.remove(path)
        return path.replace('.png', '.jpg')

    def gif_to_mp4(path):
        clip = mp.VideoFileClip(path)
        clip.write_videofile(path.replace('.gif', '.mp4'))
        os.remove(path)
        return path.replace('.gif', '.mp4')

    def delete_file(path):
        if os.path.exists(path):
            os.remove(path)
        else:
            print('Could not remove file, not found: ' + path)
