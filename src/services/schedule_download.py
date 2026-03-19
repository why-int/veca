from pathlib import Path

import requests

from src.config.constants import BASE_DIR

SHEET_ID = "1YXo9JeQ-stiU_dlAt10VGIWtMy4EwaJ6XyHUDeDDFEE"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"


def download_sheet() -> None:
    try:
        response: requests.Response = requests.get(url=url)
        response.raise_for_status()

        output_path = Path(f"{BASE_DIR}/data/files/sheet.csv")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file=output_path, mode="wb") as f:
            f.write(response.content)

        print(f"File successfully downloaded to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")
    except IOError as e:
        print(f"Error saving the file: {e}")


if __name__ == "__main__":
    download_sheet()
