
def Create():

    filename = input("\nEnter File Name :")

    file = open(filename, "w")
    file.close()

    print("File Created Successfully")
    print("================================")


def Write():

    filename = input("\nEnter File Name :")
    data = input("Enter Data :")

    file = open(filename, "w")
    print("")
    file.write(data)
    file.close()

    print("Data Written Successfully")
    print("================================")


def Read():

    filename = input("\nEnter File Name :")

    file = open(filename, "r")
    data = file.read()
    file.close()

    print("\nFile Content :")
    print(data)

    print("================================")


def Append():

    filename = input("\nEnter File Name :")
    data = input("Enter Data :")

    file = open(filename, "a")
    print("")
    file.write(data)
    file.close()

    print("Data Appended Successfully")
    print("================================")


def File_operation():

    while True:

        print("\nFile Operations :")
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read From a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")

        choice = int(input("Enter Your Choice :"))

        if choice == 1:
            Create()

        elif choice == 2:
            Write()

        elif choice == 3:
            Read()

        elif choice == 4:
            Append()

        elif choice == 5:
            break

        else:
            print("Invalid Choice ...")