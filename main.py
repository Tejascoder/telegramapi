from typing import Union

from fastapi import FastAPI
from pymongo import MongoClient
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os, gridfs
from PIL import Image
import io
from database import Registered_users,users_screenshot
from io import StringIO
from io import BytesIO
import base64

app = FastAPI()


@app.get("/")
def landing_page():

    return {"Hello": "World"}