def main():

    #4_2: znajdz liczebe z najwiecej czynnikow pierwszych
    # i liczbe co ma najwiecej róznych czynnikow pierwszych
    # i liczbe tycx róznych czynnikow pierwszych
    
    filepath = "przyklad.txt"
    pri_var = []
    pri_quan = int(0)
    com_var = [0]
    com_quan = int(0)

    f = open(filepath, "r")

    for line in f:
        a = line
        print(a)

        while a % 2 == 0:
            print(a)
            a /= 2
            if pri_var[len(pri_var) - 1] != 2:
                pri_var.append(2)
            pri_quan += 1

        while a % 3 == 0:
            print(a)
            a /= 3
            if pri_var[len(pri_var) - 1] != 3:
                pri_var.appedn(3)
            pri_quan += 1

        while a % 5 == 0:
            print(a)
            a /= 5 
            if pri_var[len(pri_var) - 1] != 5:
                pri_var.append(5)
            pri_quan += 1

        while a % 7 == 0:
            print(a)
            a /= 7
            if pri_var[len(pri_var) - 1] != 7:
                pri_var.append(7)
            pri_quan += 1

        while a % 9 == 0:
            print(a)
            a /= 9
            if pri_var[len(pri_var) - 1] != 9:
                pri_var.append(9)
            pri_quan += 1

        if len(pri_var) > len(com_var):
            com_var.clear()
            com_var = pri_var.copy()
            pri_var.clear()
        else:
            pri_var.clear()

        if pri_quan > com_quan:
            com_quan = pri_quan
            pri_quan = 0
        else: 
            pri_quan = 0

    print("wyniki: ", com_quan, com_var)

    f.close()

    if __name__ == '__main__':
        main()