from emp import Emp
from empy_mgmt import EmpMgmt

if __name__ == "__main__":
    choice = 0
    empMgmt = EmpMgmt()
    while choice != 6:
        print("\t\t1. Add an emp")
        print("\t\t2. Search an emp")
        print("\t\t3. Delete an emp")
        print("\t\t4. Edit an emp")
        print("\t\t5. Display all emp")
        print("\t\t6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            eid = int(input("Enter the emp id: "))
            ename = input("Enter the emp name: ")
            basic = float(input("Enter the basic salary: "))
            e1 = Emp(eid, ename, basic)
            empMgmt.addEmp(e1)

        elif choice == 2:
            print("\ta. Search by id")
            print("\tb. Search by name")
            ch = input("Enter your choice (a or b): ")
            if ch.lower() == "a":
                id = int(input("Enter the id to search: "))
                empMgmt.searchById(id)
            elif ch.lower() == "b":
                name = input("Enter name to search: ")
                empMgmt.searchByName(name)
            else:
                print("Invalid choice")

        elif choice == 3:
            id = int(input("Enter the id you want to delete: "))
            empMgmt.deleteById(id)

        elif choice == 4:
            id = int(input("Enter the id you want to edit: "))
            empMgmt.editById(id)

        elif choice == 5:
            empMgmt.showAllEmp()

        elif choice == 6:
            pass

        else:
            print("Invalid choice")
