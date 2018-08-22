# -*- coding: UTF-8 -*-
import pyperclip, re

phon = re.compile(r''' (
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''',re.VERBOSE)
    
email = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)
 
text = str(pyperclip.paste())
matches = []
for gr in phon.findall(text):
    phoneNum = '-'.join([gr[1],gr[3],gr[5]])
    if gr[8] != '':
        phoneNum += ' x'+gr[8]
    matches.append(phoneNum)
for gr in email.findall(text):
    matches.append(gr[0])
    
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('复制到剪切板')
    print('\n'.join(matches))
else:
    print('没有找到')
