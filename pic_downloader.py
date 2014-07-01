
import re
import os
import shutil
import urllib.error
import urllib.request

"""
this python file downloads pic of the day published by NASA
"""


class pic_downloader:

    def __init__(self):
        self.name = 'NasaGallery'
        self.feed_url = 'http://apod.nasa.gov/apod/astropix.html'
        self.img_url = 'http://apod.nasa.gov/apod/'

    def get_img(self):        
        try:
            response = urllib.request.urlopen(self.feed_url)
            html = response.read()
        except urllib.error.URLError:
            print('connection error')
            return

        html = html.decode('utf-8')

        img = re.search(r'image/\d+/\w+_(\w+)_\d+.jpg', html)

        if img:
            return img

        return

    def save_img(self):
        directory = os.path.join('C:/', self.name)

        try:
            os.mkdir(directory)
        except (FileExistsError,OSError):#directory already exists
            pass

        img = self.get_img()
        img_url = self.img_url + img.group(0)
        img_name = img.group(1)+'.jpg'
        img_path = os.path.join(directory, img_name)

        if not os.path.exists(img_path):
            try:
                
                response = urllib.request.urlopen(img_url) 
                img_file = open(img_path, 'wb')
                shutil.copyfileobj(response, img_file)
                img_file.close()
            except (urllib.error.URLError, IOError):
                        print('Connection error')
            
                    
                    


if __name__ == '__main__':
    nasa = pic_downloader()
    nasa.save_img()
        
        
    
        
        
