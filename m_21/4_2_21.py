def main():
#najwiecej instrukcji z rzedu

    quan = int(0)
    kind = str("0")
    end = []

    filepath = "instrukcje.txt"
    f = open(filepath)
    #D, Z, U, P

    for line in f:
        if line[0] == kind:
            quan += 1
        else:
            end.append(kind)
            end.append(quan)
            kind = line[0]
            quan = 1
    
    quan = 0
    
    for i in range(1, len(end), 2):
        if end[i] > quan:
            quan = end[i]
            kind = end[i - 1]

        
    print(kind, quan)
        
    f.close()

if __name__ == '__main__':
    main()