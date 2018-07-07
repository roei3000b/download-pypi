class Package:
    def __init__(self, name, download_url):
        self.name = name
        self.download_url = download_url

    def download(self, root_directory="."):
        """
        download this package to root_directory in the path of the package as it shown in the download_url
        """
        raise NotImplemented("Not implemented!")

