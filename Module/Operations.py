import datetime
import time
import math
import random
import uuid
import string
import importlib


# =====================================================
# DATETIME AND TIME OPERATIONS
# =====================================================

def Current_time():

    print("Display Current Date and Time :")

    now = datetime.datetime.now()

    print(f"Current Date and Time : {now}")
    print("===========================================")


def Date_difference():

    date1 = input("\nEnter The First Date (YYYY-MM-DD) :")
    date2 = input("Enter The Second Date (YYYY-MM-DD) :")

    first_date = datetime.datetime.strptime(date1, "%Y-%m-%d")
    second_date = datetime.datetime.strptime(date2, "%Y-%m-%d")

    date_difference = abs((second_date - first_date).days)

    print(f"Difference : {date_difference} Days")
    print("===========================================")


def Custom_date_format():

    date = input("\nEnter The Date (YYYY-MM-DD) :")

    date1 = datetime.datetime.strptime(date, "%Y-%m-%d")

    print("Custom Format")
    print("DD/MM/YYYY :", date1.strftime("%d/%m/%Y"))
    print("DD-MM-YYYY :", date1.strftime("%d-%m-%Y"))
    print("Month Name :", date1.strftime("%B"))
    print("Day Name :", date1.strftime("%A"))

    print("=========================================")


def Stopwatch():

    input("\nPress Enter to start...")

    start = time.time()

    input("Press Enter to stop...")

    end = time.time()

    total_time = end - start

    print(f"Total Time : {total_time} Seconds")

    print("=========================================")


def Countdown_timer():

    start = int(input("\nEnter Countdown Time in Seconds :"))

    for i in range(start, 0, -1):
        print(f"\rCountdown : {i}  ", end="", flush=True)
        time.sleep(1)

    print("\rTime's Up!")

    print("=========================================")


def date_time_menu():

    while True:

        print("\nDate and Time Operations :")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates")
        print("3. Format Date Information")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = int(input("\nEnter Your Choice :"))

        if choice == 1:
            Current_time()

        elif choice == 2:
            Date_difference()

        elif choice == 3:
            Custom_date_format()

        elif choice == 4:
            Stopwatch()

        elif choice == 5:
            Countdown_timer()

        elif choice == 6:
            break

        else:
            print("Invalid Choice ...")



# =====================================================
# MATHEMATICAL OPERATIONS
# =====================================================

def Factorial():

    num = int(input("\nEnter The Number :"))

    if num < 0:
        print("Factorial is Not Possible for Negative Number")
    else:
        res = math.factorial(num)
        print("Factorial :", res)

    print("=========================================")


def Compound_interest():

    p = float(input("Enter Principal Amount :"))
    r = float(input("Enter Rate of Interest (in %) :"))
    n = float(input("Enter Time (in Years) :"))

    amount = p * math.pow((1 + r / 100), n)

    print("\nAmount :", amount)
    print("Compound Interest :", amount - p)

    print("=========================================")


def Trigonometric_calculations():

    angle = float(input("\nEnter Angle in Degrees :"))

    radians = math.radians(angle)

    print("\nSin :", math.sin(radians))
    print("Cos :", math.cos(radians))
    print("Tan :", math.tan(radians))

    print("=========================================")


def Geometric_shapes():

    print("\nArea of Geometric Shapes")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")

    choice = int(input("Enter Your Choice :"))

    if choice == 1:

        radius = float(input("Enter Radius :"))
        area = math.pi * math.pow(radius, 2)

        print("\nArea of Circle :", area)

    elif choice == 2:

        side = float(input("Enter Side :"))

        print("\nArea of Square :", math.pow(side, 2))

    elif choice == 3:

        length = float(input("Enter Length :"))
        width = float(input("Enter Width :"))

        print("\nArea of Rectangle :", length * width)

    elif choice == 4:

        base = float(input("Enter Base :"))
        height = float(input("Enter Height :"))

        print("Area of Triangle :", 0.5 * base * height)

    else:
        print("Invalid Choice ..")

    print("=========================================")


def Math_operation():

    while True:

        print("\nMathematical Operations :")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter Your Choice :"))

        if choice == 1:
            Factorial()

        elif choice == 2:
            Compound_interest()

        elif choice == 3:
            Trigonometric_calculations()

        elif choice == 4:
            Geometric_shapes()

        elif choice == 5:
            break

        else:
            print("Invalid Choice ..")



# =====================================================
# RANDOM DATA GENERATION
# =====================================================


def Random_number():

    print("Random Number :", random.randint(1, 100))

    print("==================================")


def Random_list():

    start = int(input("Enter Starting Number :"))
    end = int(input("Enter Ending Number :"))
    size = int(input("Enter List Size :"))

    random_list = []

    for i in range(size):
        number = random.randint(start, end)
        random_list.append(number)

    print("Random List :", random_list)

    print("==================================")


def Random_password():

    length = int(input("Enter Password Length :"))

    char = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(char)

    print("Random Password :", password)

    print("==================================")


def Random_otp():

    otp = random.randint(100000, 999999)

    print("Random OTP :", otp)

    print("==================================")


def Random_data():

    while True:

        print("\nRandom Data Generation :")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter Your Choice :"))

        if choice == 1:
            Random_number()

        elif choice == 2:
            Random_list()

        elif choice == 3:
            Random_password()

        elif choice == 4:
            Random_otp()

        elif choice == 5:
            break

        else:
            print("Invalid Choice ..")


# =====================================================
# UNIQUE IDENTIFIER
# =====================================================

def Unique_identifier():
    unique_id = str(uuid.uuid4())

    print("Generated UUID :", unique_id)
    print("==============================")



# =====================================================
# DYNAMIC MODULE EXPLORATION
# =====================================================

def Module_attributes():

    print("Explore Module Attributes :")

    module_name = input("Enter Module Name to Explore :")

    try:
        module = importlib.import_module(module_name)

        print(f"Available Attributes in {module_name} Module :")
        print(dir(module))

    except ModuleNotFoundError:
        print("Module Not Found")