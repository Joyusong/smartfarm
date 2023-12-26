import datetime
import sys, os
import subprocess
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from uuid import uuid4

proid = "plant-a0aef"
cred = credentials.Certificate("/home/smartFarm/Desktop/project/plant.json")
default_app = firebase_admin.initialize_app(cred,{'storageBucket':f"{proid}.appspot.com"})
bucket = storage.bucket()
def fileUpload(file):
	blob = bucket.blob('SmartFarm/' +file)
	new_token = uuid4()
	metadata = {"firebaseStorageDownloadTokens":new_token}
	blob.metadata = metadata
	blob.upload_from_filename(filename = '/home/smartFarm/Desktop/project/image_store/'+file,content_type = 'image/jpeg')
	print('hello')
	print(blob.public_url)
	
def execute_camera():
	basename = "smr"
	suffix=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'.jpeg'
	filename = "_".join([basename,suffix])
	subprocess.call("libcamera-jpeg -o /home/smartFarm/Desktop/project/image_store/{}".format(filename),shell=True)
	fileUpload(filename)
	
execute_camera()
