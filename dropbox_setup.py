from dotenv import load_dotenv
import dropbox
import os


# load_dotenv()

# DBX = dropbox.Dropbox(os.getenv("DBX_ACCESS_TOKEN"))

DBX_ACCESS_TOKEN='lPXK0INBmnMAAAAAAAAAAWH2WeyIpHlt2VyvduFtVF1ObgCx5Qs46b0fjby_XcLY'

DBX = dropbox.Dropbox(DBX_ACCESS_TOKEN)


