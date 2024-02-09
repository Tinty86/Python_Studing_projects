
class Priority_queue:
    head = None

    class Object:
        data = None
        next_object = None
        priority = None
        def __init__(self, data, priority=0, next_object=None) -> set:
            self.data = data
            self.next_object = next_object
            self.priority = priority

    def append(self, data, priority=0):
        if not self.head:
            self.head = self.Object(data, priority=priority)
            return
        
        if not self.head.next_object:
            if priority > self.head.priority:
                self.head = self.Object(data, priority, next_object=self.head)
                return
            else:
                self.head.next_object = self.Object(data, priority)
                return
        

        if self.head.priority < priority:
            self.head = self.Object(data, priority, next_object=self.head)
            return
            
        object = self.head

        while object.priority >= priority and object.next_object:
            prev_object = object
            object = object.next_object
            
        if not object.next_object:
            object.next_object = self.Object(data, priority)
            return
        
        prev_object.next_object = self.Object(data, priority, next_object=object)

    def print_queue(self):
        if not self.head:
            return "[]"
        
        if not self.head.next_object:
            print(f"[{self.head.data}]")
        
        object = self.head
        print(f"[{object.data}]", end=" ")
        
        while object.next_object:
            print(f"-> [{object.next_object.data}]", end=" ")
            object = object.next_object


queue = Priority_queue()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6, priority=1)

queue.print_queue()
