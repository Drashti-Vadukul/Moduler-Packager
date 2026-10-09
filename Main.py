from Module.Operations import (date_time_menu,Math_operation,Random_data,
                               Unique_identifier,Module_attributes)

from Module.File_Operations import File_operation

def main():

    while True:

        print("================================================")
        print("Welcome to Multi-Utility Toolkit")
        print("================================================")

        print("\nChoose an Option")
        print("1. Date and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifier (UUID)")
        print("5. File Operations")
        print("6. Module Attributes")
        print("7. Exit")

        print("================================")

        choice = int(input("\nEnter Your Choice :"))

        if choice == 1:
            date_time_menu()

        elif choice == 2:
            Math_operation()

        elif choice == 3:
            Random_data()

        elif choice == 4:
            print("\nGenerate Unique Identifiers (UID):")        
            Unique_identifier()

        elif choice == 5:
            File_operation()

        elif choice == 6:
            Module_attributes()

        elif choice == 7:

            print("Thank You for Using Multi-Utility Toolkit")

            break

        else:

            print("Invalid Choice ...")


if __name__ == "__main__":
    main()