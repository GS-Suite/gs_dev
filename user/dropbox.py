from dropbox_setup import DBX


async def delete_profile_pictures(user_uid):
    x =  DBX.files_list_folder(f"/profile_pictures/{user_uid}/").entries
    for i in x:
        try:
            path = i.path_display
            DBX.files_delete_v2(path)
        except Exception as e:
            print(e)


async def change_profile_picture(user_uid, picture, filename):
    try:
        upload_path = f"/profile_pictures/{user_uid}/{filename}"
        x = DBX.files_upload(picture, upload_path)
        return x
    except Exception as e:
        print(e)
        return False