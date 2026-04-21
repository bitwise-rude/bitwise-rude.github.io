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
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap" rel="stylesheet">

  <title>My Blog</title>
  <style>
    body{
	background-color:#0a181f;
	color: white;
	font-family: sans-serif;
	font-style:normal;
    }

    #navbar ul li a {
	color:#e5ffcc;
    }

    #navbar ul {
	list-style-type:none;
	display: flex;
	justify-content:space-evenly;
	text-decoration:none;
	width:80%;
	color:#e5ffcc;
    }

    #navbar ul li:hover{
	cursor: pointer;
	transform: translate(0,-2px);
    }

    .grid { 
	margin-left:10px;
	display: grid; gap: 20px; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }

    .card { 
	border: 1px solid #ddd; padding: 10px; border-radius: 10px;
    }

    img { 
	width: 100%; border-radius: 8px; 
    }

    h2 {
	margin-left:30px;
	text-decoration:underline;
	color:#bdffeb;
	font-family: "Dancing Script", cursive;
    }
    
    a {
	text-decoration:none;
	color:white;
    }

    #prolouge {
	font-family: Times;
	font-size:25px;
	margin-left : 30px;
	color:white;
    }

  </style>
</head>
<body>
    <div id='navbar'>
	<ul>
	    <li> <a href="">Home</a> </li>
	    <li> <a href='#blog'>Blogs</a> </li>
	</ul>
    </div>
    <p id="prolouge">Hey there! It's me Meyan Adhikari. Contact me @<a href="mailto:dareludum@gmail.com">mail</a></p>
    <br>
    <h2 id='blog'>My Blogs</h2> 
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
