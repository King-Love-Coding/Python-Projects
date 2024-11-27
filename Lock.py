import os
import shutil
#Shutil module offers high-level operation on a file like a copy, create, and remote operation on the file.
# It comes under Python’s standard utility modules.
# This module helps in automating the process of copying and removal of files and directories.

from_dir = input("Enter The Dir Of Folder To Protect")
fname = input("Enter The Folder Name To Create")
password = input("Enter The Password")

to_dir = 'D:\PycharmProjects'                                      #Directory/path where folder will be create
to_dir = os.path.join(to_dir, fname)                               # Folder Name Created in the path
os.mkdir(to_dir)                                                   # Make New Folder

for i in password:
    for j in range(1, 11):
        path = os.path.join(to_dir, str(j))     # joins the path
        try:
            os.mkdir(path)
        except:
            print('error')
        for k in range(1,11):
            path2 = os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print("Error")

    to_dir = to_dir+"/"+i
try:
    shutil.move(from_dir, to_dir)
except:
    print()





# import os
# import shutil
#
# to_dir = input("Enter the destination directory where folder was moved: ")  # Directory where folder was moved
# password = input("Enter the password used for protection: ")
# original_dir = input("Enter the original directory where the folder should be restored: ")
#
# # Reverse folder structure creation
# for i in password:
#     to_dir = os.path.join(to_dir, i)  # Reverse the path based on password characters
#
# # Extract the main folder name from the destination path
# fname = os.path.basename(to_dir)
#
# # Full path to the original location where we want to restore the folder
# restore_path = os.path.join(original_dir, fname)
#
# try:
#     # Move the folder back to the original directory
#     shutil.move(to_dir, restore_path)
#     print(f"Folder '{fname}' successfully moved back to {restore_path}")
# except Exception as e:
#     print(f"Error during restoring folder: {e}")
