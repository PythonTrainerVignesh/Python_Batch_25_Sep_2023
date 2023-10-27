# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b


class ReportCard:

    def __init__(self):
        print("welcome!")

    def class_std(self):
        pass

    def subjects(self):
        pass

    def student_name(self):
        pass

    def student_roll(self):
        pass


class BankAccount:
    # Constructors
    def __init__(self, balance: float, fname: str, lname: str, pan: str, aadhar: int, phone: int):
        self.lname = lname
        self.fname = fname
        self.balance = balance
        self.pan = pan
        self.aadhar = aadhar
        self.phone = phone

    def credit(self, amount: float):
        pass

    def debit(self, amount: float):
        pass


class Products:
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        assert len(name) >= 3, "Invalid product name entry."    # Validate the objects
        assert price >= 0, "Invalid price entry."
        assert quantity >= 0, "Invalid quantity entry."

        self.name = name
        self.price = price
        self.quantity = quantity

        Products.all.append(self)

    def name(self):
        return self.name

    def price(self):
        return self.price

    def quantity(self):
        return self.quantity

    def total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"Products('{self.name}', {self.price}, {self.quantity})"
