import os
import platform
import datetime
import os.path, time
from os import listdir
from os.path import isfile, join
from datetime import datetime
from os import scandir
import shutil
import tkinter
import tkinter.filedialog
"""for i in range(1,100):
    os.makedirs(os.path.join('folder', 'subfolder' + str(i)) + '/folder' + str(i))
"""

def check_dir(folderDate):
    dir_entries = scandir(mypath)
    for entry in dir_entries:
        if entry.name == folderDate and entry.is_dir():
            return True
        else:
            continue
    return False
    
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files(mypath):
    dir_entries = scandir(mypath)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            createdDate = convert_date(info.st_ctime)
            modifiedDate = convert_date(info.st_mtime)
            """print(f'{entry.name}\t Created: '+ createdDate)
            print(f'{entry.name}\t Last Modified: '+ modifiedDate)"""
            folderDate = modifiedDate
            if (check_dir(folderDate)):
                """print ("Directory Exists")"""
                shutil.move(mypath+"/"+entry.name, mypath+"/"+folderDate+"/"+entry.name)
            else:
                os.makedirs(mypath+"/"+folderDate)
                shutil.move(mypath+"/"+entry.name, mypath+"/"+folderDate+"/"+entry.name)
            

try:
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window

    currdir = os.getcwd()
    mypath = tkinter.filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

    """mypath =os.path.abspath("C:/Users/manid_000/Pictures/testing")"""
    print("Program has initiated")
    get_files(mypath)
    time.sleep(1)
except:
    print("Something else went wrong")
else:
    print("Program executed successfully")
    time.sleep(1)
