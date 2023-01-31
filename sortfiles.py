import os
import shutil

from_dir="/Users/arshiyachhabra/Downloads"
to_dir="/Users/arshiyachhabra/Downloads"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension=os.path.splitext(i)

    if extension=='':
        continue

    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif','.heic', '.JPG', '.JPEG', '.GIF','.PNG', '.HEIC']:
        path_1=from_dir + "/" + i
        path_2= to_dir + "/" + "Image files"
        path_3= to_dir + "/" + "Image files"+ "/" + i

        if os.path.exists(path_2):
            shutil.move(path_1,path_3)

        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)

    if extension in ['.docx', '.pptx', '.pdf', '.xlsx', '.tif', '.txt', '.doc', '.ppt', '.dotx']:
        path_1=from_dir + "/" + i
        path_2= to_dir + "/" + "Documents"
        path_3= to_dir + "/" + "Documents"+ "/" + i

        if os.path.exists(path_2):
            shutil.move(path_1,path_3)

        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)

    if extension in ['.m4a', '.mp4', '.mov', '.MOV', '.mp3', '.MP4']:
        path_1=from_dir + "/" + i
        path_2= to_dir + "/" + "Media files"
        path_3= to_dir + "/" + "Media files"+ "/" + i

        if os.path.exists(path_2):
            shutil.move(path_1,path_3)

        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)

    if extension in ['.dmg', '.zip', '.ipynb', '.sql', '.pkg', '.ics', '.json']:
        path_1=from_dir + "/" + i
        path_2= to_dir + "/" + "Miscellaneous files"
        path_3= to_dir + "/" + "Miscellaneous files"+ "/" + i

        if os.path.exists(path_2):
            shutil.move(path_1,path_3)

        else:
            os.makedirs(path_2)
            shutil.move(path_1,path_3)