import datetime
from pytz import timezone

from dotenv import load_dotenv
load_dotenv()


x = datetime.datetime.now()
print(x)

# localized = timezone("Asia/Kolkata")
# print(localized.localize(x))

# print(x.astimezone(timezone("Asia/Kolkata")))


# from dropbox_setup import DBX
# from dotenv import load_dotenv
# load_dotenv()


# x = DBX.sharing_create_shared_link_with_settings("/profile_pictures/")

# print(x)