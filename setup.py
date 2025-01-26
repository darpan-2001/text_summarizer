import setuptools
with open('README.md', 'r') as f:
    long_description = f.read()


__version__ = "1.0.0"
REPO_NAME = "text_summarizer"
AUTHOR_USER_NAME = "darpan-2001"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "darpanchanana512@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarizer application",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)