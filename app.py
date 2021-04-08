#file arrangments 
import os 
import  shutil 
Target  = "G:\\images"
# print(os.getcwd())  ---- to get the current working directories
# result : -  c:\Users\Admin\Desktop\app.py "
# we need to change the directory 
os.chdir(Target)      # here we changed directory 
# print(os.getcwd())
# result :- G:\images
filenames  = os.listdir(".")  # (".") is for the current working directory 

#print(filenames) # to get the filenames present in dir 
for file_ in filenames:
    print(file_.split(".")[-1]) # to get the file extensions 
    extensions = file_.split(".")[-1]
    os.makedirs(extensions , exist_ok=True)
    src_path =  file_    # source path required to move the file
    dest_path  = os.path.join(extensions , file_)    # where to  move the path 
    # print(dest_path)  # results :- PNG\relations.PNG
    shutil.move(src_path , dest_path)
