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


def parse_devices(devices):
    if not devices:
        devices = ["pi1-32bit", "pi2-32bit", "pi3-32bit", "pi4-32bit"]

    result = []
    if "pi1-32bit" in devices:  # Pi1
        result += ["1A", "1A+", "1B", "1B+"]
    if "pi2-32bit" in devices:  # Pi2
        result += ["2B"]
    if "pi3-32bit" in devices or "pi3-64bit" in devices:  # Pi3
        result += ["3A+", "3B", "3B+"]
    if "pi4-32bit" in devices or "pi4-64bit" in devices:  # Pi4
        result += ["4B 1/2/4/8GB"]
    if "pi5-32bit" in devices or "pi5-64bit" in devices:  # Pi5
        result += ["5B 4/8GB"]

    # now the zeroes
    if "pi1-32bit" in devices:  # Zero & Zero W
        result += ["Zero", "Zero W"]
    if "pi3-32bit" in devices or "pi3-64bit" in devices:  # Zero 2
        result += ["Zero 2"]

    # and the 400
    if "pi4-32bit" in devices or "pi4-64bit" in devices:  # Pi4
        result += ["400"]

    if not result:
        return ""

    if len(result) == 1:
        return result[0]

    return ", ".join(result[:-1]) + " and " + result[-1]


def generate_data(name, octopi_and_octoprint_version, sha256, url, devices):
    octopi_version, octoprint_version = parse_versions(octopi_and_octoprint_version)

    return {
        "name": name,
        "octoprint_version": octoprint_version,
        "octopi_version": octopi_version,
        "sha256": sha256,
        "url": url,
        "pi_models": parse_devices(devices),
    }


def convert_rpi_imager_json(data):
    return list(
        map(
            lambda x: generate_data(
                x["name"],
                x["description"],
                x["image_download_sha256"],
                x["url"],
                x.get("devices", []),
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
