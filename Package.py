class Package:
    def __init__(self, name, download_url, upload_date):
        self.name = name
        self.download_url = download_url
        self.upload_date = upload_date

    def download(self, root_directory="."):
        """
        download this package to root_directory in the path of the package as it shown in the download_url
        """
        raise NotImplemented("Not implemented!")
