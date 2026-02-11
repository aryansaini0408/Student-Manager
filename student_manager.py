import csv
import os
import sys

# Simple student file manager using fh.txt (CSV-like)
FILE = "fh.txt"

def create_empty_file(path=FILE):
    """Create an empty file with header. Returns True if created, False if already exists."""
    if os.path.exists(path):
        return False
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Class", "Roll"])
    return True

def add_student(name, cls, roll, path=FILE):
    if not os.path.exists(path):
        create_empty_file(path)
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, cls, roll])

def read_students(path=FILE):
    if not os.path.exists(path):
        return []
    with open(path, "r", newline="") as f:
        reader = csv.reader(f)
        return list(reader)

def view_students(path=FILE):
    rows = read_students(path)
    if not rows:
        print("No students found (file missing or empty).")
        return
    for i, r in enumerate(rows):
        if i == 0:
            print(" | ".join(r))
            print("-" * 40)
        else:
            print(" | ".join(r))

def update_student(roll, new_name=None, new_class=None, path=FILE):
    rows = read_students(path)
    if not rows:
        return False
    header = rows[0]
    changed = False
    for i in range(1, len(rows)):
        if len(rows[i]) >= 3 and rows[i][2] == str(roll):
            if new_name is not None:
                rows[i][0] = new_name
            if new_class is not None:
                rows[i][1] = new_class
            changed = True
    if changed:
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
    return changed

def delete_student(roll, path=FILE):
    rows = read_students(path)
    if not rows:
        return False
    header = rows[0]
    newrows = [header] + [r for r in rows[1:] if len(r) < 3 or r[2] != str(roll)]
    if len(newrows) != len(rows):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(newrows)
        return True
    return False

def interactive():
    while True:
        print("\n1 Create empty file\n2 Add student\n3 View students\n4 Update student\n5 Delete student\n6 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            ok = create_empty_file()
            print("Created." if ok else "File already exists.")
        elif choice == "2":
            name = input("Name: ").strip()
            cls = input("Class: ").strip()
            roll = input("Roll: ").strip()
            add_student(name, cls, roll)
            print("Added.")
        elif choice == "3":
            view_students()
        elif choice == "4":
            roll = input("Roll to update: ").strip()
            newname = input("New name (leave blank to keep): ").strip()
            newclass = input("New class (leave blank to keep): ").strip()
            changed = update_student(roll, new_name=newname if newname else None, new_class=newclass if newclass else None)
            print("Updated." if changed else "Not found.")
        elif choice == "5":
            roll = input("Roll to delete: ").strip()
            ok = delete_student(roll)
            print("Deleted." if ok else "Not found.")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        # quick non-interactive test
        if os.path.exists(FILE):
            os.remove(FILE)
        create_empty_file()
        add_student("Prince", "10A", "1")
        add_student("Mohnish", "10B", "2")
        print("After add:")
        view_students()
        update_student("2", new_name="Mohan")
        print("After update:")
        view_students()
        delete_student("1")
        print("After delete:")
        view_students()
    else:
        interactive()