import os
from shutil import move
from pathlib import Path
from tkinter.filedialog import askdirectory

directory = Path(askdirectory())
#print(directory)

if not directory.is_dir() or str(directory) == ".":    # No valid directory - Closes program
    input("Can't continue without a valid directory! Press enter to exit.. ")
    if True:
        exit(0)
os.chdir(directory)

def mover():
    counter:int = 0
    for filename in directory.iterdir():
        if filename.is_file() and filename != Path(__file__) and not filename.suffix == '':
            counter+=1 
            #print(f"{filename} :: {os.path.isdir(filename)}")
            file_extension = filename.suffix

            new_dir = Path(str(filename)[:-len(file_extension)])
            if not new_dir.exists():
                #print('Folder doesn't exist)
                new_dir.mkdir()
                move(filename, new_dir)
            else:
                #print('Folder already exists')
                move(filename, new_dir)

        elif filename.is_dir():
            print('This is already a folder!')

        elif filename == Path(__file__):
            print('This file represents myself!')

        elif filename.is_file() and filename.suffix == '':
            print('This file has no extension!')
    
    if counter == 0:
        input("Can't continue without a valid directory! Press enter to exit.. ")
        if True:
            exit(0)
    else:
        input(f'{counter} file(s) were moved! Press enter to exit.. ')
        if True:
            exit(0)


if __name__ == "__main__":
    mover()
else:
    print("You're calling this from another file! This is not supported *yet*\nPlease run this as a standalone script :)")