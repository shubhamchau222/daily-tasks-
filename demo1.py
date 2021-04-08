# filtering the corrupt images and other files except the images 
# helpful in Image handling during the Object detection projects 

import os 
import shutil 
from PIL import Image
import argparse


def main (Target):

    os.chdir(Target)
    #print(os.getcwd())
    fileNames = os.listdir(".")
    os.makedirs("Trash" , exist_ok=True)
    for file_ in fileNames : 
        try :
            Image.open(file_) 
        except Exception as e :
            print(f"Error:{e}")
            src_path  = file_
            dest_path  = "Trash"
            shutil.move(src =src_path , dst = dest_path)
            print(f"file {file_} successfully moved to dir : {dest_path}")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--target" , default="G:\demo_1")
    parsed_args  = args.parse_args()
    print(parsed_args.target)
    main(Target  = parsed_args.target) 