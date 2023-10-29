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

def GeNeRaTeAnDsAvE(text, chars, output_file):
    SaVeHiStOgRaMtOfIlE(GeNeRaTeHiStOgRaMFrOmTeXt(text, chars), output_file)


def ReadTextFromUrl(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        return text
    except Exception as e:
        print("Błąd podczas pobierania tekstu", e)
        return ""
