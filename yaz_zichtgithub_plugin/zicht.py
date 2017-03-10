import collections
import github
import github.GithubObject
import json
import texttable
import yaz

from .github import Github
from .log import logger, set_verbose


class DependencyMatrix(yaz.BasePlugin):
    @yaz.dependency
    def set_github(self, github: Github):
        self.github = github.get_service()

    @yaz.task
    def print(self, limit: int = 666, width: int = 500, verbose: bool = False):
        set_verbose(verbose)
        repo_names, dependencies = self.generate(limit)

        logger.info('formatting dependency table')
        repo_names = sorted(repo_names)
        table = texttable.Texttable(width)
        table.header([''] + repo_names)
        for package_name, deps in sorted(dependencies.items()):
            table.add_row([package_name] + [deps.get(repo_name, '') for repo_name in repo_names])

        print(table.draw())

    def generate(self, limit: int):
        repo_names = set()
        dependencies = collections.defaultdict(dict)
        for index, repo in enumerate(self.get_repos()[:limit], 1):
            deps = self.get_dependencies(repo)
            logger.info("#%s found %s dependencies for %s", index, len(deps), repo.name)
            if deps:
                repo_names.add(repo.name)
                for package_name, package_version in deps.items():
                    dependencies[package_name][repo.name] = package_version
        return repo_names, dependencies

    def get_repos(self):
        return self.github.get_user().get_repos()

    def get_dependencies(self, repo, ref=github.GithubObject.NotSet):
        try:
            file = repo.get_file_contents('/composer.lock', ref)
        except github.GithubException:
            return {}
        data = json.loads(file.decoded_content.decode())

        return {package['name']: package['version'] for package in data['packages']}
