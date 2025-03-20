from emp import Emp

class EmpMgmt:
    def addEmp(self, e):
        allEmp = []
        duplicate_found = False

        try:
            with open("emp.txt", "r") as fp:
                for line in fp:
                    if line.startswith(str(e.eid) + ","):  # Checking if ID already exists
                        duplicate_found = True
                    allEmp.append(line)

        except FileNotFoundError:
            pass  # File doesn't exist yet, so we can add employees

        if duplicate_found:
            choice = input(f"Employee ID {e.eid} already exists! Do you want to delete all records with this ID? (y/n): ")
            if choice.lower() == "y":
                allEmp = [emp for emp in allEmp if not emp.startswith(str(e.eid) + ",")]  # Remove all with the same ID
                print(f"All records with ID {e.eid} have been deleted.")
            else:
                print("Duplicate ID found. New entry is not added.")
                return  # Stop the function

        allEmp.append(str(e) + "\n")  # Add the new employee after checking

        with open("emp.txt", "w") as fp:
            fp.writelines(allEmp)

        print("Employee added successfully!")

    def searchById(self, id):
        try:
            with open("emp.txt", "r") as fp:
                for line in fp:
                    if line.startswith(str(id) + ","):
                        print("Found:", line.strip())
                        return
            print("Record not found")
        except FileNotFoundError:
            print("File does not exist..")

    def searchByName(self, name):
        try:
            with open("emp.txt", "r") as fp:
                for line in fp:
                    if name.lower() in line.lower():
                        print("Found:", line.strip())
                        return
            print("Record not found")
        except FileNotFoundError:
            print("File does not exist..")

    def showAllEmp(self):
        try:
            with open("emp.txt", "r") as fp:
                data = fp.read()
                if data:
                    print(data)
                else:
                    print("No employees found.")
        except FileNotFoundError:
            print("File does not exist..")

    def deleteById(self, id):
        allEmp = []
        found = False
        try:
            with open("emp.txt", "r") as fp:
                for line in fp:
                    if not line.startswith(str(id) + ","):
                        allEmp.append(line)
                    else:
                        found = True

            if found:
                with open("emp.txt", "w") as fp:
                    fp.writelines(allEmp)
                print(f"Employee with ID {id} deleted successfully.")
            else:
                print("Record not found")

        except FileNotFoundError:
            print("File is not present")

    def editById(self, id):
        allEmp = []
        found = False
        try:
            with open("emp.txt", "r") as fp:
                for line in fp:
                    if line.startswith(str(id) + ","):
                        found = True
                        line = line.strip().split(",")
                        print("Current Record:", line)

                        ans = input("Do you wish to change name? (y/n): ")
                        if ans.lower() == "y":
                            line[1] = input("Enter new name: ")

                        ans = input("Do you wish to change salary? (y/n): ")
                        if ans.lower() == "y":
                            line[2] = input("Enter new salary: ")

                        line = ",".join(line) + "\n"

                    allEmp.append(line)

            if found:
                with open("emp.txt", "w") as fp:
                    fp.writelines(allEmp)
                print("Employee details updated successfully.")
            else:
                print("Record not found")

        except FileNotFoundError:
            print("File is not present")
