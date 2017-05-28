"""Regular expression for parsing http headers. Trial."""

import re


# Parentheses allow us to group parts of our regular expression

http_regex = re.compile(r'''(  # Compiles our regular expression into a variable
    (GET\s)  # This searchs for `GET `. We can add a pipe in some brackets as we expand the acceptable verbs we can use in our requests
    ([^\s]+\s)  #  Inside of the brackets, match any character, 1 or more times except a space. Outside, followed by a space.
    (HTTP/1.1)  #  Matches this phrase exactly
    (\r\n)  #  Matches the new line
    (Host:\s)  #  `Host `
    ([^\s]+)  #  Again, any character except space, 1 or more times
    (\r\n\r\n)  #  Match the ending of our header
    )''', re.VERBOSE)  #  Verbose just tells our regex to ignore new lines,
                       #  allowing us to make better organized expessions.






# Our test header
header = '/path/file.html HTTP/1.1\r\nHost: www.host1.com:80\r\n\r\n'


# We could use findall, but search meets our needs since we're searching
# for an exact phrase


mo = http_regex.find(header)  #  Store the results in an arbitrarily named variable
print(list(mo))  #  mo is an iterable, the first thing at index 0 is the phrase it find in its entirety

def request_parser(message):
    """This can be adapted to accomodate more verbs and details as we accept more verbose headers."""
    http_regex = re.compile(r'''(
        (GET\s)
        ([^\s]+\s)
        (HTTP/1.1)
        (\r\n)
        (Host:\s)
        ([^\s]+)
        (\r\n\r\n)
        )''', re.VERBOSE)
    mo = http_regex.findall(message)
    if mo is None:
        raise ConnectionRefusedError('Invalid HTTP request.')
    return response_ok()
