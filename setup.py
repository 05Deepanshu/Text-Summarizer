import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME ="Text-Summarizer"
AUTHOR_USER_NAME = "05Deepanshu"
SRC_REPO =  "textSummarizer"
AUTHOR_EMAIL = "deepanshukatariya200@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="05Deepanshu",
    author_email="deepanshukatariya200@gmail.com",
    description="A small python package for NLP app"
    "which can summarize the given text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/05Deepanshu/Text-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/05Deepanshu/Text-Summarizer/issues",
    },
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where="src")
)    