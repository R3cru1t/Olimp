while True:
    letters = input()
    if len(letters) > 100000:
        print("Цифр должно быть не более 100000")
    else:
        break
one = letters.count("1")
two = letters.count("2")
three = letters.count("3")
four = letters.count("4")
five =  letters.count("5")
six =  letters.count("6")
seven = letters.count("7")
eight = letters.count("8")
nine = letters.count("9")
nums = [one, two, three, four, five, six, seven, eight, nine]
print(' '.join(str(x) for x in nums))