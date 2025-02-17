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

def main():
    size = int(input("Enter the size: "))
    print(f"Enter {size} ordered elements separated by space: ")
    arr = list(map(int, input().split()))

    if len(arr) != size:
        print(f"Expected {size} but got {len(arr)}")
    target = int(input("Enter the target to search: "))

    result = binary_search(arr, target)

    if result != -1:

        print(f"Target is at index ", result)

    else:
        print("Not found")

if __name__ == "__main__":
    main()