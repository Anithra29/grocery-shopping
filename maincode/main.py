import pymysql

db = pymysql.connect(
    host="localhost",
    user="root",
    password="VARNIKA2005",
    database="grocery_store"
)

cursor=db.cursor()

def add_product():
    
    name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    cursor.execute("INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s)",
                   (name, category, price, stock))
    db.commit()
    print("Product added successfully!")
def view_products():
    
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)
def update_stock():
    
    pid = int(input("Enter product ID to update: "))
    new_stock = int(input("New stock: "))
    cursor.execute("UPDATE products SET stock = stock + %s WHERE product_id = %s", (new_stock, pid))
    db.commit()
    print("Stock updated!")
def delete_product():
    
    pid = int(input("Enter product ID to delete: "))
    cursor.execute("DELETE FROM products WHERE product_id = %s", (pid,))
    db.commit()
    print("Product deleted!")

def sell_product():
    
    pid = int(input("Product ID: "))
    quantity = int(input("Quantity to sell: "))
    cursor.execute("SELECT stock FROM products WHERE product_id = %s", (pid,))
    stock = cursor.fetchone()
    if stock and stock[0] >= quantity:
        cursor.execute("INSERT INTO sales (product_id, quantity) VALUES (%s, %s)", (pid, quantity))
        cursor.execute("UPDATE products SET stock = stock - %s WHERE product_id = %s", (quantity, pid))
        db.commit()
        print("Sale completed.")
    else:
        print("Not enough stock!")

def view_sales():
  
    cursor.execute("SELECT * FROM sales")
    for row in cursor.fetchall():
        print(row)


def main():

    while True:
        print("Grocery Menu")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Stock")
        print("4. Delete Product")
        print("5. Sell Product")
        print("6. View Sales Report")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_stock()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            sell_product()
        elif choice == '6':
            view_sales()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()  
    db.close()    
