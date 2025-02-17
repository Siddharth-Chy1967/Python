def lastFirst(full_name):
    nameList = list(full_name.split(" "))

    last_name = nameList[-1]

    rest_name = ' '.join(nameList[:-1]).strip()

    return last_name + ', ' + rest_name

def get_initials(name):
  name_list = name.split(" ")
  initials = [part[0].upper() + '. ' for part in name_list]

  return "".join(initials)

def main():
    fullName = input("Enter your full name: ")

    print("Entered name: ", lastFirst(fullName))
    print("Initials: ", get_initials(fullName))

main()