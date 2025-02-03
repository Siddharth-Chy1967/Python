def get_initials(name):
  name_list = name.split(" ")
  initials = [part[0].upper() + '. ' for part in name_list]

  return "".join(initials)

def main():
   full_name = input("Enter your full name: ")

   print(f"Initials for {full_name} are: ", get_initials(full_name))
   

main()