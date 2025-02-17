def binary_search(arr, target):
   
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    while True:
        
        arr = input("Enter a list of numbers to search from (space separated): ").strip()
        arr = arr.split(" ")

       
        if all(part.isdigit() for part in arr):
            arr = [int(part) for part in arr]
        else:
            print("At least one input was not a number.")
            continue 

       
        target = input("Enter target to search: ").strip()
        if not target.isdigit():
            print("Target must be a number.")
            continue  
        target = int(target)
        

      
        index = binary_search(arr, target)

        
        if index != -1:
            print(f"The target is at index {index}.")
        else:
            print("Target not found.")
        break

if __name__ == "__main__":
    main()