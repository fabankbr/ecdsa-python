from os import path
from setuptools import setup, find_packages


with open(path.join(path.dirname(__file__), "README.md")) as readme:
    README = readme.read()


setup(
    name="fabank-ecdsa",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    description="A lightweight and fast pure python ECDSA library",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/fabankbr/ecdsa-python.git",
    author="Fabank",
    author_email="developers@fabank.com.br",
    keywords=["ecdsa", "elliptic curve", "elliptic", "curve", "fabank", "cryptograph", "secp256k1", "prime256v1"],
    version="1.0.0"
)


### Create a source distribution:

#Run ```python setup.py sdist``` inside the project directory.

### Install twine:

#```pip install twine```

### Upload package to pypi:

#```twine upload dist/*```

