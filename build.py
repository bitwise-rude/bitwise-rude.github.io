import os
import json

BLOG_DIR = "blogs"

posts = []

for folder in os.listdir(BLOG_DIR):
    path = os.path.join(BLOG_DIR, folder)

    if not os.path.isdir(path):
        continue

    config_path = os.path.join(path, "config.json")

    # maybe folders without config TODO:??
    if not os.path.exists(config_path):
        continue

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except:
        continue

    title = config.get("title", folder)
    thumbnail = config.get("thumbnail", "")
    desc = config.get("description", "")
    date = config.get("date", "")

    posts.append({
        "folder": folder,
        "title": title,
        "thumbnail": thumbnail,
        "desc": desc,
        "date": date,
    })

html = """
<!DOCTYPE html>
<html>
<head>
  <title>My Blog</title>
  <style>
    body { font-family: sans-serif; }
    .grid { display: grid; gap: 20px; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }
    .card { border: 1px solid #ddd; padding: 10px; border-radius: 10px; }
    img { width: 100%; border-radius: 8px; }
  </style>
</head>
<body>
  <h1>Blogs</h1>
  <div class="grid">
"""

for p in posts:
    img_tag = f'<img src="blogs/{p["folder"]}/{p["thumbnail"]}">' if p["thumbnail"] else ""

    html += f"""
    <div class="card">
      <a href="blogs/{p['folder']}/index.html">
        {img_tag}
        <h3>{p['title']}</h3>
      </a>
      <p>{p['desc']}</p>
      <p>{p['date']}</p>
    </div>
    """

html += """
  </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

# ugh
