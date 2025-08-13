#
# Author: Rohtash Lakra
#
# Read .env local file
import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

from core.enums.appenv import AppEnv

_ = load_dotenv(find_dotenv())
ROOT_DIR = Path(__file__).resolve().parent.parent
print(f"ROOT_DIR={ROOT_DIR}")


class Config:
    TESTING = False
    FLASK_ENV = os.getenv('FLASK_ENV', AppEnv.PRODUCTION.value)
    APP_ENV = os.getenv('APP_ENV', AppEnv.PRODUCTION.value)
    
    # AppEnv
    env_path = ROOT_DIR / f".env.{APP_ENV}"
    should_override = AppEnv.is_local(APP_ENV)
    if env_path.exists():
        load_dotenv(env_path, override=should_override)
    else:
        load_dotenv()
    
    GOOGLE_API_VIDEO_FILES_URL = os.getenv('GOOGLE_API_VIDEO_FILES_URL', None)
    # Comma Separated Files Names
    VIDEO_FILE_NAMES = os.getenv('VIDEO_FILE_NAMES', None)
    
    PANDADOC_BASE_URL = os.getenv("PANDADOC_API_URL", "https://api.pandadoc.com")
    PANDADOC_API_KEY = os.getenv("PANDADOC_API_KEY", None)
