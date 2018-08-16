import re

import requests

from ..Project import Project


class PypiProject(Project):
    def get_requires_dist(self):
        requires_dist = self.data["info"]["requires_dist"]
        if requires_dist:
            return [re.search("[^; ]*", dist).group() for dist in requires_dist]

    def get_packages_to_download(self):
        pass

    def get_project_data(self):
        json_url = self.get_json_url()
        return requests.get(json_url).json()

    def get_json_url(self):
        return "https://pypi.org/pypi/{}/json".format(self.name)

