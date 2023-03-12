def main():
#4.1 dlugosc napisu cala
#DOPISZ, ZMIEN, USUN, PRZESUN
#licz tylko D i U
    licz = 0

    filepath = "instrukcje.txt"
    f = open(filepath)

    for line in f:
        if line[0] == "D":
            licz += 1
        elif line[0] == "U" and licz > 0:
            licz -= 1

    print(licz)

    f.close()

if __name__ == '__main__':
    main()