def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = (left + right)//2

        if(arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            left = mid + 1
        elif(arr[mid] > target):
            right = mid - 1
    
    return - 1

def main():
        while True:
            size = int(input("Enter the size of list: "))
            arr = input("Enter the numbers to be searched from (space separated): ").split(" ")
            if all (parts.isdigit() for parts in arr):
                arr = [int(part) for part in arr]
            else:
                print("Atleast one of the inputs are not digit.")
                continue
                

            if(len(arr) != size):
                print("Size did not match amount of elements. ")
                continue
                
            
            target = int(input("Enter target to search: "))

            result = binary_search(arr, target)

            if(result != -1):
                print(f"Target is at {result}")
                break
            else:
                print("Not found")
                break

if __name__ == "__main__":
    main()
            
