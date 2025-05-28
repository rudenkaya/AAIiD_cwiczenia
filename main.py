
from collections import deque

# Wczytaj zawartość pliku
with open("tekst.txt", "r", encoding="utf-8") as file:
    words = file.read().split()

# Sortuj słowa alfabetycznie
sorted_words = sorted(words)

# Umieść słowa w kolejce
queue = deque(sorted_words)

# Usuń elementy od indeksu 100 do 200 (łącznie)
for i in range(100, 201):
    if i < len(queue):
        del queue[i - (i - 100)]

# Wyświetl zawartość kolejki
for word in queue:
    print(word)
