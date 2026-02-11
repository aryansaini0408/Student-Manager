# 🎓 Student Manager (File Handling Project)

A simple Python-based Student Management System that performs CRUD operations 
(Create, Read, Update, Delete) using file handling with CSV format.

This project stores student records in a file named `fh.txt`.

---

## 📌 Features

- Create student file with header
- Add new student records
- View all students
- Update student details by roll number
- Delete student by roll number
- Interactive menu-based interface
- Quick test mode using command-line argument

---

## 🛠 Technologies Used

- Python 3
- CSV module
- OS module
- Sys module

---

## 📂 File Structure

```
project-folder/
│
├── student_manager.py   # Main program file
├── fh.txt                # Data file (auto-created)
└── README.md
```

---

## ▶️ How to Run

### 🔹 Interactive Mode

Run:

```bash
python student_manager.py
```

You will see a menu:

```
1 Create empty file
2 Add student
3 View students
4 Update student
5 Delete student
6 Exit
```

---

### 🔹 Test Mode (Non-interactive)

Run:

```bash
python student_manager.py --test
```

This will:
- Create file
- Add sample students
- Update a student
- Delete a student
- Display results

---

## 📁 Data Format (fh.txt)

The file is stored in CSV format:

```
Name,Class,Roll
Prince,10A,1
Mohnish,10B,2
```

---

## 🧠 Concepts Demonstrated

- File handling in Python
- CSV read/write operations
- Command-line arguments
- Modular function design
- Basic CRUD implementation

---

## 👨‍💻 Author

Aryan Saini

---

## 📌 Note

If `fh.txt` does not exist, it will be created automatically when adding a student.

