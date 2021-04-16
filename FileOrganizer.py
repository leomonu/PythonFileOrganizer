# we imported os and shutil modules
import os
import shutil
# asking the user to enter the director they want to sort
path = input("Enter Directory you want to sort ")
# reading all the files and placing in an array
listOfFiles = os.listdir(path)
# going through all the files
for file in listOfFiles:
    # spliting the root name and extension
        name,ext = os.path.splitext(file)
        # this is storing the extension
        ext = ext[1:]
        # if it is a directory it will force the itteration
        if(ext == ''):
            continue
        if(os.path.exists(path+'/'+ext)):
                shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        else:
            # this will create a new directory
                
                os.makedirs(path+'/'+ext)
                             # source       destination
                shutil.move(path+'/'+file,path+'/'+ext+'/'+file)