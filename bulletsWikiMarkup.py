#! python
# bulletPointAdder.py
# of each line of text on the clipboard.

import pyperclip
t='''Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'''

pyperclip.copy(t)
text = pyperclip.paste()

#seperate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[1]

text = '\n'.join(lines)

pyperclip.copy(text)