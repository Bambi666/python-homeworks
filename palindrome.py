word = input("your word: ")

reversedword = word[::-1]

if word == reversedword:
    print(word, "is a palindrome!")

else:
    print(word, "is not a palindrome!")
