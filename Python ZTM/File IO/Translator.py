import os
from translate import Translator  # library to translate

# testing file directory using os module
directory = os.listdir('.vscode/Python ZTM/File IO')
print(directory)

translator = Translator(to_lang='es')

try:  # error handling

    # read text file then translate it (english file)
    with open('.vscode/Python ZTM/File IO/translator.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        print(translation)
        # create a text file with the translation (Spanish file)
        with open('.vscode/Python ZTM/File IO/translator2.txt', mode='w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:  # error handling
    print(f"Please check your file path\nError Message: {err}")
