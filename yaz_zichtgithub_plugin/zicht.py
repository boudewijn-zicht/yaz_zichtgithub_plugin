import os

import github
import github.GithubObject
import json
import yaz

from .spreadsheet import VersionMatrixWorksheet
from .github import Github
from .log import set_verbose


class DependencyMatrix(yaz.BasePlugin):
    json_key_file = "~/.yaz/zicht-dependency-matrix-8d2c5244262f.json"
    sheet_key = "1vEAqgWz4DROS09r1mnODoxbaybOIlBpc2m9wSN98gf0"

    @yaz.dependency
    def set_github(self, github: Github):
        self.github = github.get_service()

    @yaz.task
    def update_spreadsheet(self, limit: int = 666, verbose: bool = False):
        set_verbose(verbose)

        worksheet = VersionMatrixWorksheet(os.path.expanduser(self.json_key_file), self.sheet_key)
        worksheet.set_updating()
        try:
            for repo in self.get_repos()[:limit]:
                dependencies = self.get_dependencies(repo)
                if dependencies:
                    worksheet.set_dependencies(repo, dependencies)
        finally:
            worksheet.unset_updating()

    def get_repos(self):
        return self.github.get_user().get_repos()

    def get_dependencies(self, repo, ref=github.GithubObject.NotSet):
        try:
            file = repo.get_file_contents('/composer.lock', ref)
        except github.GithubException:
            return {}
        data = json.loads(file.decoded_content.decode())

        return {package['name']: package['version'] for package in data['packages']}
