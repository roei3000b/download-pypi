class Project:

    def __init__(self, name, from_date, to_date, requires_dist=False):
        self.name = name
        self.from_date = from_date
        self.to_date = to_date
        if requires_dist:
            self.requires_dist = self.get_requires_dist()
        self.packages = []

    def get_requires_dist(self):
        """
        :return: list of all requires project as Project object
        """
        raise NotImplemented("Not implemented!")

    def get_packages_to_download(self):
        """
        :return: list  of all packages that we need to download as Package object
        """
        raise NotImplemented("Not implemented!")
