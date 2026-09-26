# Widevine update request logic inspired by and adapted from Kodi InputStream Helper.
# Adapted and extended by Minime, 2026-09-26.
# Original project:
# https://github.com/emilsvennesson/script.module.inputstreamhelper
#
# Licensed under the MIT License.
# See LICENSE for the full license text.
import argparse
import json
import os
import sys
import urllib.request
import zipfile
from io import BytesIO

UPDATE_URL = "https://update.googleapis.com/service/update2/json"

APP_ID = "oimompecagnajdejgnnjijobebaeigek"
VERSION = "1.4.9.1088"
UPDATER_VERSION = "151.0.7922.173"


def get_widevine(os_name, arch, output_dir):
    """Download and extract the latest Widevine CDM."""

    payload = {
        "request": {
            "@os": "",
            "@updater": "",
            "acceptformat": "crx3,download,puff,run,xz,zucc",
            "apps": [
                {
                    "appid": APP_ID,
                    "installsource": "ondemand",
                    "updatecheck": {},
                    "version": VERSION
                }
            ],
            "dedup": "cr",
            "ismachine": False,
            "arch": arch,
            "os": {
                "arch": arch,
                "platform": os_name
            },
            "protocol": "4.0",
            "updaterversion": UPDATER_VERSION
        }
    }

    # Query Google's update service
    request = urllib.request.Request(
        UPDATE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(request) as response:
            text = response.read().decode("utf-8")
    except Exception as e:
        print("ERROR: Could not contact Google's update service.")
        print(e, file=sys.stderr)
        return 1

    # Remove Google's JSON prefix: )]}'
    if text.startswith(")]}'"):
        text = text[4:]

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print("ERROR: Could not parse Google's response.")
        print(e, file=sys.stderr)
        return 1

    try:
        update = (
            data["response"]
                ["apps"][0]
                ["updatecheck"]
        )

        cdm_version = update["nextversion"]

        print(cdm_version)

        cdm_urls = (
            update["pipelines"][0]
                ["operations"][0]
                ["urls"]
        )

        # Select HTTPS URLs
        https_urls = [
            item["url"]
            for item in cdm_urls
            if item["url"].startswith("https://")
        ]

        if not https_urls:
            print("ERROR: No HTTPS download URL was provided.")
            return 1

        cdm_url = https_urls[0]

    except (KeyError, IndexError) as e:
        print("ERROR: Could not extract Widevine information.")
        print(e, file=sys.stderr)
        return 1

    # Download CRX3 file
    download_file = output_dir + "/widevine-" + cdm_version + "-aarch64.crx3"

    try:
        urllib.request.urlretrieve(
            cdm_url,
            download_file
        )
    except Exception as e:
        print("ERROR: Widevine download failed.")
        print(e, file=sys.stderr)
        return 1

    # Find ZIP data inside CRX3 file
    try:
        with open(download_file, "rb") as f:
            data = f.read()

        zip_offset = data.find(b"PK\x03\x04")

        if zip_offset == -1:
            print("ERROR: ZIP data not found in CRX3 file.")
            return 1

        # Extract the ZIP data.
        #
        # zipfile.ZipFile accepts a file-like object, so we use
        # the ZIP data directly without needing another library.

        with zipfile.ZipFile(
            BytesIO(data[zip_offset:])
        ) as archive:
            archive.extractall(output_dir)

    except zipfile.BadZipFile as e:
        print("ERROR: Invalid ZIP data inside CRX3 file.")
        print(e, file=sys.stderr)
        return 1
    except OSError as e:
        print("ERROR: Could not read/write Widevine files.")
        print(e, file=sys.stderr)
        return 1

    # Remove downloaded CRX3 after extraction.
    try:
        os.remove(download_file)
    except OSError:
        pass
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Download and extract the latest Widevine CDM."
    )

    parser.add_argument(
        "--os",
        required=True,
        help="Target operating system, e.g. Linux"
    )

    parser.add_argument(
        "--arch",
        required=True,
        help="Target architecture, e.g. arm64"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Directory where Widevine will be extracted"
    )

    args = parser.parse_args()

    return get_widevine(
        args.os,
        args.arch,
        args.output
    )
if __name__ == "__main__":
    sys.exit(main())
