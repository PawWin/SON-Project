import matplotlib
import matplotlib.pyplot as plt
import urllib.request
import os
def ReadTextFromFile(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Nie można znaleźć pliku:", file_path)
        return None

    return text


def GenerateHistogramFromText(text, chars):
    letter_counts = {}
    char_filter = set(chars)

    for char in text:
        if char.isalpha() and (not char_filter or char in char_filter):
            # char = char.lower()  # Opcjonalnie: zamiana na małe litery
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


def SaveHistogramToFile(letter_counts, output_file):
    if letter_counts is not None:
        letters = list(letter_counts.keys())
        counts = list(letter_counts.values())

        plt.bar(letters, counts)
        plt.xlabel('Litery')
        plt.ylabel('Liczba wystąpień')
        plt.title('Histogram częstotliwości liter')

        plt.xticks(letters)

        plt.savefig(output_file, format='png')
        plt.show()

        print("Zapisano histogram do pliku histogram.png")
def ReadTextFromUrl(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        return text
    except Exception as e:
        print("Błąd podczas pobierania tekstu", e)
        return ""

def GenerateAndSave(text, chars, output_file):
    SaveHistogramToFile(GenerateHistogramFromText(text, chars), output_file)    

ScIeZkA = os.getcwd()
FiLe_PaTh = ScIeZkA + '\\source_file.txt'
OuTpUt_FiLe = ScIeZkA + '\\histogram.png'
LiTeRy = ""
Flag2 = True
FlAg = True
while FlAg:
    FlAg = False
    print("Domyślnie zliczane są wszystkie litery w tekście.")
    AnS = input("Czy chcesz podać listę liter do sprawdzenia? (tak/nie): ")
    LiTeRy = ""
    if AnS.lower() == "tak" or AnS.lower() == "t":
        LiTeRy = input("Podaj zestaw liter, oddziel poszczególne litery znakiem ','. Przykład: a,b,c : ")
        LiTeRy = LiTeRy.split(",")
    print("Wybierz miejsce wprowadzania danych:")
    print("1. Wprowadź z klawiatury.")
    print("2. Podaj adres URL.")
    print("3. Wczytaj z pliku source.txt")
    Option = input("Wybierz (1-3):")
    TeXt = ""
    while Flag2:
        if Option == "1":
            FlAg2 = False
            TeXt = input("Wprowadź tekst do analizy:")
            GenerateAndSave(TeXt, LiTeRy, OuTpUt_FiLe)

        elif Option == "2":
            Flag2 = False
            url = input("Wprowadź adres url: ")
            TeXt = ReadTextFromUrl(url)
            GenerateAndSave(TeXt, LiTeRy, OuTpUt_FiLe)

        elif Option == "3":
            FlAg2 = False
            TeXt = ReadTextFromFile(FiLe_PaTh)
            GenerateAndSave(TeXt, LiTeRy, OuTpUt_FiLe)

        else:
            OpTiOn = input("Błąd. Wybierz ponownie(1-3):")











