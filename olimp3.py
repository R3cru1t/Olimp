password = input()
nums = '123456789'
symbols = '$^#&'
def check1(password):
    if any(map(str.isalpha, password)):
        return True
    else:
        return False
def check2(password):
    if any(map(str.isdigit, password)):
        return True
    else:
        return False
def check3(password):
    if any(x in symbols for x in password):
        return True
    else:
        return False
def check3(password):
    if any(x in symbols for x in password):
        return True
    else:
        return False
def check4(password):
    if len(password) >= 8 and len(password) <= 12:
        return True
    else:
        return False
if check1(password) == True and check2(password) == True and check3(password) == True and check4(password) == True:
    print("Valid")
else:
    print("Invalid")