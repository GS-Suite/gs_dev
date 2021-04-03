from dropbox_setup import DBX


async def create_classroom_folder(classroom_uid):
    try:
        upload_path = f"/classrooms/{classroom_uid}"
        x = DBX.files_create_folder(upload_path)
        if x:
            return True
    except Exception as e:
        print(e)
        return False


async def get_classroom_folder_link(classroom_uid):
    try:
        path = f"/classrooms/{classroom_uid}"
        try:
            DBX.sharing_create_shared_link_with_settings(path)
        except Exception as e:
            #print(e)
            pass
        k = DBX.sharing_get_shared_links(path)

        return k.links[0].url

    except Exception as e:
        print(e)
        return False