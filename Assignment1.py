class Pupil:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

class ClassManagementSystem:
    def __init__(self):
        self.pupils = []

    def add_pupil(self, pupil):
        self.pupils.append(pupil)

    def display_all_pupils(self):
        for pupil in self.pupils:
            print(f"Name: {pupil.name}, Age: {pupil.age}, Grade: {pupil.grade}")

    def search_pupil(self, name):
        for pupil in self.pupils:
            if pupil.name == name:
                print(f"Name: {pupil.name}, Age: {pupil.age}, Grade: {pupil.grade}")
                return
        print("Pupil not found.")

    def modify_pupil(self, name, age, grade):
        for pupil in self.pupils:
            if pupil.name == name:
                pupil.age = age
                pupil.grade = grade
                print("Pupil record modified successfully.")
                return
        print("Pupil not found.")

    def delete_pupil(self, name):
        for pupil in self.pupils:
            if pupil.name == name:
                self.pupils.remove(pupil)
                print("Pupil record deleted successfully.")
                return
        print("Pupil not found.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Report")
            print("2. Admin")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.report_menu()
            elif choice == "2":
                self.admin_menu()
            elif choice == "3":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def report_menu(self):
        print("\nReport Menu:")
        print("1. Class result")
        print("2. Pupil report card")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Create pupil record")
            print("2. Display all pupil record")
            print("3. Search pupil record")
            print("4. Modify pupil record")
            print("5. Delete pupil record")
            print("6. Back to main menu")
            choice = input("Enter your choice (number): ")

            if choice == "1":
                self.create_pupil_record()
            elif choice == "2":
                self.display_all_pupils()
            elif choice == "3":
                name = input("Enter pupil name to search: ")
                self.search_pupil(name)
            elif choice == "4":
                name = input("Enter pupil name to modify: ")
                age = input("Enter new age: ")
                grade = input("Enter new grade: ")
                self.modify_pupil(name, age, grade)
            elif choice == "5":
                name = input("Enter pupil name to delete: ")
                self.delete_pupil(name)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def create_pupil_record(self):
        name = input("Enter pupil name: ")
        age = input("Enter pupil age: ")
        grade = input("Enter pupil grade: ")
        pupil = Pupil(name, age, grade)
        self.add_pupil(pupil)
        print("Pupil record created successfully.")

if __name__ == "__main__":
    cms = ClassManagementSystem()
    cms.main_menu()
