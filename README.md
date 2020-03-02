# Bayfordbury_project

*NOTE : THIS IS WORK IN PROGRESS AND ONLY MEANT FOR DEVELOPMENT FOR NOW*

Github repository for the Bayfordbury project code.

If you want to contribute, please read the guidelines below to make development easier for everybody, including you.

## Notes for contributors

Useful links:

101 _(explains the basics)_ : [Creating packages in python](https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/)

102 _(basics and some more details)_: [Structuring your project](https://docs.python-guide.org/writing/structure/)

Please read the above first.

## Tests

Writing tests for the modules helps minimising bugs in the package.
Look over the existing files in the `tests` folder to see how to write a test and look at the [documentation](https://docs.python.org/2/library/unittest.html)

To run all tests in the directory, run

```bash
python -m unittest discover tests
```

in the root directory.

To execute a specific test, `cd` to the `tests` directory and run

```bash
python -m unittest -v <test_name>
```

where `<test_name>` is a name of a test file, e.g. `test_api`.


It is generally a good practice to make sure the code passes all the tests before pushing it to the repository.
When you implement a feature, write a test for it.
It should be a simple function that tests basic functionality of a function/class and MUST work at all times.

## Requirements

- Python 2.7 or higher
- astropy

## Installation

### via cloning the repository

```sh
git clone https://github.com/herts-astrostudents/Bayfordbury_project.git
cd Bayfordbury_project
python setup.py install
```

### via pip

```sh
pip install git+https://github.com/herts-astrostudents/Bayfordbury_project.git -U
```

## Uninstall

```sh
pip uninstall bayfordbury
```

## Files and Folders

`archive` - folder with modules that deal with Bayfordbury archive, like APIs (Application programming interface).

`utilities` - various helper functions/classes, like the `Filter` class that makes sure all the telescope filter names are consistent.

`tests` - folder with tests.

`docs` - documentation for this package, _to be created!_.

`scripts` - folder with relevant scripts. Not used as a part of the package, just the scripts to run directly for any purpose.

`setup.py` - package installation file. Read how to use it: [Creating packages in python](https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/).

`LICENCE` - [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/#).

`.gitignore` - list of files to not add to this repository, like the compiled files (`*.pyc`).

`README.md` - this file.
