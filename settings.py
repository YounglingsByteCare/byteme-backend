import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

dotenv_path = join(dirname(abspath(__file__)), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
