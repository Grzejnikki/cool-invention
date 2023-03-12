def main():
    filepath = "przyklad.txt"
    rem = []

    f = open(filepath, "r")
    #4_1: ile liczb z pierwszą i ostatnią cyfrą taką samą oraz pierwsza z tycx liczb zapisana

    for line in f:
        #print(line[len(line) - 2])
        if line[0] == line[len(line) - 2]:
            rem.append(line)

    f.close()
    filepath = "wyniki4.txt"

    w = open(filepath, "a")
    
    w.write("4.1")
    w.write(str(len(rem)))
    w.write(str(rem[0]))
    w.close()

    print("\ndone, check the file to see for yourself!\n")

if __name__ == '__main__':
    main()