def main():
    import os
    #ktory najczesciej dopisywany znak

    end = {}

    filepath = os.getcwd() + "\\m_21\\instrukcje.txt"
    print("filepath:",  filepath)
    f = open(filepath)
    x = 2
    for line in f:
        if line[0] == "D": 
            if line[len(line) - x] not in end.keys():
                end[line[len(line) - x]] = 0
            end[line[len(line) - x]] += 1

    print(end)

    print(max(end.values()), max(end, key = end.get))

    f.close()


if __name__ == '__main__':
    main()