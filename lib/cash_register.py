#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction_amount = {"title": None, "price": 0, "quantity": 0}
  
  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    self.last_transaction = {"title": title, "price": price, "quantity": quantity} 
    for _ in range(quantity):
        self.items.append(title)

  def apply_discount(self):
    if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            total_display = int(self.total) if self.total.is_integer() else f"{self.total:.2f}"
            print(f"After the discount, the total comes to ${total_display}.")
    else:
        print("There is no discount to apply.")

  def void_last_transaction(self):
     if self.last_transaction["title"]:
            self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
            for _ in range(self.last_transaction["quantity"]):
                if self.last_transaction["title"] in self.items:
                    self.items.remove(self.last_transaction["title"])
            
            self.last_transaction = {"title": None, "price": 0, "quantity": 0}
     

   




