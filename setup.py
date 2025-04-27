import setuptools

#it is reading the readme file and storing it in long_description variable
# README.md file is in the same directory as setup.py
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "chicken-disease-classification"
AUTHOR_USER_NAME = "Dushy2121"
SRC_REPO = "cnn_classifier"
AUTHOR_EMAIL = "handedushyant2121@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Dushy2121/chicken-disease-classification",
    project_urls={
        "Bug Tracker": f"https://github.com/Dushy2121/chicken-disease-classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)