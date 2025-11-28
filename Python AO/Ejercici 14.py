def convertir_base(numero: str, base_origen: int, base_destino: int) -> str:
    """
    Convierte un número desde base_origen a base_destino.
    Bases permitidas: 2 a 36.
    """
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if not (2 <= base_origen <= 36) or not (2 <= base_destino <= 36):
        raise ValueError("Las bases deben estar entre 2 y 36.")


    try:
        valor_decimal = int(numero, base_origen)
    except ValueError:
        raise ValueError(f"El número '{numero}' no es válido en la base {base_origen}.")


    if valor_decimal == 0:
        return "0"

    resultado = ""
    while valor_decimal > 0:
        valor_decimal, residuo = divmod(valor_decimal, base_destino)
        resultado = caracteres[residuo] + resultado

    return resultado


numero = input("Introduce el número: ")
base_origen = int(input("Introduce la base de origen: "))
base_destino = int(input("Introduce la base de destino: "))

try:
    resultado = convertir_base(numero.upper(), base_origen, base_destino)
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Error: {e}")
