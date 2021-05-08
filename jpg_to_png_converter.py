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


def cmd_input():
    '''following requires input from command prompt'''
    cmd_input_holder = []

    # first input on command prompt
    jpg_folder = sys.argv[1]
    cmd_input_holder.append(jpg_folder)

    # Second input on command prompt
    png_folder = sys.argv[2]
    cmd_input_holder.append(png_folder)

    # print(jpg_folder, png_folder) # Test to see if the input in cmd reflects the values

    return cmd_input_holder


# check if new_folder exist, if not create it
# Utilizes OS module to grab the path


def jpg_folder_check(jpg_folder_name):
    '''jpg folder exist check'''

    # check if folder name is in directory
    jpg_folder_exist = jpg_folder_name in os.listdir()

    if jpg_folder_exist == False:
        exit("jpg folder doesn't exist, please try later")

    return jpg_folder_name


def png_fodler_check(png_folder_name):
    '''png folder exist check'''

    # check if folder name is in directory
    png_folder_exist = png_folder_name in os.listdir()

    if png_folder_exist == False:
        # create png folder with name entered in cmd prompt
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
    '''few types of test'''
    # 1. input correctly, out come is correct (Success)
    # 2. input wrong jpg folder name, out come is exiting the system with a message saying "try again"
    # 3. input a random png folder name, it should be able ot create a new png folder with taht name and put the png images in it.

    '''cmd prompt input "pokedex" "new_folder" '''
    folder_list = cmd_input()
    jpg_folder = folder_list[0]
    png_folder = folder_list[1]

    '''jpg folder check'''
    jpg_folder_name = jpg_folder_check(jpg_folder)

    '''png folder check'''
    png_folder_name = png_fodler_check(png_folder)

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

    '''save images as png at current directory'''
    save_png(new_name_image_dict)
