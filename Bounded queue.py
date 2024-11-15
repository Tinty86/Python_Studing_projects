
class BoundedQueue:
    head = None

    def set_length(self) -> int:
        
        length = 0
       
        if not self.head:
            length = 0
            return length
        
        customer = self.head 
        
        while customer.next_costumer:
            length += 1
            costumer = costumer.next_costumer

        length += 1
        return length

    class Customer:
        data = None
        next_costumer = None

        def __init__(self, data, next_costumer = None):
            self.data = data
            self.next_costumer = next_costumer

    def append(self,data, user_length=5):
        length = self.set_length()
        if length < user_length:
            if not self.head:
                self.head = self.Customer(data)
                return
            
            costumer = self.head
            while costumer.next_costumer:
                costumer = costumer.next_costumer 

            costumer.next_costumer = self.Customer(data)

        else:
            print("Error: Too many objects in the queue")

    def first_out(self):
        if not self.head:
            return "Error: Empty queue"
        self.head = self.head.next_costumer

    def out(self):
        costumer = self.head
        if not self.head:
            return "Error: Empty queue"
        if not self.head.next_costumer:
            print(f"[{costumer.data}]")
            return 
        
        print(f"[{costumer.data}] <- [{costumer.next_costumer.data}]", end="")
        costumer = costumer.next_costumer
        while costumer.next_costumer:
            print(f" <- [{costumer.next_costumer.data}]")
            costumer = costumer.next_costumer
            

queue = BoundedQueue()

queue.append(1)
queue.append(2)

queue.out()
