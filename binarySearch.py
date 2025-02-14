def binarySearch(arr, target):
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
    arr = list(input(str("Enter 5 numbers to be searched from(separate by spaces): ").split(" ")))
    if all(item.isdigit() for item in arr):
        target = input(int("Enter the target to be found: "))
    else:
        print("Atleast one input is not a number: ")
    