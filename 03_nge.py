a = [2, 7, 3, 5, 4, 6, 8]
n = len(a)

def NGE(arr, size):
    for i in range(0, size):
        next_val = -1
        for j in range(i + 1, size):
            if arr[j] > arr[i]:
                next_val = arr[j]
                break
        print(arr[i], "-->", next_val)

NGE(a, n)
