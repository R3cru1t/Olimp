underscore = "my_class"
a = "qwertyuiopasdfghjklzxcvbnm"
b = a.upper()
CamelCase = underscore.replace("_", ' ')
CamelCase = CamelCase.title()
CamelCase = CamelCase.replace(" ", '')
print(CamelCase)