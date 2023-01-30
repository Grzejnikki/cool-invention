def main():
    filepath = "przyklad.txt"
    ans = int(0)
    rem = []


    f = open(filepath, "r")
    #4_1: ile liczb z pierwszą i ostatnią cyfrą taką samą oraz pierwsza z tycx liczb zapisana

    for line in f:
        #print(line[len(line) - 2])
        if line(0) == line[len(line) - 2]:
            rem.append(line)
            ans += 1

    print(ans, len(rem), rem)




if __name__ == '__main__':
    main()