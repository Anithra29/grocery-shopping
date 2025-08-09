# Grocery Store Management System

This is a **Python + MySQL** based project I developed to manage a grocery store’s inventory and sales in a simple and efficient way.  
The system runs in the command line and allows store owners to easily keep track of products, stock, and sales.

## 📌 Project Overview
The application provides a menu-driven interface where the user can:
- Add new products with details like name, category, price, and available stock.
- View all products currently in the store.
- Update stock levels when new inventory arrives.
- Delete products that are no longer available.
- Record sales transactions, which automatically deduct the sold quantity from stock.
- View a sales report to track all transactions.

## 💡 What I Did
1. **Designed the database** in MySQL with two main tables:
   - `products` – Stores product details and stock.
   - `sales` – Stores sales records.
2. **Wrote Python code** using the `pymysql` library to connect to the database.
3. Implemented **CRUD operations** (Create, Read, Update, Delete) for managing inventory.
4. Added **sales tracking** so stock updates automatically after a sale.
5. Made the program **menu-driven** so users can navigate easily without technical knowledge.

## 🛠️ Technologies Used
- **Python 3.x**
- **MySQL** database
- **PyMySQL** library for database interaction

## 🎯 Purpose
The goal of this project is to provide a **simple, offline inventory management system** for small grocery store owners who want to track stock and sales without needing a complex or expensive software solution.

---

