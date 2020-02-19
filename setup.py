from setuptools import setup

setup(
    name="bayfordbury",
    url="https://github.com/herts-astrostudents/Bayfordbury_project",

    author="Centre for Astrophysics Research, University of Hertfordshire",
    author_email="m.lisogorskyi@herts.ac.uk",

    packages=["api"],
    install_requires=["astropy"],
    
    version="0.1",
    license="GNU General Public License v3.0",

    description="An example of a python package from pre-existing code",
    long_description=open("README.md").read(),
)