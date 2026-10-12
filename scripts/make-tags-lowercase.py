import os

from pathlib import Path

from ruamel.yaml import YAML

FOLDER = Path(__file__).parent / ".." / "content" / "blog"

def process_page(path: Path):
    print(f"Processing {path.resolve()}...")

    if path.is_dir():
        path = path / "index.md"

    frontmatter, content = path.read_text().lstrip().split("\n---", 1)
    frontmatter += "\n"

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent = 2
    yaml.block_seq_indent = None

    data = yaml.load(frontmatter)

    if "tags" not in data:
        print("\tNo tags found, nothing to do")
        return

    data["tags"] = [tag.lower() for tag in data["tags"]]

    with open(path, mode="w") as f:
        f.write("---\n")
        yaml.dump(data, f)
        f.write("---")
        f.write(content)

if __name__ == "__main__":
    for entry in os.scandir(FOLDER):
        if not entry.name.endswith(".md") and not entry.is_dir():
            continue
        process_page(Path(entry.path))
