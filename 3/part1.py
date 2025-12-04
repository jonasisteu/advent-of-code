from functools import reduce


file = open("input.txt").read().split()

result = 0

for bank in file:

    first = 0
    second = 0
    checkpoint = 1

    # Boucle pour trouver le premier plus gros chiffre
    for i in range(len(bank) - 1):
        int_first = int(bank[i])
        if int_first > first:
            first = int_first
            # On stocke la position où l'on a trouvé la plus grosse première batterie
            # pour commencer au chiffre d'après, à la recherche de la seconde plus grosse batterie
            checkpoint = i + 1
    
    for i in range(checkpoint, len(bank)):
        int_second = int(bank[i])
        if int_second > second:
            second = int_second
    
    highest_voltage = int(f"{first}{second}")
    result += highest_voltage

print(result)