'''
Ejercicios Extra de Estructuras de Datos 2

Cree una clase LinkedList con los métodos:
- insert_front(data): Inserta al inicio
    - Ejemplo:
        - Entrada: 
            - insert_front(10)
            - insert_front(20)
        - Salida: 
            - 20 -> 10
- insert_back(data): Inserta al final
    - Ejemplo:
        - Entrada:
            - insert_back(30)
        - Salida: 
            - 20 -> 10 -> 30
- delete(data): Elimina el primer nodo con el valor dado
    - Ejemplo:
        - Entrada:
            - delete(10)
        - Salida:
            - 20 -> 30
- print_all(): Imprime todos los valores
    - Ejemplo:
        - print_all() #20 -> 30
'''

class Node:
    # Represents a single element (node) in the Linked List
    data: int

    def __init__(self, data, next=None):
        self.data = data  # data: value stored in the node
        self.next = next  # next: reference to the next node in the list


class LinkedList:
    def __init__(self):
        # head points to the first node in the linked list
        self.head = None

    # Method to Insert a new node at the beginning of the list
    def insert_front(self, data):

        # Create a new node
        new_node = Node(data)

        # New node points to the current head
        new_node.next = self.head

        # Update head to the new first node
        self.head = new_node

    # Method to Insert a new node at the end of the list
    def insert_back(self, data):

        # Create a new node
        new_node = Node(data)

        # Check if list is empty
        if self.head is None:
            self.head = new_node
            return

        # Start from the head node
        current_node = self.head

        # Traverse until the last node
        while current_node.next is not None:
            current_node = current_node.next

        # Link the last node to the new node
        current_node.next = new_node

    # Method to Delete the first node with the given value
    def delete(self, data):

        # Check if list is empty
        if self.head is None:
            print("La Linked List está vacía")
            return

        # If the first node contains the value
        if self.head.data == data:
            self.head = self.head.next
            return

        # Start traversing the list
        previous = self.head
        current_node = self.head.next

        # Search for the node containing the value
        while current_node is not None:

            if current_node.data == data:
                # Skip the current node
                previous.next = current_node.next
                return

            previous = current_node
            current_node = current_node.next

        # Value not found
        print(f"El valor {data} no existe en la lista.")

    # Method to Print all elements in the linked list
    def print_all(self):

        current_node = self.head

        # If list is empty, notify user
        if current_node is None:
            print("La Linked List está vacía")
            return

        # Traverse the linked nodes until the end
        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()


# -------------------------
# Testing the Linked List
# -------------------------

linked_list = LinkedList()

print("== Insertando al inicio ==")

linked_list.insert_front(10)
linked_list.insert_front(20)

print("\n== Lista actual ==")
linked_list.print_all()

print("\n== Insertando al final ==")

linked_list.insert_back(30)

print("\n== Lista después de insert_back ==")
linked_list.print_all()

print("\n== Eliminando 10 ==")

linked_list.delete(10)

print("\n== Lista después de delete ==")
linked_list.print_all()

print("\n== Eliminando 50 ==")

linked_list.delete(50)

print("\n== Lista después de delete ==")
linked_list.print_all()


print("\n== Insertando al final ==")

linked_list.insert_back(40)

print("\n== Lista final ==")
linked_list.print_all()