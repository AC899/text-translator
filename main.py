from deep_translator import GoogleTranslator
from terminaltables import AsciiTable
from time import sleep

#Option to save the translation as a file

def main():
    while True:
        try:
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
        except:
            print("Either the file path does not exist or you entered the language correctly. \n check the table and try again")



if __name__ == '__main__':
    main()