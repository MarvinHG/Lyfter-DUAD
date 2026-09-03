'''
Ejercicios Extra de Estructuras de Datos 1

Cree una estructura que represente una cola básica (Queue) con objetos enlazados
- Restricción:
    - no usar list, dict, tuple, collections
- Métodos requeridos:
    - enqueue(data): agrega un nodo al final
        - Ejemplo:
            - Entrada:
                q.enqueue("A")
                q.enqueue("B")
                q.enqueue("C")
            - Salida:
                A -> B -> C
    - dequeue(): elimina y retorna el nodo del inicio
        - Ejemplo:
            - Entrada:
                q.dequeue()
            - Salida:
                "A"
    - print_all(): imprime todos los elementos de la cola en orden
        - Ejemplo:
            - Entrada:
                q.print_all()
            - Salida: 
                B -> C

'''
class Node:
    # Represents a single element (node) in the Queue
    data: str

    def __init__(self, data, next=None):
        self.data = data  # data: value stored in the node
        self.next = next  # next: reference to the next node in the queue


class Queue:
    def __init__(self):
        # front points to the first node in the queue
        # rear points to the last node in the queue
        self.front = None
        self.rear = None

    # Method to Add a new node to the end of the queue
    def enqueue(self, data):

        # Create the new node internally
        new_node = Node(data)

        # Check if queue is empty
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            # Link the current rear node to the new node
            self.rear.next = new_node

            # Update rear to the new last node
            self.rear = new_node

    # Method to Remove the first node from the queue
    def dequeue(self):

        # Check if queue is empty
        if self.front is None:
            print("La Queue está vacía")
            return

        # Save the removed value
        removed_data = self.front.data

        # Move front pointer to the next node
        self.front = self.front.next

        # If queue becomes empty, rear must also be None
        if self.front is None:
            self.rear = None

        return removed_data

    # Method to Print all elements in the queue from front to rear
    def print_all(self):

        current_node = self.front

        # If queue is empty, notify user
        if current_node is None:
            print("La Queue está vacía")
            return

        # Traverse the linked nodes until the end
        while current_node is not None:
            print(current_node.data, end="")

            if current_node.next is not None:
                print(" -> ", end="")

            current_node = current_node.next

        print()


# -------------------------
# Testing the Queue
# -------------------------

queue = Queue()

print("== Agregando nodos ==")

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("\n== Queue actual ==")
queue.print_all()

print("\n== Haciendo dequeue ==")
print(queue.dequeue())

print("\n== Queue después del dequeue ==")
queue.print_all()

print("\n== Otro dequeue ==")
print(queue.dequeue())

print("\n== Queue final ==")
queue.print_all()