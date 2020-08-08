from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from datetime import datetime
import dropbox, os, random, base64

load_dotenv()

dbx = dropbox.Dropbox(os.getenv('DROPBOX_TOKEN'))

def upload(image):
  filename = f'{datetime.now()}-{random.randint(0,9999)}'

  file_to = f'/images/{filename}.png'

  base64_img_bytes = image.encode('utf-8')
  decoded_image_data = base64.decodebytes(base64_img_bytes)

  res = dbx.files_upload(decoded_image_data, file_to)

  link = dbx.sharing_create_shared_link(file_to)
  url = get_url(link)
  return url
  

def get_url(link):
  new_ur = f'https://dl.dropboxusercontent.com/s/{link.url[26:-5]}'
  return new_ur