from dotenv import load_dotenv
import dropbox
import os


load_dotenv()

DBX = dropbox.Dropbox(os.getenv("DBX_ACCESS_TOKEN"))

'''
db_path = "/upload test/test.jpg"
file_path = "C:/Users/keane/Desktop/test.jpg"
download_path = "C:/Users/keane/Desktop/download_test.jpg"
'''
'''dbx.files_upload(
    open(file_path, "rb").read(), 
    db_path
)'''
'''
with open(download_path, "wb") as f:
    metadata, res = BOX.files_download(path = db_path)
    f.write(res.content)'''
