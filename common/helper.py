import os
import re
import requests
from os import walk
from PIL import Image
import numpy as np

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
    
    if images is np.NaN  or images == []:
        print("!!"*30)
        print("Doesn't have any image file.")
        print("!!"*30)
        return()

    image_list = []

    for file in images:
        img = Image.open(file)
        if img.mode == 'RGBA':
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3])
            image_list.append(rgb_img)
        elif img.mode == "RGB":
            image_list.append(img)
        else:
            print(f"Some image go wrong {img}")

    img1 = image_list[0]
    img_oth = image_list[1:]
    
    img1.save(name+".pdf", save_all=True, append_images=img_oth)

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

def get_file_extension_from_file(file_path:str):
        '''
        Get file extension from file.

        :param str file_path: The path of the file.
        :return str: The extension of the file.
        '''

        return os.path.splitext(file_path)[-1].lower()