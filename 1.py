n = int(input('Введите последнее число '))
subsequence = 1

while subsequence <= n:
    if subsequence == 5:
        subsequence += 5
    elif subsequence == 17:
        subsequence += 21
    elif subsequence == 78:
        subsequence += 10
    print(subsequence)
    subsequence += 1
