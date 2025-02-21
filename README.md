A simple command-line To-Do List application built with Python. It allows users to add, remove, complete, and list tasks, with all tasks stored in a JSON file for persistence.

🚀 Features: 
✅ Add tasks with a description
✅ Remove tasks by their index or name
✅ Mark tasks as completed
✅ View all pending and completed tasks
✅ Data persistence using a JSON file
✅ Error handling for invalid inputs

🛠️ Tech Stack: 
Python 3.x, 
JSON (for data storage), 
argparse (for command-line arguments).

## 🚀 **How to Use it after it was cloned**  

### **1️⃣ Add a Task**  
To add a new task:  
```sh
python todo.py add "Buy groceries"
```
 **Example Output:**  
`Task "Buy groceries" was added successfully!`

---
### **2️⃣ List All Tasks**  
To view your current to-do list:  
```sh
python todo.py list
```
**Example Output:**  
```
📌 Your To-Do List:
1. Buy groceries
2. Finish homework
3. Call mom
```
### **3️⃣ Remove a Task**  
To delete a task, use its number:  
```sh
python todo.py delete 2
```
**Example Output:**  
`The 2. task was deleted successfully.`  

`If you try deleting an invalid task number, you’ll see:`
`Invalid task number. Please enter a valid number.`  

---
### **4️⃣ Mark a Task as Completed**  
To mark a task as done:  
```sh
python todo.py mark 1
```
**Example Output:**  
`The 1. task was marked as completed.`  

Now, listing tasks will show:  
```
📌 Your To-Do List:
1. [✅] Buy groceries
2. [ ] Finish homework
```

📌 Future Enhancements that could be made: 
🔹 Add SQLite database for better storage
🔹 Implement a simple GUI with Tkinter
🔹 Add unit tests using unittest. 
🔹 Set due dates
🔹 Add priority levels

This project is open-source under the MIT License.
