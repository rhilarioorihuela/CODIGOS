
from prompting_base_tarea import preguntar

MENSAJE_ENVIADO = "¿Aceptan Yape?"

MENSAJE = f"""
Clasifica el mensaje en UNA categoría: BEB (bebidas), COM (comida), PAG (pagos) y RES (reservas).

Mensaje: 
{MENSAJE_ENVIADO}

Responde solo con la categoría.
"""

print("MENSAJE:", MENSAJE)
print("-------------------")
print("RESULTADO:" ,preguntar(MENSAJE))


