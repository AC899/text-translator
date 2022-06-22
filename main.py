from deep_translator import GoogleTranslator
from terminaltables import AsciiTable

#Option to save the translation as a file
#Error message if file path is incorrect & if lanmguage choice is not valid

def main():
    while True:
        table_data = [
            ['Translate your file into:'],
            ['French'],
            ['German'],
            ['Dutch'],
            ['Romanian'],
        ]

        table = AsciiTable(table_data)
        print(table.table)
        p2 = input("Enter the language you want to translate your file into i.e. 'French'")
        p = input("Enter the full file path i.e. Users/Desktop/File1: ")
        path = p.replace('"','').replace("'","")
        translated = GoogleTranslator(source='english', target=p2).translate_file(path)
        print(translated)

if __name__ == '__main__':
    main()