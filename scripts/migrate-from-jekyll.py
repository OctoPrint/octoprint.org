import datetime
import os
import re
import shutil

from pathlib import Path

import markdown

from bs4 import BeautifulSoup
from ruamel.yaml import YAML


TARGET_FOLDER = Path(__file__).parents[0] / ".." / "content" / "blog"
TARGET_NAME = "{date}-{slug}"

HEADLINE_MIN = 2
HEADLINE_RE = re.compile(r"^(#+)\s+(.*)$", flags=re.MULTILINE)

YOUTUBE_RE = re.compile(r'\{% include youtube.html vid="(.*?)" %\}')

IMAGE_RE = re.compile(r'([\'"])(/assets/img/blog/.+?)\1')

AUTO_EXCERPT_MAX = 250

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()

def convert_md_headlines(text: str) -> str:
    min_level = -1

    matches = list(HEADLINE_RE.finditer(text))
    for match in matches:
        level = len(match.group(1))
        if min_level == -1 or level < min_level:
            min_level = level

    diff = HEADLINE_MIN - min_level
    if diff == 0:
        return text

    for match in matches:
        level = len(match.group(1)) + diff
        text = text.replace(match.group(0), "#" * level + " " + match.group(2))

    return text

def process_post(path: Path, category: str):
    print(f"Processing {path.resolve()}...")

    path_base = path.parents[0] / ".." / ".." / ".."

    def copy_image(src, dst, name=None):
        if not src: 
            return

        while src.startswith("/"):
            src = src[1:]

        src_path = path_base / Path(src)
        if not src_path.exists(): 
            return

        if name is None:
            name = src_path.name

        _, ext = src.rsplit(".", 1)
        target = Path(dst) / name.format(ext=ext)
        shutil.copy2(src_path, target)
        return target

    frontmatter, content = path.read_text().lstrip().split("\n---", 1)
    frontmatter += "\n"

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent = 2
    yaml.block_seq_indent = None

    data = yaml.load(frontmatter)

    # remove layout
    try:
        del data["layout"]
    except KeyError:
        pass

    # map category
    if category == "releases":
        data["tags"] = ["Release"]
    elif category == "octoprintonair":
        data["tags"] = ["OctoPrint on Air"]
    else:
        data["tags"] = [category.capitalize()]

    # rename excerpt to summary
    if "excerpt" in data:
        summary = data.pop("excerpt")
        if summary:
            data["summary"] = summary
    else:
        # no excerpt, let's look if we have a <!-- more --> comment in the content
        more = content.find("<!-- more -->")
        if more >= 0:
            data["summary"] = md_to_text(content[:more].strip())
        else:
            # no more either, let's create a mimimal excerpt...
            plain = md_to_text(content.strip())
            summary = plain[:AUTO_EXCERPT_MAX]
            data["summary"] = summary[:summary.rfind(" ")] + "..."

    # set slug
    filename = path.name
    slug = filename[len("YYYY-MM-DD-"):-len(".md")]
    data["slug"] = slug

    # rename release fields
    if "bugfix" in data:
        stable = data.pop("release")
        data["release"] = data.pop("bugfix")
        data["stable"] = stable

    # prepare page bundle
    if "date" in data:
        datestr = data["date"]
    else:
        datestr = filename[:len("YYYY-MM-DD")] + " 00:00:00 +0000"
    date = datetime.datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S %z")
    bundle = TARGET_NAME.format(date=date.strftime("%Y-%m-%d"), slug=slug)

    bundle_path = Path(TARGET_FOLDER) / Path(bundle)
    if not bundle_path.exists():
        os.mkdir(bundle_path)

    # move card & poster
    if "card" in data:
        copy_image(data.pop("card"), bundle_path, "card.{ext}")
    if "poster" in data:
        copy_image(data.pop("poster"), bundle_path, "poster.{ext}")

    if "featuredimage" in data:
        data.pop("featuredimage")

    # move post images
    img_path = bundle_path / "images"
    if "images" in data:
        images = data.pop("images")

        if not img_path.exists():
            os.mkdir(img_path)

        new_images = []
        for image in images:
            if isinstance(image, dict):
                copied = copy_image(image["url"], img_path)
                new_images.append({"url": "images/" + copied.name, "title": image.get("title")})
            else:
                copied = copy_image(image, img_path)
                new_images.append("images/" + copied.name)
        data["images"] = new_images

    # move stats images
    if "stats" in data:
        stats = data["stats"]

        stats_path = bundle_path / "stats"
        if not stats_path.exists():
            os.mkdir(stats_path)

        if "instancegraph" in stats:
            copy_image(stats.pop("instancegraph"), stats_path, "instances.{ext}")
        if "printtimegraph" in stats:
            copy_image(stats.pop("printtimegraph"), stats_path, "prints.{ext}")
        if "piecharts" in stats:
            copy_image(stats.pop("piecharts"), stats_path, "piecharts.{ext}")

    # move any other images contained in content
    for match in IMAGE_RE.finditer(content):
        if not img_path.exists():
            os.mkdir(img_path)

        copy_image(match.group(2), img_path)

    # check for youtube include
    youtube = YOUTUBE_RE.search(content)
    if youtube:
        content = content.replace(youtube.group(0), "{{< youtube " + youtube.group(1) + " >}}")

    # convert headline levels
    content = convert_md_headlines(content)

    with open(bundle_path / "index.md", mode="w") as f:
        f.write("---\n")
        yaml.dump(data, f)
        f.write("---")
        f.write(content)

def process_category(path: Path):
    category = path.name
    post_dir = path / "_posts"

    print(f"--- Processing category {category}")

    for entry in os.scandir(post_dir):
        if not entry.name.endswith(".md"):
            continue
        process_post(Path(entry.path), category)

if __name__ == "__main__":
    path = "../../octoprint.org/blog"
    for entry in os.scandir(Path(__file__).parents[0] / Path(path)):
        if not entry.is_dir():
            continue

        process_category(Path(entry.path))
