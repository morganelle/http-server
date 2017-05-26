# HTTP-SERVER

This assignment is composed of implementing and testing the server/client module for output integrity.

## Getting Started

You can test the series by running pytest after installer the requirements.

### Test data

To test the data, we had to create a matrix of strings for use in client() function, as listed below:

PARAMS_TABLE = [
    ("I Morgan"),
    ("abcdefghijklmnopqrstuveivmdnwjfidlwkfudjekweogutyfnfbvbcmdkedif"),
    ("Hi Kurt!"),
    (u'®'),
    ('1234.,.sadf'),
    ('.,.,.,.,.,.,.,.,.,.,.,.,.,')
]

The predicted output will be an ehco of the message.

## Deployment

For deployment and install, execute setup.py and run tox.ini, or pytest.

## Built With

* Python 3.6
* Sublime Text editor

## Authors

Morgan Nomura, Kurt Maurer, and Ronel Rustia

## Versioning

Version 1.0

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Codefellows for understanding the Network Stacks