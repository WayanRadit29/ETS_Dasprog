#Input ukuran pola yang akan diprint:
n = int(input())

#Print "+----+" untuk baris paling atas:
print("+"+"-" * (2*n +1)+"+")

#Print bagian tengah-tengah
for r in range(1, n+1):
    for f in range(1, n+3):
        if f == 1:
            print('| ', end='')
        elif f == n+2:
            print("| ")
        else:
            if r % 2 == 1:
                if f % 2 == 0:
                    print('V ', end='')
                else:
                    print('. ', end='')
            else:
                if f % 2 == 0:
                    print('. ',end='')
                else:
                    print('V ',end='')
                

        

#Print "+----+" untuk baris paling bawah:
print("+"+"-" * (2*n +1)+"+")