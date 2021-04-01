import datetime
from pytz import timezone

from dotenv import load_dotenv
load_dotenv()


x = datetime.datetime.now()
print(x)

localized = timezone("Asia/Kolkata")

print(localized.localize(x))