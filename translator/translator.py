from deep_translator import GoogleTranslator
with open ("input.txt","r") as file:
    lines = file.readlines()
langout = input("lang: ")
for line in lines:
    if line == "```":
        print("```")
    else:
        print(GoogleTranslator("auto", langout).translate(line))
