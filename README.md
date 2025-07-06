🏦 Bank Management System (with Streamlit)
This is a simple and interactive Bank Management System built using Python and Streamlit. The application allows users to create and manage bank accounts with essential features like deposit, withdrawal, balance inquiry, detail update, and account deletion. All data is stored in a local JSON file for persistence.

📌 Features
✅ Create Account — Users can create a new bank account by providing basic information.
💰 Deposit — Deposit money into the account (limit: ₹1 - ₹10,000).
💸 Withdraw — Withdraw money if sufficient balance is available.
🔍 Show Details — View account details securely using account number and PIN.
🛠️ Update Details — Update name, email, or PIN.
🗑️ Delete Account — Permanently delete an account after confirmation.

🛠️ Tech Stack
Frontend: Streamlit

Backend: Python Classes & JSON for local storage

Storage: data.json file for storing user account data

🧪 How It Works
Each user account is uniquely generated using random letters, numbers, and a symbol.

Users authenticate using an account number and a 4-digit PIN.

Balance operations (deposit/withdraw) and details are updated in data.json persistently.

The UI is powered by Streamlit widgets such as input fields, buttons, and dropdowns.

🚀 Getting Started
🔧 Prerequisites
Python 3.7+

Streamlit

💻 Installation
bash
Copy
Edit
# Clone the repository or copy the files
git clone https://github.com/yourusername/bank-management-streamlit.git
cd bank-management-streamlit

# Install dependencies
pip install streamlit
▶️ Run the App
bash
Copy
Edit
streamlit run bank_app.py
Make sure data.json is present in the same directory. If not, it will be auto-generated.

📂 File Structure
bash
Copy
Edit
📁 bank-management-streamlit/
│
├── bank_app.py        # Main Streamlit application file
├── data.json          # JSON file to store all account data
└── README.md          # Project documentation (this file)
🔐 Security & Validation
PINs are 4-digit numbers required for every secure operation.

Input validation for age, amount limits, email, and duplicate entries.

No sensitive information is exposed in the frontend.

🧠 Concepts Applied
Python OOP (Object-Oriented Programming)

JSON file handling

Streamlit UI integration

Basic authentication logic

Data persistence without a database

📌 Example Usage
Account Creation

yaml
Copy
Edit
Name: John Doe
Age: 25
Email: john@example.com
PIN: 1234
→ ✅ Account created! Your account number: Ab1$X7
Deposit ₹500

yaml
Copy
Edit
Account No: Ab1$X7
PIN: 1234
Amount: ₹500
→ ✅ Deposit successful. New Balance: ₹500
📈 Future Enhancements
Add database support (SQLite, MongoDB)

Add login/logout session management

Add transaction history for each user

Use hashed PINs for better security
