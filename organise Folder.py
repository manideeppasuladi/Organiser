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

def check_dir(dirtype):
    dir_entries = scandir(mypath)
    for entry in dir_entries:
        if entry.name == dirtype and entry.is_dir():
            return True
        else:
            continue
    return False
    
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def getextension(name):
    filename,fileextension = os.path.splitext(name)
    if(fileextension == ".jpeg" or fileextension == ".jpg" or fileextension == ".gif" or fileextension == ".png" or fileextension == ".JPEG" or fileextension == ".JPG" or fileextension == ".GIF" or fileextension == ".PNG"):
        return "Images"
    else:
        if(fileextension == ".mp4" or fileextension == ".mov" or fileextension == ".MP4" or fileextension == ".MOV"  ):
            return "Videos"
        else:
            if (fileextension == ".mp3" or fileextension == ".MP3"):
                return "Audio"
            else:
                return "Files"


def get_files(mypath):
    dir_entries = scandir(mypath)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            
             
            dirtype = getextension(entry.name)
            """print(dirtype)"""
            if (check_dir(dirtype)):
                """print ("Directory Exists")"""
                shutil.move(mypath+"/"+entry.name, mypath+"/"+dirtype+"/"+entry.name)
            else:
                os.makedirs(mypath+"/"+dirtype)
                shutil.move(mypath+"/"+entry.name, mypath+"/"+dirtype+"/"+entry.name)
            

try:
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window

    currdir = os.getcwd()
    mypath= tkinter.filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')

    """mypath =os.path.abspath("C:/Users/manid_000/Pictures/testing")"""
    print("Program has initiated on : " + mypath)
    get_files(mypath)
    """ time.sleep(1)"""
except:
    print("Something else went wrong")
else:
    print("Program executed successfully")
    

