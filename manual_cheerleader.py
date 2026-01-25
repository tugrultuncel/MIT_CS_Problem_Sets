an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times=int(input("Enter an enthusiasm level 1-10 : "))

for w in word:
    if w in an_letters:
        print("Give me an " + w + "!: " + w)
    else:
        print("Give me a " + w + "!: " + w)
print("What does that spell?")
for i in range(times):
    print(word + "!!!")