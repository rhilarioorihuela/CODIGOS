
from prompting_base_tarea import preguntar

# ----- CASO 1 ----

MENSAJE = """
El café estaba frío pero el pan estaba delicioso. ¿Qué opinas?
"""
print("MENSAJE:", MENSAJE)
print("-------------------")
print("RESULTADO:" ,preguntar(MENSAJE))


# ----- CASO 2 ----


MENSAJE_ESTRUCTURADO = """

Eres el sistema de clasificación de CaféYa.
Clasifica el sentimiento del siguiente mensaje de un cliente.

Mensaje:
\"\"\"El café estaba frío pero el pan estaba delicioso.\"\"\"

Responde con una sola palabra: positivo, negativo o neutral.
"""

print("MENSAJE_ESTRUCTURADO:", MENSAJE_ESTRUCTURADO)
print("-------------------")
print("RESULTADO:", preguntar(MENSAJE_ESTRUCTURADO))

