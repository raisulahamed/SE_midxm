class CustomerOrder:
    def __init__(self, orderID, customerName, orderAmount):
        self.orderID = orderID
        self.customerName = customerName
        self.orderAmount = orderAmount

    def inputOrder(self):
        self.orderID = input()
        self.customerName = input()
        self.orderAmount = float()
    def showOrder(self):
        print(f"Order id : {self.orderID} , Customer's Name : {self.customerName}, Order Amount : {self.orderAmount}")

    def calculateTotal(orders):
        total = sum(order.orderAmount for order in orders)
        print(f"Total Order Amount : {total}")
order1 = CustomerOrder("C223114", "Raisul", 300)
order2 = CustomerOrder("C223115", "Robi", 600)
order3 = CustomerOrder("C223116", "Faruk", 654)
order4 = CustomerOrder("C223117", "Sadi", 900)

orders = [order1, order2, order3, order4]

for order in orders:
    order.showOrder()
CustomerOrder.calculateTotal(orders)

