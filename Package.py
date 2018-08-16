import shutil
import requests


class Package:
    def __init__(self, name, download_url, upload_date):
        self.name = name
        self.download_url = download_url
        self.upload_date = upload_date

    def download(self, dest_path="."):
        """
        download this package to root_directory in the path of the package as it shown in the download_url
        """
        with requests.get(self.download_url, stream=True) as response:
            with open(dest_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
