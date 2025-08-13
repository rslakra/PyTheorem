#
# Author: Rohtash Lakra
#
import json
import sys
from datetime import time

import yaml

from configs.base import ROOT_DIR
from core.logger.base import getLogger

logger = getLogger(__name__)


def read_env_file(env_file):
    """Reads the environment file and returns a dictionary."""
    logger.debug("Reading env file=%s", env_file)
    
    env_vars = {}
    with open(env_file, 'r') as f:
        for line in f:
            if line.startswith('#') or '=' not in line:
                continue
            
            key, value = line.strip().split('=', 1)
            env_vars[key] = value.strip("'").strip('"')
    
    return env_vars


def read_yaml_file(file_path: str):
    """Reads the YAML file and returns a dictionary."""
    logger.debug("Reading YAML file=%s", file_path)
    contents = None
    if file_path is None:
        raise Exception("The 'file_path' should provide.")
    
    # open a file in readonly mode
    with open(file_path) as file:
        contents = yaml.safe_load(file)
    
    return contents


def read_json_file(file_path: str):
    """Reads the JSON file and returns a dictionary."""
    logger.debug("Reading JSON file=%s", file_path)
    contents = None
    if file_path is None:
        raise Exception("The 'file_path' should provide.")
    
    # open a file in readonly mode
    with open(file_path) as file:
        contents = json.load(file)
    
    return contents


if __name__ == "__main__":
    try:
        logger.info("[%s] Starting ...", __name__)
        startTime = time.time()
        logger.info("startTime=%s", startTime)
        args = sys.argv[1:]
        logger.info("args=%s", args)
        # load testing event
        fileName = "orders.json"
        orders = read_json_file(f"{ROOT_DIR}/data/{fileName}")
        logger.info("orders=%s", orders)
        endTime = time.time()
        logger.info("endTime=%s", endTime)
        logger.info(f"Time taken= {float(endTime - startTime):.2f} secs")
    except Exception as e:
        logger.error("[%s] Error=%s", __name__, str(e))
    
    logger.info("[%s] Ended.", __name__)
