
class Queue:
    head = None

    class Customer:
        data = None
        next_customer = None

        def __init__(self, data, next_customer = None):
            self.data = data
            self.next_customer = next_customer

    def append(self,data):
        if not self.head:
            self.head = self.Customer(data)
            return
        customer = self.head
        while customer.next_customer:
            customer = customer.next_customer

        customer.next_customer = self.Customer(data)

    def first_out(self, ):
        if not self.head:
            return "Error: Empty queue"
        head = self.head
        self.head = head.next_customer

    def out(self):
        customer = self.head
        if not self.head:
            return "Error: Empty queue"
        if not self.head.next_customer:
            print(f"[{customer.data}]")
            return 
        
        customer = self.head
        print(f"[{customer.data}]", end=" ")
        
        while customer.next_customer:
            print(f"-> [{customer.next_customer.data}]", end=" ")
            customer = customer.next_customer

        
            

queue = Queue()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)

queue.first_out()

queue.out()

