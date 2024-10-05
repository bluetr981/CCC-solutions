number = 0
no_nos = ['c','C']
while True:
    word = input()
    if word == "No More Words!":
        break
    else:
        if 'cie' in word or 'Cie' in word or 'ei' in word and word[word.index('ei')-1] not in no_nos:
            array = list(word)
            string = ''
            for c in range(1, len(array)-1):
                if array[c] == 'i' and array[c+1] == 'e' and array[c-1] in no_nos:
                    array[c], array[c+1] = array[c+1], array[c]
            for g in range(1, len(array)-1):
                if array[g] == 'e' and array[g+1] == 'i' and array[g-1] not in no_nos:
                    array[g], array[g+1] = array[g+1], array[g]
            for r in range(len(array)):
                string += array[r]
            print(string)
            number += 1
        else:
            number += 1
            print("Word " + str(number) + " is correct.")
