from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("LICENSE", "r", encoding="utf-8") as fh:
    _license = fh.read()

setup(
    # Package name:
    name="popt_performance",

    # Package number (initial):
    version="0.0.1",

    # Package author details:
    author="Jorge Rivero Dones",
    author_email="jorivero83@gmail.com",

    # Packages
    packages=["popt_performance"],

    # Include additional files into the package
    include_package_data=False,

    # Details
    url="https://github.com/jorivero83/popt_performance",

    #
    # license="LICENSE.txt",
    description="Dashboard to see the portfolio evolution and it's metrics.",

    long_description=long_description,
    long_description_content_type="text/markdown",
    license=_license,

    # Dependent packages (distributions)
    install_requires=[
        "numpy",
        "pandas",
        "streamlit",
        "yahoo_fin"
    ],
)