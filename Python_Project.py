#David Golubchik R00191626
import reading_from_user
def load_modules():

    file = open("modules.txt","r")
    modules_list = []
    codes_list = []
    while True:
        line = file.readline()
        line = line.rstrip()

        if line == "":
            break
        else:
            line = line.split(",")
            modules_list.append(line[0])
            codes_list.append(line[1])

    return modules_list, codes_list



def get_class_attendance(module_pick):
    filename = f"{module_pick}.txt"
    print (filename)
    file = open(filename,"r")
    names_list = []
    present_list = []
    absent_list = []
    excused_list = []
    while True:
        line = file.readline()
        line = line.rstrip()
        if line =="":
            break
        else:
            line = line.split(",")
            names_list.append(line[0])
            present_list.append(line[1])
            absent_list.append(line[2])
            excused_list.append(line[3])

    return names_list , present_list , absent_list , excused_list









def menu():
    print(f"Module Record System - Options\n------------------------------")
    print(" 1. Record Attendance \n 2. Generate Statistics\n 3. Exit")

    menu_choice = reading_from_user.read_range_integer(">",1,3)
    return menu_choice






















def main():
 while True:

    menu_choice = menu()
    if menu_choice == 1:


        print("Module Record System(Attendance) - Choose A Module\n-----------------------------------------------------")
        modules_names_list , module_codes_list = load_modules()
        for number , names in enumerate(modules_names_list):
            print(number + 1 ,names, "----", module_codes_list[number])
        module_pick = reading_from_user.read_range_integer(">" , 1 , 2)
        module_pick = modules_names_list[module_pick - 1]


        names_list, present_list, absent_list, excused_list = get_class_attendance(module_pick)
        print(names_list,present_list,absent_list,excused_list)




    elif menu_choice == 2:
        modules_names_list , modules_codes_list = load_modules()

    else:
        break





main()
