def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper()):
            translation = translatin + "G"
            else:
                translation = translatin + "g"            
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
