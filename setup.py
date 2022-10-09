from setuptools import setup, find_packages

setup(
    name="pypackage_eg",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        # if you want to develop this package instead of only using it.
        # It will be more convenient to install by `pip install -e .[dev]`
        "dev": [
            "flake8",
            "black",
            "pre-commit",
        ],
    },
)
