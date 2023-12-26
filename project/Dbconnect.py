import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from uuid import uuid4
import subprocess

proId = "plant-aaef"
cred = credentials.Certificate("./plant.json")
default_app = firebase_admin.initialize_app(cred,{
'storageBucket' :f"{proId}.appspot.com"})

bucket = storage.bucket()

def fileUpload(file):
	blob = bucket.bolb(file)
	new_token = uuid4()
	metadata = {"firebaseStorageDownloadTokens" :new_token}
	blob.metadata =metadata
	blob.upload_from_filename(filename=file,content_type="image/jpeg")
	print("upload")
	
def camera_snapshot():
	subtitle = "SmartFarm/MTUWK6P8BIkRavItd4VX"
	suffix=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'.jpg'
	filename = "_".join([subtitle,suffix])
	subprocess.call("libcamera-jpeg -o /home/smartFarm/Desktop/project/image_store/{}".format(filename),shell=True)
	print("asdf","\n\n\n\n")
	fileUpload(filename)
	
	
camera_snapshot()
