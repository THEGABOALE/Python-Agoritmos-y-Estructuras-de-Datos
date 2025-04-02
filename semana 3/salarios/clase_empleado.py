class Empleado:
    def __init__(self, nombre, salarioBruto):
        self.__nombre = nombre
        self.__salarioBruto = salarioBruto
        
    def getNombre(self):
        return self.__nombre
    
    def get_salarioNeto(self):
        from salario_neto import SalarioNeto
        return SalarioNeto(self.__salarioBruto)