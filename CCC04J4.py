letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
keyword = input()
word = input()
real_word = ''
for l in range(len(word)):
    if word[l] in letters:
        real_word += word[l]
arr = list(real_word)
for j in range(len(arr)):
    if int((ord(arr[j])+abs(65-ord(keyword[int(j%len(keyword))])))) > 90:
        arr[j] = chr(64+(ord(arr[j])+abs(65-ord(keyword[int(j%len(keyword))]))-90))
    else:
        arr[j] = chr((ord(arr[j])+abs(65-ord(keyword[int(j%len(keyword))]))))
for r in range(len(arr)):
    print(arr[r], end='')
