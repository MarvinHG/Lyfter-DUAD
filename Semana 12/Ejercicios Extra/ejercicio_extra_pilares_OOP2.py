'''
Ejercicios extra de Los 4 Pilares de OOP #2

Cree una clase abstracta User con los siguientes métodos abstractos:
    get_role()
    has_permission(permission)
Luego cree dos clases que hereden de ella:
    AdminUser
    RegularUser
Cada una debe implementar los métodos
Por ejemplo:
AdminUser siempre tiene permisos
RegularUser solo tiene permisos limitados ("read", por ejemplo)
Ejemplo:
    Entrada:
        user1 = AdminUser("Carlos")
    user2 = RegularUser("Andrea")

    Salida:
        print(user1.has_permission("delete"))  # True
        print(user2.has_permission("delete"))  # False

'''

from abc import ABC, abstractmethod


# Create the Abstract base class
class User(ABC):
    def __init__(self, name):
        self.name = name

    # Returns the user's role
    @abstractmethod
    def get_role(self):
        pass

    # Checks if the user has a specific permission
    @abstractmethod
    def has_permission(self, permission):
        pass


# Create the Admin user class
class AdminUser(User):

    # Returns admin role
    def get_role(self):
        return "Admin"

    # Admin always has all permissions
    def has_permission(self, permission):
        return True


# Create the Regular user class
class RegularUser(User):

    # Returns regular user role
    def get_role(self):
        return "Regular User"

    # Regular users only have limited permissions
    def has_permission(self, permission):
        allowed_permissions = ["read"]
        return permission in allowed_permissions


# Creating test users
user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")


# Testing permissions
print(user1.has_permission("delete"))   # True
print(user2.has_permission("delete"))   # False