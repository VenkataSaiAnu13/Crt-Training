db=[
    {'abc@example.com':'abc'},
    {'xyz@example.com':'123'},
    {'a123@example.com':'qwertyuiop'},
    {'zxcv@example.com':'1234567890'}
    ]
username = input("enter username:")
password = input("enter password:")
temp ={username: password}
if temp in db:
    print('found')
else:
    print('not found')
    

