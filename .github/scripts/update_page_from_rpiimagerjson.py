import click
import json
import os
import sys
import yaml


def read_rpi_imager_json(path):
    with open(path, "r") as f:
        return json.load(f)


def read_octopi_data(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def write_octopi_data(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f)


def parse_versions(octopi_and_octoprint_version):
    # formats:
    # "OctoPi 0.18.0 with OctoPrint 1.7.0"
    # "OctoPi 0.18.0 with OctoPrint 1.7.0 (build aabbccdd)"
    # "OctoPi 0.18.0 with OctoPrint 1.7.0 (build aabbccdd from branch foo)"
    octopi, octoprint = octopi_and_octoprint_version.split(" with ")
    octopi_version = octopi.split(" ")[1]
    octoprint_version = octoprint.split(" ")[1]
    return octopi_version, octoprint_version


def generate_data(name, octopi_and_octoprint_version, sha256, url):
    octopi_version, octoprint_version = parse_versions(octopi_and_octoprint_version)
    return {
        "name": name,
        "octoprint_version": octoprint_version,
        "octopi_version": octopi_version,
        "sha256": sha256,
        "url": url,
    }


def convert_rpi_imager_json(data):
    return list(
        map(
            lambda x: generate_data(
                x["name"], x["description"], x["image_download_sha256"], x["url"]
            ),
            filter(
                lambda x: "subitems" not in x and "subitems_url" not in x,
                data["os_list"],
            ),
        )
    )


def update_octopi_data(path, latest, latest_cam, next_octoprint):
    data = read_octopi_data(path)

    print(
        f"Updating latest to OctoPi {latest['octopi_version']} with OctoPrint {latest['octoprint_version']}"
    )
    data["latest"].update(latest)

    if latest_cam:
        print(
            f"Updating latest_cam to OctoPi {latest_cam['octopi_version']} with OctoPrint {latest_cam['octoprint_version']}"
        )
        if "latest_cam" not in data:
            data["latest_cam"] = dict()
        data["latest_cam"].update(latest_cam)

    if next_octoprint:
        print(
            f"Updating next_octoprint to OctoPi {next_octoprint['octopi_version']} with OctoPrint {next_octoprint['octoprint_version']}"
        )
        if "next_octoprint" not in data:
            data["next_octoprint"] = dict()
        data["next_octoprint"].update(next_octoprint)

    write_octopi_data(path, data)


@click.command()
@click.argument(
    "rpi_imager_json",
    default=os.path.join(
        os.path.dirname(__file__), "..", "..", "files", "rpi-imager.json"
    ),
)
@click.argument(
    "octopi_yaml",
    default=os.path.join(os.path.dirname(__file__), "..", "..", "_data", "octopi.yaml"),
)
def main(rpi_imager_json, octopi_yaml):
    rpi_imager_data = read_rpi_imager_json(rpi_imager_json)
    converted = convert_rpi_imager_json(rpi_imager_data)

    if not converted:
        # not even a stable release, fail
        print("Couldn't find a stable OctoPi release!")
        sys.exit(-1)

    latest = converted[0]
    latest_cam = None
    next_octoprint = None

    if len(converted) > 1:
        # if there's more than one, there might be an RC or camera stack here
        for entry in converted:
            if "rc" in entry["octoprint_version"]:
                next_octoprint = entry
            elif "(new camera stack)" in entry["name"]:
                latest_cam = entry

    update_octopi_data(octopi_yaml, latest, latest_cam, next_octoprint)
    print("Updated OctoPi data")


if __name__ == "__main__":
    main()
