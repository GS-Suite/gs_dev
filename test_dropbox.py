import dropbox


access_token = ""
dbx = dropbox.Dropbox(access_token)
'''x = dbx.users_get_current_account()
print(x)'''

'''for entry in dbx.files_list_folder('').entries:
    print(entry)'''


db_path = "/upload test/test.jpg"
file_path = "C:/Users/keane/Desktop/test.jpg"
download_path = "C:/Users/keane/Desktop/download_test.jpg"

dbx.files_upload(
    open(file_path, "rb").read(), 
    db_path
)

with open(download_path, "wb") as f:
    metadata, res = dbx.files_download(path = db_path)
    f.write(res.content)