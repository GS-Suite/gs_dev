from responses.standard_response_body import StandardResponseBody
from classrooms import controllers as classroom_controllers
from storage import controllers as storage_controllers


async def create_folder(classroom_uid, folder_name, path, token):
    res = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    if res:
        res = await storage_controllers.create_folder(classroom_uid, folder_name, path)
        if res == True:
            return StandardResponseBody(
                True, "Folder created", token.token_value
            )
        elif res == "exists":
            return StandardResponseBody(
                False, "Folder already exists", token.token_value
            )
        return StandardResponseBody(
            False, "Folder not created"
        )



async def get_files_and_folders(classroom_uid, path, token):
    res = await classroom_controllers.check_user_if_creator(classroom_uid, token.user_id)
    if res:
        res = await storage_controllers.get_files_and_folders(classroom_uid, path)
        if res:
            return StandardResponseBody(
                True, "Files retrieved", token.token_value, res
            )
        return StandardResponseBody(
            False, "Files not retrieved"
        )