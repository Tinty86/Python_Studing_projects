

"""
FIFO 
First in, first out
"""
class Stack:
    head = None
    max_stack_length = None
    current_stack_length = None

    class Object:
        data = None
        next_object = None
        prev_object = None

        def __init__(self, data, prev_object=None, next_object = None):
            self.data = data
            self.object = next_object
            self.prev_object = prev_object

    def set_length(self, user_length=5):
        self.max_stack_length = int(user_length)

    def append(self, data):
        if not self.head:
            self.head = self.Object(data)
            return
        
        current_stack_length = 1

        object = self.head

        while object.next_object and current_stack_length < self.max_stack_length:
            current_stack_length += 1
            object = object.next_object
            prev_object = object

        else:
            current_stack_length += 1

            self.current_stack_length = current_stack_length

            if current_stack_length > self.max_stack_length:
                print("Error: Stack overflow")
                exit()

            if not self.head.next_object:
                self.head.next_object = self.Object(data, prev_object = self.head)

            else:
                object.next_object = self.Object(data, prev_object)


    def print_stack(self, direction):
        if not self.head:
            print("Stack is empty")
            return
        
        if direction == "hor":
            object = self.head
            print(f"[{object.data}]", end=" ")

            while object.next_object:
                print(f"<- [{object.next_object.data}]", end=" ")
                object = object.next_object

        if direction == "vert":
            object = self.head

            stack_matrix = []
            for i in range(self.current_stack_length):
                stack_matrix.append(object.data)
                object = object.next_object
                
            stack_matrix.reverse()
            for i in stack_matrix:
                if stack_matrix.index(i)+1 == len(stack_matrix):
                    print(f"[{i}]")
                    return
                else:
                    print(f"[{i}]")
                    print(" ↓")


    def out_from_stack(self):
        object = self.head
        while object.next_object: 
            object = object.next_object

        object.prev_object.next_object = None

            

queue = Stack()

queue.set_length(4)

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# queue.print_stack(direction="hor")

queue.print_stack(direction="vert")
