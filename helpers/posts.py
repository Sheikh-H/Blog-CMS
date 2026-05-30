from pathlib import Path
import os
import json

base_dir = Path(__file__).resolve().parent.parent
posts_file = base_dir / "instance" / "posts.json"


def add_post(title, description, content):
    if not os.path.exists(posts_file):
        with open(posts_file, "w") as f:
            json.dump([], f)

    with open(posts_file, "r") as f:
        data = json.load(f)
    _id = max((post["id"] for post in data), default=0) + 1
    post = {
        "id": _id,
        "title": title.title(),
        "description": description,
        "content": content,
    }
    data.append(post)
    with open(posts_file, "w") as f:
        json.dump(data, f, indent=2)


def delete_post(id):
    if not os.path.exists(posts_file):
        with open(posts_file, "w") as f:
            json.dump([], f)

    with open(posts_file, "r") as f:
        data = json.load(f)
    for i, post in enumerate(data):
        if post["id"] == id:
            del data[i]
    with open(posts_file, "w") as f:
        json.dump(data, f, indent=2)


def update_post(id, title=None, description=None, content=None):
    if not os.path.exists(posts_file):
        with open(posts_file, "w") as f:
            json.dump([], f)

    with open(posts_file, "r") as f:
        data = json.load(f)

    for post in data:
        if post["id"] == id:
            if title:
                post["title"] = title
            else:
                post["title"] = post["title"]
            if description:
                post["description"] = description
            else:
                post["description"] = post["description"]
            if content:
                post["content"] = content
            else:
                post["content"] = post["content"]
    with open(posts_file, "w") as f:
        json.dump(data, f, indent=2)
