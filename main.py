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
