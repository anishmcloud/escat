import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="escat",
    version="0.0.1",
    author="Anish Mashankar",
    author_email="anishmcloud@gmail.com",
    description="Command line wrapper for Elasticsearch CAT API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itisanish/escat",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)