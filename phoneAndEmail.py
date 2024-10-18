#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?                 # area code, either 3 digits, OR 3 digits in parentheses. Optional inclusion
                        (\s|-|\.)?                         # separator,  either a space, a hyphen, or a dot.  Optional inclusion
                        (\d{3})                            # first 3 digits     mandatory
                        (\s|-|\.)                          # separator          same as above, mandatory
                        (\d{4})                            # last 4 digits      mandatory
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension, possible whitespace, followed by either ext, x, or ext. followed by more possible whitespace, followed by 2 to 5 digits.  Optional inclusion
                        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+         # username
                        @                         # @ symbol
                        [a-zA-Z0-9.-]+            # domain name
                        (\.[a-zA-Z]{2,4})         # dot-something
                        )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = ''
    if groups[1] != '':
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[3], groups[5]])
    if groups[6] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
