from dropbox_setup import DBX
from user import models as user_models


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

        try:
            DBX.sharing_create_shared_link_with_settings(upload_path)
        except Exception as e:
            #print(e)
            pass

        k = DBX.sharing_get_shared_links(upload_path)
        ### store link
        await user_models.update_profile_picture(user_uid, k.links[0].url)
        
        return True

    except Exception as e:
        print(e)
        return False


async def create_profile_picture_with_link(user_uid, picture):
    try:
        upload_path = f"/profile_pictures/{user_uid}/no_profile_pic.jpg"
        x = DBX.files_upload(picture, upload_path)
        
        try:
            DBX.sharing_create_shared_link_with_settings(upload_path)
        except Exception as e:
            #print(e)
            pass

        k = DBX.sharing_get_shared_links(upload_path)
        #print(k.links[0].url)
        ### store link
        await user_models.update_profile_picture(user_uid, k.links[0].url)

        return True

    except Exception as e:
        print(e)
        return False