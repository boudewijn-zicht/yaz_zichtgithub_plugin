=======================
A github plugin for YAZ
=======================

This YAZ plugin provides three tools:

**yaz-zicht-dependency-matrix**: this tool connects to https://github.com/zicht
and uses the composer.lock and package-lock.json files to determine the dependencies
that a project has.  These dependencies are then stored in the associated google sheet
document.

**yaz-zicht-repository-list**: this tool connects to https://github.com/zicht
and uses the repository descriptions to determine if the repo represents a library,
website, utility, or is obsolete.  It when scans the readme file to performs some checks.
The results are stored in the associated google sheet document.

**yaz-zicht-github-finder**: this tool connects to https://github.com/zicht
and allows a regexp search on a given file in all available repositories.

Installing
----------

    .. code-block:: bash

        # Install or upgrade from the main repository
        pip3 install --upgrade yaz_zichtgithub_plugin

        # Configure ~/.yaz/yaz_extension/__init__.py to include Github.token,
        # and settings for DependencyMatrix and RepositoryList (these contain
        # personal information and will not be included here)

        # Call one of the installed scripts
        yaz-zicht-dependency-matrix

        # Or
        yaz-zicht-repository-list

        # Or
        yaz-zicht-github-finder


Developing
----------

    .. code-block:: bash

        # Get the code
        git clone git@github.com:boudewijn-zicht/yaz_zichtgithub_plugin.git
        cd yaz_zichtgithub_plugin

        # Ensure you have python 3.5 or higher and yaz installed
        python3 --version
        pip3 install --upgrade yaz

        # Setup your virtual environment
        virtualenv --python=python3 env
        source env/bin/activate
        python setup.py develop

        # Run tests
        python setup.py test

        # Or run nosetests directly (allows coverage report)
        nosetests --with-cover --cover-html --cover-package yaz_zichtgithub_plugin

        # Upload a new release to pypi
        python setup.py tag
        python setup.py publish

        # Once you are done... exit your virtual environment
        deactivate


Maintainer
----------

- Boudewijn Schoon <boudewijn@zicht.nl>
