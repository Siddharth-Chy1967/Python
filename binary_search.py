def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return -1



if __name__ == "__main__":
    main()