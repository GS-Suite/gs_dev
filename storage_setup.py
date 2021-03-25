import dropbox


dbx_access_token = "nWV4J7tifZEAAAAAAAAAAbUK4zh2bIY9oqOJfYZ-VLWvt4yVTGksAKVZ5Ko3juT_"
DBX = dropbox.Dropbox(dbx_access_token)


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

async def change_profile_picture(user_uid, picture, filename):
    try:
        ### delete previous pictures
        x =  DBX.files_list_folder(f"/profile_pictures/{user_uid}/").entries
        for i in x:
            try:
                path = i.path_display
                DBX.files_delete_v2(path)
            except Exception as e:
                print(e)
        
        upload_path = f"/profile_pictures/{user_uid}/{filename}"
        x = DBX.files_upload(picture, upload_path)
        return True
    except Exception as e:
        print(e)
        return False