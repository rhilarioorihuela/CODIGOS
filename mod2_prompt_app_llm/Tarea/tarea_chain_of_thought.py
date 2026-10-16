from prompting_base_tarea import preguntar
# ----- CASO 1 : Respuesta directa ----

MENSAJE = f"""
Un cliente de CaféYa compró 2 capuchinos a S/ 9 cada uno y 3 empanadas a S/ 6 cada una, con un cupón de 10 % de descuento sobre el total. Si paga con S/ 50, ¿cuánto vuelto recibe?

Responde solo con el monto.
"""
print("=============================")
print("MENSAJE:", MENSAJE)
print("-------------------")
print("RESULTADO:" ,preguntar(MENSAJE))

# ----- CASO 2 : Detalle del paso a paso ----

MENSAJE_CoT = f"""

Un cliente de CaféYa compró 2 capuchinos a S/ 9 cada uno y 3 empanadas a S/ 6 cada una. 
Con un cupón de 10 % de descuento sobre el total. Si paga con S/ 50, 
¿cuánto vuelto recibe?

Detalla el paso a paso e indica el monto al final.

"""
print("=============================")
print("MENSAJE_CoT:", MENSAJE_CoT)
print("-------------------")
print("RESULTADO:" ,preguntar(MENSAJE_CoT))
