import os
import re
import requests
from os import walk
from PIL import Image

def hello():
    print("I am helper. I will help you")

def save_image_url(name, url):
    response = requests.get(url)

    file = open(name, "wb")
    file.write(response.content)
    file.close()

def get_files_from_directory(path):
    filenames = next(walk(path), (None, None, []))[2]
    return filenames

def remove_files_from_directory(path,name):
    os.remove(path + name)

def create_pdf(images, name):
    image_list = []

    for file in images:
        img = Image.open(file)
        image_list.append(img)

    img1 = image_list[0]
    img_oth = image_list[1:]
    
    img1.save(name+".pdf",save_all=True, append_images=img_oth)

# Sort the list that contain text with number (Ex test1, test2, ...)
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def sort_text_with_number(items):
    items.sort(key=natural_keys)
    return(items)