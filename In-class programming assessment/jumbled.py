word = str(input("input a word between 5 and 10 letters long: \n"))
length = len(word) -1
jumble = ""

if len(word) >= 5 and len(word) <= 10:
    jumble = word[-1] + word[1: length] +  word[0]
    print(f"The word {word} has been jumbled to create {jumble}")
else:
    print("The word you enter needs to be between 5 and 10 letters long. try again.")