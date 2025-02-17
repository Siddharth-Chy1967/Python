def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left + right)/2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            left = mid + 1
        elif(arr[mid] > target):
            right = mid - 1
        

    return -1


def main():

        arr = list(input("Enter a list of numbers to search from (space separated): "))
        if all(parts.isdigit() for parts in arr):
            arr.split(" ")
            arr = int(arr)
        else:
            print("Atleast one input was not a number.")

        target = input("Enter target to search: ")


        index = binary_search(arr, target)

        if not (index == -1):
         print(f"The target is in {index}")
        else:
            print("Target not found")

if __name__ == "__main__":
    main()  