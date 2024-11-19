import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads the config.yaml file and returns a ConfigBox object."""
    try:
        with open(Path(path_to_yaml), "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file {path_to_yaml} read successfully.")
            return ConfigBox(content)
        
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates list of directories if they do not exist."""
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory {path} created.")
        else:
            if verbose:
                logger.info(f"Directory {path} already exists.")


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of the file in KB"""
    size = round(os.path.getsize(path)/1024)
    return f"{size} KB"