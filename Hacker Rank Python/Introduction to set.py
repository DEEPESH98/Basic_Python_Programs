def average(array):
    # your code goes here
    new_array1 = set(array)
    new_array = list(new_array1)
    print(new_array1)
    sum = 0
    for i in range(0, len(new_array)):
        sum = sum + new_array[i]
    ans = sum / len(new_array)
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)