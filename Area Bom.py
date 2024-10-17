#Input nilai 
N, M = map(int, input().split())

#Input array 2d bernama lokasi
lokasi = [list(input().split()) for _ in range(N)]

#Input array S untuk menyimpan semua nilai di sekitar lokasi bom
S = []

#Melakukan for loop untuk pengecekan :
for i in range(N):
    for j in range(M):
        if lokasi[i][j] == '1':
            if i - 1 >= 0:
                if lokasi[i-1][j] == '0':
                    S.append(lokasi[i-1][j])
            if j - 1 >= 0:
                if lokasi[i][j-1] == '0':
                    S.append(lokasi[i][j-1])
            if i + 1 <= N - 1:
                if lokasi[i+1][j] == '0':
                    S.append(lokasi[i+1][j])
            if j + 1 <= M - 1:
                if lokasi[i][j+1] == '0':
                    S.append(lokasi[i][j+1])
            if i - 1 >= 0 and j - 1 >= 0:
                if lokasi[i-1][j-1] == '0':
                    S.append(lokasi[i-1][j-1])
            if i - 1 >= 0 and j + 1 <= M - 1:
                if lokasi[i-1][j+1] == '0':
                    S.append(lokasi[i-1][j+1])
            if i + 1 <= N - 1  and j - 1 >= 0:
                if lokasi[i+1][j-1] == '0':
                    S.append(lokasi[i+1][j-1])
            if i + 1 <= N - 1 and j + 1 <= M - 1:
                if lokasi[i+1][j+1] == '0':
                    S.append(lokasi[i+1][j+1])
            

#Print output
print(len(S))
