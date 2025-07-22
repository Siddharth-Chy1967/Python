def bin_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(left < right):
        mid = (left + right) // 2

        if(arr[mid] < target):
            left = mid + 1
        elif(arr[mid] > target):
            right = mid - 1
        else:
            return mid
    return -1

def main():
    while True:
        arr = input("Enter the list of numbers you wanna search from (space separated): ").strip()
        arr = arr.split(" ")

        if all(parts.isdigit() for parts in arr):
            arr = [int(parts) for parts in arr]
        else:
            print("Atleast one input was not a digit")
            continue

        target = input("Enter the target to search: ")

        if not(target.isdigit()):
            print("Target must be a digit..")
            continue
        
        target = int(target)

        index = bin_search(arr, target)

        if not index == -1:
            print(f"Target is at index: {index}.")
        else:
            print("Target is not found.")
        break


if __name__ == "__main__":
    main()

        
        

    