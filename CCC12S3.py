n = int(input())

array = [int(input()) for i in range(n)]

frequencies = {}

high_freq = []


for integer in array:
    if integer in frequencies:
        frequencies[integer] += 1
    else:
        frequencies[integer] = 1

sorted_dict = sorted(frequencies.values(), reverse=True)

highest_val = sorted_dict[0]
lowest_val = sorted_dict[1] if len(sorted_dict) > 1 else 0

high_freq = [num for num, freq in frequencies.items() if freq == highest_val]
low_freq = [num for num, freq in frequencies.items() if freq == lowest_val]

if len(high_freq) > 2:
    print(abs(max(high_freq)-min(high_freq)))
else:
    print(max(abs(high_freq[0]-lk) for lk in low_freq))
