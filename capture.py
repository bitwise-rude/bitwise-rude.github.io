import os
import json
from datetime import datetime

title = os.environ.get("DISC_TITLE", "")
body = os.environ.get("DISC_BODY", "")
user = os.environ.get("DISC_USER", "")
url = os.environ.get("DISC_URL", "")

entry = {
    "title": title,
    "body": body,
    "user": user,
    "url": url,
    "date": datetime.utcnow().isoformat()
}

try:
    with open("discussions.json", "r") as f:
        data = json.load(f)
except:
    data = []

data.append(entry)

with open("discussions.json", "w") as f:
    json.dump(data, f, indent=2)

