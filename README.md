# Bayfordbury_project

Github repository for the Bayfordbury project code

**NOTE : THIS IS WORK IN PROGRESS AND ONLY MEANT FOR DEVELOPMENT FOR NOW**

If you want to contribute, please read the guidelines below to make development easier for everybody, including you.

## Notes for contributors

Useful links:

101 _(explains the basics)_ : [Creating packages in python](https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/)

102 _(basics and some more details)_: [Structuring your project](https://docs.python-guide.org/writing/structure/)

Please read the above first.


# Requirements

- Python 2.7 or higher
- astropy

# Installation

## from this repository

```sh
git clone https://github.com/herts-astrostudents/Bayfordbury_project.git
cd Bayfordbury_project
python setup.py install
```

or

```sh
pip install git+https://github.com/herts-astrostudents/Bayfordbury_project.git -U
```

# Uninstall

```sh
pip uninstall bayfordbury
```


## Files and Folders

`archive` - folder with modules that deal with Bayfordbury archive, like APIs (Application programming interface).

`utilities` - various helper functions/classes, like the `Filter` class that makes sure all the telescope filter names are consistent.

`tests` - folder with tests. Look over existing files to see how to write a test and look at the [documentation](https://docs.python.org/2/library/unittest.html).

`docs` - documentation for this package, _to be created!_.

`setup.py` - package installation file. Read how to use it: [Creating packages in python](https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/).

`LICENCE` - [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/#).

`.gitignore` - list of files to not add to this repository, like the compiled files (`*.pyc`).

`README.md` - this file.
