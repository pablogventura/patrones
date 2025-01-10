# como disparador para usarlo puede ser ver funciones que tienen chequeos previos todos iguales
# y que se pueden encapsular en un decorador
def tiene_que_ser_admin(func):
    def wrapper(usuario):
        if usuario.es_admin:
            return func(usuario)
        else:
            raise ValueError("No tienes permisos de administrador")
    return wrapper

@tiene_que_ser_admin
def get_contraseña(usuario):
    return usuario.contraseña

