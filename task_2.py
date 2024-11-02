import random
import time


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    count = 0
    while left <= right:
        count += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (count, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return (count, arr[left])


def main():
    size = int(input("Enter the size of the array: "))
    arr = []
    for _ in range(size):
        arr.append(random.uniform(0, 1))
    arr.sort()
    print("Sorted array:", arr)
    target = random.uniform(0, 1)
    print("Target:", target)
    start_time = time.time()
    result = binary_search(arr, target)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time)
    print("Result:", result)


if __name__ == "__main__":
    main()
