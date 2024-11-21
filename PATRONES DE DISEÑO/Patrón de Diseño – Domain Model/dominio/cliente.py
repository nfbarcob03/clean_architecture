class Cliente: 
    def __init__(self, id_cliente: int, nombre: str, email: str): 
        self.id_cliente = id_cliente 
        self.nombre = nombre 
        self.email = email 
    
    def __repr__(self): 
        return f"Cliente({self.id_cliente}, '{self.nombre}', '{self.email}')" 
    
    def actualizar_email(self, nuevo_email: str): 
        if '@' in nuevo_email: 
            self.email = nuevo_email
        else: 
            raise ValueError("El email proporcionado no es vlido.")