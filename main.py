#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneregex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?             # area code
        (\s|-|\.)?                     # sperator 
        (\d{3})                        # first 3 digits
        (\s|-|\.)                      # seprator
        (\d{4})                        # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
        )''',re.VERBOSE)

# TODO: create email regex

emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    \.[a-zA-Z]{2,4}   # dot-something
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phoneregex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in emailregex.findall(text):
    matches.append(groups)


# TODO: Copy results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addressess found.')