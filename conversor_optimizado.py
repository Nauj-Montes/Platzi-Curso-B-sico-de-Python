print(
    """Bienvenido a mi programa de conversor de moneda😏🤑.
    
    Por favor, elija la moneda a convertir:
    [1] Dolares
    [2] Pesos Colombianos
    [3] Pesos Argentinos
    [4] Pesos Mexicanos\n""")


def conversion(nombre, valor_usd, valor_usd_final):
    dinero_convertido = str(
        round(((dinero_cantidad / valor_usd) * valor_usd_final), 2))
    return print("\n Su cantidad de dinero en " + nombre + " es de " + str(dinero_convertido))


def valor_usd(valor):
    switch = {
        1: 1,
        2: 3940.22,
        3: 106.47,
        4: 20.38,
    }
    return switch.get(valor)


moneda_inicial = int(input("Escriba el número de la respectiva moneda: "))
moneda_convertir = int(
    input("\nElija el número de la moneda a la que quieres convertir a: "))


if moneda_inicial in range(1, 5) and moneda_convertir in range(1, 5):
    dinero_cantidad = float(input("\n¿Cuántos dinero tienes?: "))

    if moneda_inicial == 1:
        conversion("Dolares Americanos", valor_usd(
            moneda_inicial), valor_usd(moneda_convertir))
    elif moneda_inicial == 2:
        conversion("Pesos Colombianos", valor_usd(
            moneda_inicial), valor_usd(moneda_convertir))
    elif moneda_inicial == 3:
        conversion("Pesos Argentinos", valor_usd(
            moneda_inicial), valor_usd(moneda_convertir))
    else:
        conversion("Pesos Mexicanos", valor_usd(
            moneda_inicial), valor_usd(moneda_convertir))
else:
    print("Valor invalido, ejecute nuevamente el programa")
    exit()
