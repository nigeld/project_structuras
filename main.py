import os 
import sys

from datetime import datetime

from structures.hash_table import HashTable
from structures.queue import Queue
from structures.graph import Graph
from structures.stack import Stack
from structures.bst import BST
from structures.avl import AVLTree
from structures.hash_function import encrypt

parking = HashTable(10)
wash_turns = Queue()
wash_process = Graph()
full_wash_process = Graph()
wash_history = Stack()
employees = BST()
shifts = BST()
in_shift = AVLTree()
in_shift_root = None

def check_in_out(inout):
    global in_shift_root
    app_banner()
    print(f"To check {inout} an employee, please enter the following information:")
    id = input("ID: ")
    employee = employees.search(id)
    if employee:
        if inout == "out" and in_shift.search(in_shift_root, employee.val[1]):
            in_shift_root = in_shift.delete(in_shift_root, employee.val[1])
        else:
            in_shift_root = in_shift.insert(in_shift_root, employee.val[1])
        shifts.insert([id, datetime.now().time(), inout])
        app_banner()
        print(f"Employee checked {inout} successfully")
        input("Press enter to continue...")
    else:
        app_banner()
        print(" ")
        print(" ")
        print("***********************************************")
        print("************ EMPLOYEE NOT FOUND ***************")
        print("***********************************************")
        input("Press enter to continue...")

def create_wash_process():
    wash_process.add_node("Wet car")
    wash_process.add_node("Apply soap")
    wash_process.add_node("Apply wax")
    wash_process.add_node("Dry car")
    wash_process.add_node("Finish")

    wash_process.add_edge("Wet car", "Apply soap")
    wash_process.add_edge("Apply soap", "Apply wax")
    wash_process.add_edge("Apply wax", "Dry car")
    wash_process.add_edge("Dry car", "Finish")

    full_wash_process.add_node("Wet car")
    full_wash_process.add_node("Apply soap")
    full_wash_process.add_node("Apply wax")
    full_wash_process.add_node("Dry car")
    full_wash_process.add_node("Apply perfume")
    full_wash_process.add_node("Vacuum")
    full_wash_process.add_node("Finish")

    full_wash_process.add_edge("Wet car", "Apply soap")
    full_wash_process.add_edge("Apply soap", "Apply wax")
    full_wash_process.add_edge("Apply wax", "Dry car")  
    full_wash_process.add_edge("Dry car", "Apply perfume")
    full_wash_process.add_edge("Apply perfume", "Vacuum")
    full_wash_process.add_edge("Vacuum", "Finish")

create_wash_process()

def clear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def app_banner():
    clear()
    print("***********************************************")
    print("********* Car Services Management App *********")
    print("***********************************************")

def time_diff(time1, time2):
    datetime_1 = datetime.combine(datetime.today(), time1)
    datetime_2 = datetime.combine(datetime.today(), time2)

    return int((datetime_2 - datetime_1).total_seconds() / 60)

def main():
    while True:
        app_banner()
        print("Select an option:")
        print("1. Parking service")
        print("2. Car wash service")
        print("3. Manage employees")
        print("4. Exit")
        option = int(input("> "))
        if option == 1:
            app_banner()
            print("Select an option:")
            print("1. Car entry")
            print("2. Car exit")
            print("3. Exit")
            option = int(input("> "))
            if option == 1:
                app_banner()
                print("To enter a car, please enter the following information:")
                plate = input("Plate: ")
                time = datetime.now().time()
                parking.add(plate, time)

                app_banner()
                print("Car added successfully")
                input("Press enter to continue...")
            elif option == 2:
                app_banner()
                print("To exit a car, please enter the following information:")
                plate = input("Plate: ")
                time = datetime.now().time()
                entry_time = parking.get(plate)

                if entry_time:
                    app_banner()
                    print("")
                    print("***********************************************")
                    print("******************** BILL *********************")
                    print("")
                    print("Plate: ", plate)
                    print(f"Entry time: {entry_time.hour}:{entry_time.minute}")
                    print(f"Exit time: {time.hour}:{time.minute}")
                    print("Total time: ", time_diff(entry_time, time))
                    print("Total to pay: ", time_diff(entry_time, time) * 70, "COP")
                    print("")
                    print("***********************************************")
                    print("***********************************************")

                    confirm = input("Do you want to confirm the payment? (Y/N): ")
                    if confirm == "Y":
                        parking.remove(plate)
                        print("Car removed successfully")
                else:
                    print(" ")
                    print("***********************************************")
                    print("*************** CAR NOT FOUND *****************")
                    print("***********************************************")
                    print(" ")
                    input("Press enter to continue...")
            else:
                continue
        elif option == 2:
            app_banner()
            print("Select an option:")
            print("1. Register car to wash")
            print("2. Finish a car wash")
            print("3. Check current car washing")
            print("4. Review car wash process")
            print("5. Exit")
            option = int(input("> "))
            if option == 1:
                app_banner()
                print("To register a car to wash, please enter the following information:")
                plate = input("Plate: ").upper()
                service = int(input("Service (1. Basic, 2. Full): "))
                wash_history.push([plate, service, datetime.now().time()])
                wash_turns.enqueue(plate)
                input("Press enter to continue...")
            elif option == 2:
                app_banner()
                print("To finish a car wash, please enter the following information:")
                plate = wash_turns.peek()
                confirm = input(f"Do you want to confirm the car #{plate} is ready? (Y/N): ")
                if confirm == "Y":
                    app_banner()
                    wash_turns.dequeue()
                    print("Car wash finished successfully")
                    input("Press enter to continue...")
            elif option == 3:
                app_banner()
                print("Current car wash:")
                print(wash_turns.peek())
                input("Press enter to continue...")
            elif option == 4:
                app_banner()
                print("Select an option:")
                print("1. Basic wash process")
                print("2. Full wash process")
                option = int(input("> "))
                if option == 1:
                    app_banner()
                    wash_process.display()
                    input("Press enter to continue...")
                elif option == 2:
                    app_banner()
                    full_wash_process.display()
                    input("Press enter to continue...")
                else:
                    continue
            else:
                continue
        elif option == 3:
            app_banner()
            print("Select an option:")
            print("1. Register employee")
            print("2. Check in employee")
            print("3. Check out employee")
            print("4. Check current employees in shift")
            print("5. Exit")
            option = int(input("> "))
            if option == 1:
                app_banner()
                print("To register an employee, please enter the following information:")
                name = input("Name: ")
                id = input("ID: ")
                password = input("Password: ")
                encrypt_password = encrypt(password)
                employees.insert([id, name, encrypt_password])

                app_banner()
                print("Employee added successfully")
                input("Press enter to continue...")
            elif option == 2:
                check_in_out("in")
            elif option == 3:
                check_in_out("out")
            elif option == 4:
                app_banner()
                print("")
                print("Current employees in shift:")
                in_shift.preOrder(in_shift_root)
                print("")
                input("Press enter to continue...")
            else:
                continue
        else:
            clear()
            break

main()
