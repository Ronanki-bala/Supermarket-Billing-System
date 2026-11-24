from datetime import datetime

products = {
    1: {"name": "Rice", "price": 60},
    2: {"name": "Wheat Flour", "price": 45},
    3: {"name": "Sugar", "price": 50},
    4: {"name": "Milk", "price": 30},
    5: {"name": "Oil", "price": 150},
    6: {"name": "Soap", "price": 35},
    7: {"name": "Shampoo", "price": 120},
    8: {"name": "Biscuits", "price": 20},
    9: {"name": "Tea Powder", "price": 80},
    10: {"name": "Salt", "price": 25}
}

cart = {}
TAX_RATE = 0.12

def display_products():
    print("\n========== PRODUCT LIST ==========")
    print("{:<10} {:<20} {:<10}".format(
        "ID", "Product", "Price"
    ))
    print("----------------------------------")

    for product_id, details in products.items():
        print("{:<10} {:<20} Rs.{:<10}".format(
            product_id,
            details["name"],
            details["price"]
        ))

    print("----------------------------------")
    print("Enter 0 to exit.")


def add_to_cart():
    display_products()

    while True:
        try:
            choice = int(input("\nEnter product ID: "))

            if choice == 0:
                break

            if choice not in products:
                print("Invalid product ID! Try again.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            product_name = products[choice]["name"]
            price = products[choice]["price"]

            if choice in cart:
                cart[choice]["quantity"] += quantity
            else:
                cart[choice] = {
                    "name": product_name,
                    "price": price,
                    "quantity": quantity
                }

            print(f"{product_name} added to cart successfully!")

            again = input(
                "\nDo you want to add another product? (yes/no): "
            ).lower()

            if again != "yes":
                break

        except ValueError:
            print("Please enter a valid numeric value!")


def generate_bill(customer_name):

    if not cart:
        print("\nYour cart is empty. No bill generated.")
        return

    print("\n")
    print("=" * 60)
    print(" ABC SUPERMARKET")
    print(" Hyderabad, Telangana")
    print("=" * 60)

    print("Customer Name :", customer_name)
    print("Date & Time :", datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    ))
    print("-" * 60)

    print("{:<15} {:<8} {:<12} {:<12}".format(
        "Item", "Qty", "Price", "Total"
    ))
    print("-" * 60)

    subtotal = 0

    for item in cart.values():

        item_total = item["price"] * item["quantity"]
        subtotal += item_total

        print("{:<15} {:<8} Rs.{:<9} Rs.{:<9}".format(
            item["name"],
            item["quantity"],
            item["price"],
            item_total
        ))

    tax = subtotal * TAX_RATE
    grand_total = subtotal + tax

    print("-" * 60)

    print("{:<35} Rs.{:.2f}".format(
        "Total Amount:", subtotal
    ))

    print("{:<35} Rs.{:.2f}".format(
        "GST (12%):", tax
    ))

    print("=" * 60)

    print("{:<35} Rs.{:.2f}".format(
        "Grand Total:", grand_total
    ))

    print("=" * 60)
    print(" THANK YOU FOR SHOPPING!")
    print(" VISIT AGAIN!")
    print("=" * 60)


def main():

    print("\n")
    print("*" * 45)
    print(" WELCOME TO ABC SUPERMARKET")
    print("*" * 45)

    customer_name = input("\nEnter customer name: ")

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. View Products")
        print("2. Add Products to Cart")
        print("3. Generate Bill")
        print("4. Exit")
        print("===============================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_products()

            elif choice == 2:
                add_to_cart()

            elif choice == 3:
                generate_bill(customer_name)
                break

            elif choice == 4:
                print("\nThank you for visiting ABC Supermarket!")
                break

            else:
                print("Invalid choice! Please select 1 to 4.")

        except ValueError:
            print("Please enter a valid number!")

    print("\nProgram exited successfully.")


if __name__ == "__main__":
    main()

