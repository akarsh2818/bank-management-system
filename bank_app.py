import json
import random
import string
from pathlib import Path
import streamlit as st

class Bank:
    database = 'data.json'
    data = []

    @staticmethod
    def load_data():
        try:
            path = Path(Bank.database)
            if path.exists():
                with open(path) as fs:
                    Bank.data = json.load(fs)
            else:
                path.write_text("[]")
                Bank.data = []
        except Exception as err:
            st.error(f"Error loading data: {err}")
            Bank.data = []

    @staticmethod
    def __update():
        with open(Bank.database, "w") as fs:
            json.dump(Bank.data, fs, indent=4)

    @staticmethod
    def __accountgenerate():
        id = random.choices(string.ascii_letters, k=3) + \
             random.choices(string.digits, k=3) + \
             random.choices("!@#$%^&*_", k=1)
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "You must be 18+ and pin should be 4 digits."

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": cls.__accountgenerate(),
            "balance": 0
        }
        cls.data.append(info)
        cls.__update()
        return True, info

    @classmethod
    def deposit(cls, accountNo, pin, amount):
        for user in cls.data:
            if user['accountNo'] == accountNo and user['pin'] == pin:
                if 0 < amount <= 10000:
                    user['balance'] += amount
                    cls.__update()
                    return True, user
                else:
                    return False, "Amount should be between 1 and 10000."
        return False, "Account not found."

    @classmethod
    def withdraw(cls, accountNo, pin, amount):
        for user in cls.data:
            if user['accountNo'] == accountNo and user['pin'] == pin:
                if user['balance'] >= amount:
                    user['balance'] -= amount
                    cls.__update()
                    return True, user
                else:
                    return False, "Insufficient balance."
        return False, "Account not found."

    @classmethod
    def show_details(cls, accountNo, pin):
        for user in cls.data:
            if user['accountNo'] == accountNo and user['pin'] == pin:
                return True, user
        return False, "Account not found."

    @classmethod
    def update_details(cls, accountNo, pin, name=None, email=None, new_pin=None):
        for user in cls.data:
            if user['accountNo'] == accountNo and user['pin'] == pin:
                if name: user['name'] = name
                if email: user['email'] = email
                if new_pin: user['pin'] = int(new_pin)
                cls.__update()
                return True, user
        return False, "Account not found."

    @classmethod
    def delete_account(cls, accountNo, pin):
        for user in cls.data:
            if user['accountNo'] == accountNo and user['pin'] == pin:
                cls.data.remove(user)
                cls.__update()
                return True, "Account deleted successfully."
        return False, "Account not found."


# ------------------------------
# 🟢 Streamlit App Starts Here
# ------------------------------

st.set_page_config(page_title="Bank Management System", layout="centered")
st.title("🏦 Bank Management System")

# 🔁 Load data on each run
Bank.load_data()

option = st.selectbox("Choose an option", [
    "Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"])

if option == "Create Account":
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("PIN (4-digit)", type="password")
    if st.button("Create"):
        if name and age and email and pin:
            success, result = Bank.create_account(name, int(age), email, int(pin))
            if success:
                st.success(f"✅ Account created!\nYour account number: {result['accountNo']}")
            else:
                st.error(result)

if option == "Deposit":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Deposit"):
        success, result = Bank.deposit(acc, int(pin), int(amount))
        if success:
            st.success(f"✅ Deposit successful. New Balance: ₹{result['balance']}")
        else:
            st.error(result)

if option == "Withdraw":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        success, result = Bank.withdraw(acc, int(pin), int(amount))
        if success:
            st.success(f"✅ Withdrawal successful. New Balance: ₹{result['balance']}")
        else:
            st.error(result)

if option == "Show Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        success, result = Bank.show_details(acc, int(pin))
        if success:
            st.json(result)
        else:
            st.error(result)

if option == "Update Details":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")
    if st.button("Update"):
        success, result = Bank.update_details(acc, int(pin), name, email, new_pin)
        if success:
            st.success("✅ Details updated successfully.")
            st.json(result)
        else:
            st.error(result)

if option == "Delete Account":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        success, msg = Bank.delete_account(acc, int(pin))
        if success:
            st.success("🗑️ " + msg)
        else:
            st.error(msg)
