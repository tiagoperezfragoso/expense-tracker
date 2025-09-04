# 📊 Expense Tracker (Controle de Despesas)

A simple **Expense Tracker** built in Python to help manage personal finances.  
The program allows you to add, list, and summarize expenses and incomes, storing the data in a JSON file for persistence.

---

## ✨ Features
- Add new expenses and incomes (with date, category, description, and amount)  
- List all transactions with filters (by date or category)  
- Show a summary (total income, total expenses, balance)  
- Data saved automatically in `data/expense.json`  
- Simple menu-driven console interface  

---

## 📂 Project Structure
```
expense/
│
├── data/              # Stores JSON data
│   └── expense.json   # Your expenses will be saved here
│
└── src/               # Source code
    └── main.py        # Entry point of the application
```

---

## ⚙️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install requirements (if you add any in the future, e.g., `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage
Run the program from the project root:
```bash
python src/main.py
```

Example interaction:
```
1 - Add expense
2 - Add income
3 - List transactions
4 - Show summary
5 - Exit
```

---

## 💡 Next Improvements
- Edit and delete transactions  
- Monthly/category reports  
- Export to CSV  
- Budget alerts (warn when overspending)  
- Graphical charts  

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.  

---

## 📜 License
This project is licensed under the MIT License.  
