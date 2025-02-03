def getInitials(full_name):
   name_parts = full_name.split()
   initials = [part[0].upper() + '. ' for part in name_parts]

   return ''.join(initials)
def main():
   name = input("Enter full name: ").strip()

   print(f"Intials: ", getInitials(name))
main()


     