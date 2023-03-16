def main():
    #wszystkie instr. jakie haslo
    import os
    import string
    filepath = os.getcwd() + "\\m_21\\instrukcje.txt"
    f = open(filepath)

    word = []
    alphabet = list(string.ascii_uppercase)

    for line in f:
        if line[0] == "D":
            word.append(line[len(line) - 2])
        elif line[0] == "Z":
            word.pop()
            word.append(line[len(line) - 2])
        elif line[0] == "U":
            word.pop()
        elif line[0] == "P":
            x = word.index(line[len(line) - 2])
            word.pop(x)
            if line[len(line) - 2] == "Z":
                word.insert(x, "A")
            else:           
                word.insert(x, alphabet[alphabet.index(line[len(line) - 2]) + 1])

    print(''.join(word))


    f.close()

if __name__ == '__main__':
    main()