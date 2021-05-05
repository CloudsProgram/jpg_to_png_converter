import sys
import os
from PIL import Image

'''
Scrpit's function:
Copy JPG images in one folder, and saved it as PNG images in another folder.

Assumptions:
The above action will be executed through Command prompt
The existing JPG folder and empty PNG folder will be at the same directory with jpg_to_ong_converter.py

Example use case:
(in command prompt at the same directory as this jpg_to_png_converter.py file)
type: python jpg_to_png_converter.py pokedex new_folder       #pokedex folder(has the jpg file), and new_folder folder(will recieve the png file)
# result: pokemon jpg images from pokedex folder will be copied to new_folder folder as png images
'''
# following requires input from command prompt
# jpg_folder = sys.argv[1] # can input through cmd, can't run in environment b/c it has yet to receive value
# png_folder = sys.argv[2] # can input through cmd, can't run in environment b/c it has yet to receive value
# print(jpg_folder, png_folder)


# check if new_folder exist, if not create it
# Utilizes OS module to grab the path

# need to add input output
def jpg_folder_check():
    '''jpg folder exist check'''

    # meant for tests, will change name pokedex to sys.argv[1]
    jpg_folder_name = 'pokedex'

    # check if folder name is in directory
    jpg_folder_exist = jpg_folder_name in os.listdir()

    if jpg_folder_exist == False:
        exit("jpg folder doesn't exist, please try later")

    return jpg_folder_name

# need to add input output


def png_fodler_check():
    '''png folder exist check'''

    # tests, will change name to sys.argv[2]
    png_folder_name = 'new_folder'

    # check if folder name is in directory
    png_folder_exist = png_folder_name in os.listdir()

    if png_folder_exist == False:
        # create png folder # can be any folder name input in cmd prompt.
        os.mkdir(png_folder_name)

    return png_folder_name


''' Step1: able to look at pokedex folder and show existing directories
    Step2: loop through them to create png that saves in "new_folder"
'''


def change_directory(folder_name, original_path):
    path = original_path + "\\" + folder_name
    # print(path) #test: am I at the correct path?

    os.chdir(path)  # change directory to this path
    # print(os.getcwd()) #test: am I at the correct path?


def copy_and_rename():
    # step2: copy them as png, change directory to "new_folder", put those png in new_folder
    # store tho directories as a list, go to other folder. check if the list is still correct
    images_to_convert = os.listdir()  # test: list of jpg images stored
    # print(images_to_convert)  # test: make sure is correct

    new_images_dict = {}
    for img in images_to_convert:
        # changeed file names stored as .png, as a key for the dictionary
        jpg_to_png = img.replace(".jpg", ".png")
        # image stored as value for the dictionary
        new_images_dict[jpg_to_png] = Image.open(img)

    return new_images_dict


def save_png(new_images_dict):
    # convert from jpg to png and save it to the new folder
    for name, image in new_images_dict.items():
        image.save(name)


if __name__ == "__main__":
    print("hi")
    '''need to finish my work on the cmd prompt'''

    '''jpg folder check'''
    jpg_folder_name = jpg_folder_check()

    '''png folder check'''
    png_folder_name = png_fodler_check()

    '''get existing path'''
    original_path = os.getcwd()

    '''change to jpg img folder's directory'''
    change_directory(
        jpg_folder_name, original_path)  # change_directory_jpg(jpg_folder_name, original_path)

    '''rename and store image in a dict'''
    new_name_image_dict = copy_and_rename()

    '''change to png folder's directory'''
    change_directory(
        png_folder_name, original_path)  # change_directory_png(png_folder_name, original_path)

    '''save images as png'''
    save_png(new_name_image_dict)
