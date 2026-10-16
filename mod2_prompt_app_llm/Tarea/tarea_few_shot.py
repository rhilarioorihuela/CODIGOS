
from prompting_base_tarea import preguntar

MENSAJE_ENVIADO = "¿Aceptan Yape?"

MENSAJE = f"""
Clasifica el mensaje en UNA categoría: BEB (bebidas), COM (comida), PAG (pagos) y RES (reservas).

Mensaje: "Me dieron una bebida que no solicité"                 -> BEB
Mensaje: "Quiero cambiar la orden de comida que realice"        -> COM
Mensaje: "Me facturaron un producto que no compré"              -> PAG
Mensaje: "Requiro una reserva para el dia de mañana a las 8pm"  -> RES

Mensaje: 
{MENSAJE_ENVIADO}

Responde solo con la categoría.
"""

print("MENSAJE:", MENSAJE)
print("-------------------")
print("RESULTADO:" ,preguntar(MENSAJE))

