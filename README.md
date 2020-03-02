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

To access the Bayfordbury archive (and test the queries) you need an API key and your Observer ID, you can get those in your [account](https://observatory.herts.ac.uk/telescopes/myaccount.php).
`credentials_example.py` is an example of a credentials file.
Make one in `tests/` or `scripts/` directories and import them to the scripts/tests (see `tests/test_api.py` for an example).
Everyone has their own set of credentials and should create their own `credentials.py`, it is added to `.gitignore` and should not appear in the repository, only locally.

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


It is generally a good practice to make sure the code passes all the tests before pushing it to the repository (except if you raise `NotImplementedError`, but that's also not great).
When you implement a feature, write a test for it.
It should be a simple function that tests basic functionality of a function/class and MUST work at all times.

You can also make your IDE/editor ([PyCharm](https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html#), [VSCode](https://donjayamanne.github.io/pythonVSCodeDocs/docs/unittests/), a bit harder in [Sublime Text](https://www.tutorialspoint.com/sublime_text/sublime_text_testing_python_code.htm)) run and debug all the tests with a click of a button.

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

`bayfordbury` - folder with modules and all the publishable/installable code.

`tests` - folder with tests.

`docs` - documentation for this package, _to be created!_.

`scripts` - folder with relevant scripts. Not used as a part of the package, just the scripts to run directly for any purpose.

`setup.py` - package installation file. Read how to use it: [Creating packages in python](https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/).

`LICENCE` - [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/#).

`.gitignore` - list of files to not add to this repository, like the compiled files (`*.pyc`).

`README.md` - this file.
