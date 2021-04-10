from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers
from storage import controllers as storage_controllers


async def create_folder(classroom_uid, folder_name, path, token):
    res = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    if res:
        res = await storage_controllers.create_folder(folder_name, path)
        if res == True:
            return StandardResponseBody(
                True, "Folder created", token.token_value
            )
        elif res == "exists":
            return StandardResponseBody(
                False, "Folder already exists", token.token_value
            )
        return StandardResponseBody(
            False, "Folder could not be created", token.token_value
        )
    return StandardResponseBody(
        False, "User not authorized"
    )


async def upload_file(token, classroom_uid, path, file):
    res = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    if res:
        res2 = await storage_controllers.upload_file(path, file)
        if res2:
            return StandardResponseBody(
                True, "File uploaded", token.token_value
            )
        return StandardResponseBody(
            False, "File could not be uploaded", token.token_value
        )
    return StandardResponseBody(
        False, "User not authorized."
    )


async def get_files_and_folders(classroom_uid, path, token):
    res1 = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    res2 = await classroom_controllers.if_user_enrolled(classroom_uid, token.user_id)
    if classroom_uid in path:
        if res1 or res2:
            res = await storage_controllers.get_files_and_folders(path)
            if res:
                return StandardResponseBody(
                    True, "Files retrieved", token.token_value, res
                )
            elif res == []:
                return StandardResponseBody(
                    True, "Files retrieved", token.token_value, []
                )
            return StandardResponseBody(
                False, "Files could not be retrieved", token.token_value
            )
    return StandardResponseBody(
        False, "User not authorized"
    )


async def get_file_download_link(classroom_uid, path, token):
    res1 = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    res2 = await classroom_controllers.if_user_enrolled(classroom_uid, token.user_id)
    if res1 or res2:
        res = await storage_controllers.get_file_download_link(path)
        if res:
            return StandardResponseBody(
            True, "Link retrieved", token, res
        )
    return StandardResponseBody(
        False, "User not authorized"
    )


async def delete_file(classroom_uid, path, token):
    res = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    if res:
        res = await storage_controllers.delete_file(path)
        if res == True:
            return StandardResponseBody(
                True, "File / folder deleted", token.token_value
            )
        return StandardResponseBody(
            False, "File / folder could not be deleted", token.token_value
        )
    return StandardResponseBody(
        False, "User not authorized"
    )