from dotenv import load_dotenv
import dropbox
import os


load_dotenv()

DBX = dropbox.Dropbox(os.getenv("DBX_ACCESS_TOKEN"))