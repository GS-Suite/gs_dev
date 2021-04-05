from dropbox_setup import DBX
import dropbox


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


async def create_folder(folder_name, path):
    try:
        upload_path = f"{path}/{folder_name}"
        x = DBX.files_create_folder(upload_path)
        if x:
            return True
    except Exception as e:
        print(e)
        return False


async def get_files_and_folders(full_path):
    try:
        res = DBX.files_list_folder(full_path)
        results = []
        if res:
            for file in res.entries:
                x = {}
                #print(type(file) == dropbox.files.FileMetadata)
                if type(file) == dropbox.files.FolderMetadata:
                    x = {
                        "type": "folder",
                        "name": file.name,
                        "path": file.path_display,
                    }
                elif type(file) == dropbox.files.FileMetadata:
                    x = {
                        "type": "file",
                        "name": file.name,
                        "path": file.path_display,
                        "date_modified": file.server_modified,
                        "content_hash": file.content_hash,
                        "size": file.size
                    }
                results.append(x)
            return results
    except Exception as e:
        print(e)
    return False


async def delete_file(path):
    try:
        x = DBX.files_delete(path)
        if x:
            return True
    except Exception as e:
        print(e)
        return False