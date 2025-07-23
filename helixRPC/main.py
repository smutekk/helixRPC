
import discordrpc

import os
import sys
from dotenv import load_dotenv

load_dotenv()

app_id = str(os.getenv("APPID"))

rpc = discordrpc.RPC(app_id=app_id)

file_name=sys.argv[1]
file_details=None
image=None

if file_name:
    file_extension = sys.argv[1].split(".")[-1]
    file_details=f"Editing {sys.argv[1]}"
else:
    file_details=f"Editing Unnamed File"    


image_dict = {
    "py": "python",
    "sh": "bash",
    "cpp": "cpp",
    "conf": "config",
    "css": "css",
    "": "none"
}

rpc.set_activity(
    state="she get : on my w till i q",
    details=f"{file_details}",
#    small_image=f"{image_dict[file_extension]}"
)

rpc.run()


