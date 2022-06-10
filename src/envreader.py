from cmath import log
import os
from tokenize import String
from dotenv import load_dotenv
from pathlib import Path
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_var(variable: String) -> String:
    
    dotenv_path = Path('./.env')
    load_dotenv(dotenv_path)
    
    if(os.getenv(variable)):
        return os.getenv(variable)
    else:
        logger.error("Env var missing", exc_info=1)
        return ""

    