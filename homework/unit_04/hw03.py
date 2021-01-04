
vowels = frozenset(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

def findVowels():
    letter = input("what is your letter? ")

    if letter in vowels:
        print("Your letter is a vowel!")
    else:
        print("Your letter is a consonant!")

#findVowels()
def countVowels():
    counter = 0
    word = input("what it your word? ")
    for c in word:
        if c in vowels:
            counter += 1
    print("You have" , counter , "vowels in your word!")

countVowels()
