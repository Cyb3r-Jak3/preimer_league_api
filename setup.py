from setuptools import setup
from premier_league_api import __version__

install_reqs = open("requirements.txt").readlines()
dev_reqs = open("requirements-dev.txt").readlines()

readme = open("README.md").read()

setup(
        name="premier_league_api",
        version=__version__,
        description="API for pulling Premier League Data",
        long_description=readme,
        long_description_content_type="text/markdown",
        author="Cyb3r-Jak3",
        author_email="git@cyberjake.xyz",
        url="https://github.com/Cyb3r-Jak3/premier_league_api",
        project_urls={
            "Changelog": "https://github.com/Cyb3r-Jak3/premier_league_api/blob/main/CHANGELOG.md",
            "Issues": "https://github.com/Cyb3r-Jak3/premier_league_api/issues"
        },
        download_url="https://github.com/Cyb3r-Jak3/premier_league_api/releases/latest",
        packages=[
            "premier_league_api"
        ],
        package_dir={"premier_league_api": "premier_league_api"},
        tests_require=dev_reqs[1:],
        install_requires=install_reqs,
        license="MPL 2.0",
        zip_safe=True,
        keywords="premier league, REST, api client, REST API",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
)
