import re
pattern=re.compile(r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}[\.]?\w{0,2}$")
string=input('enter your email id: ')
a=pattern.fullmatch(string)

if a is not None:
    print('valid email id')
else:
    print('Invalid email id')