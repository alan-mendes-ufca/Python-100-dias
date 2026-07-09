"""Os três pilares da programação orientada a objetos: encapsulamento, herança e polimorfismo.
Este arquivo implementa um sistema simples de folha de pagamento mensal."""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """Funcionário (classe base abstrata)."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """Calcule o salário mensal."""
        pass


class Manager(Employee):
    """Gerente de departamento."""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """Programador."""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """Vendedor."""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    """Fábrica de objetos de funcionários."""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """Crie um funcionário."""
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp
