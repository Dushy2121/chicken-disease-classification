import  os
from box.exceptions import BoxValueError
import yaml
from src.cnnclassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64 

#this function is used to read the yaml file and return the content as a dictionary.

@ensure_annotations
def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a dictionary.
    
    Args:
        path_to_yaml (str): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"File not found: {path_to_yaml}. Error: {e}")
        raise e
    except BoxValueError as e:
        logger.error(f"Error in YAML file structure: {path_to_yaml}. Error: {e}")
        raise e
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {path_to_yaml}. Error: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred while reading the YAML file: {path_to_yaml}. Error: {e}")
        raise e

#the directory is created if it does not exist. The function takes a list of directories as input and creates them one by one.   
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, prints the status of directory creation.
        
    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory '{path}' created or already exists.")



#the save function is used to save the model in the specified path. The function takes the path and the model as 
# input and saves the model in the specified path.
@ensure_annotations
def save_json(path: str, data: dict) -> None:
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path_to_json (str): Path to save the JSON file.
        data (dict): Dictionary to save as JSON.
        
    Returns:
        None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"JSON file saved at: {path}")    

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data as a binary file using joblib.
    
    Args:
        data (Any): Data to save as a binary file.
        path (str): Path to save the binary file.
        
    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (str): Path to the binary file.
        
    Returns:
        Any: Loaded data.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(file_path: str) -> str:
    """
    Returns the size of a file in a human-readable format.
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        str: Size of the file in a human-readable format.
    """
    size_in_kb = os.path.getsize(file_path/1024)
    return f"{size_in_kb:.2f} KB"

def decodeImage(imagstring,filename):
    imgdata = base64.b64decode(imagstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')