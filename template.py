import os
from pathlib import Path
import logging

#
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')
project_name="cnn_classifier"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/train.ipynb",
    "template/index.html"

]

#filepath load the file one by one and create the directory if it does not exist

for filepath in list_of_files:
    filepath=Path(filepath)
    #we have to seperate foler and file creation and return  tuple of folder and file eg. (folder, file)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        #if file is not empty then create the directory
        #create the directory if it does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory ;{filedir} for the file :{filename}")


    #check if the file exists or not and if it is empty or not
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)) and filename != "":
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file :{filename} at {filedir}")
    else:
        #if file is not empty then do not create the file and log the message
        #logging.info(f"File already exists or is not empty :{filename} at {filedir}")
        logging.info(f"{filename}File already exists or is not empty ")
        


        