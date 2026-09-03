'''
Ejercicios Extra de Estructuras de Datos 3

Lista doblemente enlazada
- Requisitos:
    - Cada nodo debe tener referencia al siguiente y al anterior
- Métodos:
    - append(data): Agrega al final
        - Ejemplo:
            - Entrada:
                - append("A")
                - append("B")
                - append("C")
            - Salida (print_forward):
                - A -> B -> C
            - Salida (print_bacward)
                - C -> B -> A
    - prepend(data): Agrega al inicio
        - Ejemplo:
            - Entrada:
                - prepend("X")
            - Salida (print_forward):
                - X -> A -> B -> C
            - Salida (print_bacward)
                - C -> B -> A -> X
    - delete(data): Elimina el primer nodo con ese valor
        - Ejemplo:
            - Entrada:
                - delete("B")
            - Salida (print_forward):
                - X -> A -> C
            - Salida (print_bacward)
                - C -> A -> X
    - print_forward() y print_backward(): Imprime en ambas direcciones
        - Ejemplo:
            Salida:
                - print_forward()  #→ X -> A -> C
                - print_backward() #← C -> A -> X
'''

class Node:
    # Represents a single element (node) in the Doubly Linked List
    data: str

    def __init__(self, data):
        self.data = data  # data: value stored in the node
        self.next = None  # next: reference to the next node
        self.prev = None  # prev: reference to the previous node


class DoublyLinkedList:
    def __init__(self):
        # head points to the first node
        # tail points to the last node
        self.head = None
        self.tail = None

    # Method to Add a new node at the end of the list
    def append(self, data):

        # Create a new node
        new_node = Node(data)

        # Check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Link current tail to the new node
        self.tail.next = new_node

        # Link new node back to the current tail
        new_node.prev = self.tail

        # Update tail
        self.tail = new_node

    # Method to Add a new node at the beginning of the list
    def prepend(self, data):

        # Create a new node
        new_node = Node(data)

        # Check if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Link new node to current head
        new_node.next = self.head

        # Link current head back to the new node
        self.head.prev = new_node

        # Update head
        self.head = new_node

    # Method to Delete the first node with the given value
    def delete(self, data):

        # Check if list is empty
        if self.head is None:
            print("La lista está vacía")
            return

        current_node = self.head

        # Search for the node
        while current_node is not None:

            if current_node.data == data:

                # If deleting the first node
                if current_node == self.head:
                    self.head = current_node.next

                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None

                    return

                # If deleting the last node
                elif current_node == self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None
                    return

                # If deleting a middle node
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    return

            current_node = current_node.next

        print(f"El valor {data} no existe en la lista.")

    # Method to Print all elements from head to tail
    def print_forward(self):

        current_node = self.head

        if current_node is None:
            print("La lista está vacía")
            return

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()

    # Method to Print all elements from tail to head
    def print_backward(self):

        current_node = self.tail

        if current_node is None:
            print("La lista está vacía")
            return

        while current_node is not None:
            print(current_node.data, end="")

            if current_node.prev is not None:
                print(" -> ", end="")

            current_node = current_node.prev

        print()


# -------------------------
# Testing the Doubly Linked List
# -------------------------

dll = DoublyLinkedList()

print("== Agregando al final ==")
dll.append("A")
dll.append("B")
dll.append("C")

print("\nForward:")
dll.print_forward()

print("\nBackward:")
dll.print_backward()

print("\n== Agregando al inicio ==")
dll.prepend("X")

print("\nForward:")
dll.print_forward()

print("\nBackward:")
dll.print_backward()

print("\n== Eliminando B ==")
dll.delete("B")

print("\nForward:")
dll.print_forward()

print("\nBackward:")
dll.print_backward()