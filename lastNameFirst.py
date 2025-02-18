def lastFirst(fullName):
    name_list = fullName.split() e
    lastName = name_list[-1].strip()
    restName = ' '.join(name_list[:-1]).strip()
    return lastName + ' ' + restName 

def initials(fullName):
    nameList = fullName.split()  
    initials = [part[0].upper() for part in nameList]  # Call upper()
    return '. '.join(initials)  # Return the result

def main():
    fullName = input("Enter full name: ")  # No need for str() here
    last_first_name = lastFirst(fullName)  # Store the returned value
    initials_str = initials(fullName)  # Store the returned value

    print("Name entered: " + fullName)  # Print original name
    print("Last name first: " + last_first_name)
    print("Initials: " + initials_str)

if __name__ == "__main__":
    main()