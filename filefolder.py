import os
from shutil import move
from tkinter.filedialog import askdirectory

directory:str = askdirectory()
if directory is None or directory == "":    # No valid directory - Closes program
    print("Can't continue without a valid directory! Closing here..")
    exit()
os.chdir(directory)

def mover():
    counter:int = 0
    # print(os.getcwd())
    for filename in os.listdir():
        if not os.path.isdir(filename) and not filename.endswith('.py'):    # for test purposes i excluded python files, but you don't have to!
            file_name, file_extension = os.path.splitext(str(os.getcwd() + "\\" + filename))
            
            """print(f"{filename[:-len(file_extension)]}")
            print(filename)
            print(file_name)
            print(file_extension)"""

            if file_extension == '':    #file with no extension
                print("Can't deal with this kind of file! File has no extension :/")

            else:
                if not os.path.exists(os.getcwd() + "\\" + file_name):
                    os.mkdir(f"{filename[:-len(file_extension)]}")
                
                    move(str(os.getcwd() + "\\" + (filename)), str(os.getcwd() + "\\" + filename[:-len(file_extension)] + "\\" + filename))
                    counter+=1

                else:
                    print('Folder already exists')

                    move(str(os.getcwd() + "\\" + (filename)), str(os.getcwd() + "\\" + filename[:-len(file_extension)] + "\\" + filename))
                    counter+=1

    if counter == 0:
        print('There is nothing I can do here! Closing here..')
    else:
        print(f'{counter} file(s) were moved!')
        

if __name__ == "__main__":
    mover()
else:
    print("You're calling this from another file! This is not supported *yet*\nPlease run this as a standalone script :)")