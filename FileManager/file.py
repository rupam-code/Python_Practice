import os 
import shutil

path =  input("Enter your path: ")
 
files = os.listdir(path)

for i in files:
    filename, extenstion = os.path.splitext(i)
    extenstion_1 = extenstion[1:]
    folder_path = path+"\\"+extenstion_1
    if os.path.exists(folder_path):
        shutil.move(path+"\\"+i,path+"\\"+extenstion_1+"\\"+i)
    else:
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i,path+"\\"+extenstion_1+"\\"+i)