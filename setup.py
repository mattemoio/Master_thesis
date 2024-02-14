from setuptools import setup, find_packages

setup(
    name="pyfatbands",
    version="0.1",
    author="Matteo Moioli",
    author_email="matte.moio99@gmail.com",
    description="script to plot the fatbands",
    long_description="This script gets .dat file from an eigfat2plot calculation after a SIESTA run. \n Developed during the master thesis of Matteo Moioli, CDTG University of Milan, Chemistry Dep.\n",
    url="https://github.com/mattemoio/Master_thesis/tree/main/pyfatbands",
    packages=find_packages(),
    install_requires=["numpy", "matplotlib"],
    entry_points= {
        "console_scripts": [
            "pyfatbands=pyfatbands.fatbands:main"
        ],
    }
)
