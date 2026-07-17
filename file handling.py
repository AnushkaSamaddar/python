import os
def list_files_recursive(path): #imports pythons built-in os module which provides functions to interact with the operating system
    """
    this func prints all files and directories inside the given path.if it finds a directory,it calls itself 
    again(recursion) to explore thr content of the directory
    """
    print(os.listdir(path))
    #os.list.dir(path) returns a list containing the names of files
    #and directories inside thr specified path
    for item in os.listdir(path):
        #os.path.join(path,item) safely combines the directory path
        #and the file/folder name into a full path
        full_path=os.path.join(path,item)
        #os.path.isfile(full_path) checks if the given path is a file
        #returns true if it is a file
        if os.path.isfile(full_path):
            print("file:", full_path)
            #os.path.isdir(full_path) checks if the given path is a directory (folder)
            #returns true if it is a directory 
        elif os.path.isdir(full_path):
            print("Directory: ",full_path) #prints the directory path
        #recursive call: the function calls itself to explore
        # thr contents inside this directory
            list_files_recursive(full_path)
#print(os.listdir("C:/Users/MSCLAB-32/Desktop"))
list_files_recursive()