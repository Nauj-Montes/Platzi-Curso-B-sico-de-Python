print(
    "\nBienvenido a mi programa de conversor de moneda\n Por favor, elija la moneda a convertir:\n [1] Dolares\n [2] Pesos Colombianos\n [3] Pesos Argentinos\n [4] Pesos Mexicanos\n")

# Valores de las monedas en dolares
pesos_col = 3940.22
pesos_ar = 106.47
pesos_mex = 20.38
moneda_text = ""

moneda = int(input("Escriba el número de la respectiva moneda: "))
if moneda >= and moneda <= 4:
    moneda_convertir = int(
        input("Elija el número de la moneda a la que quieres convertir a: "))
    if moneda_convertir == 1:
        moneda_text = "Dolares"
        print("\n")
        pass
    elif moneda_convertir == 2:
        moneda_text = "Pesos Colombianos"
        moneda_convertir = pesos_col
        print("\n")
    elif moneda_convertir == 3:
        moneda_text = "Pesos Argentinos"
        moneda_convertir = pesos_ar
        print("\n")
    else:
        moneda_text = "Pesos Mexicanos"
        moneda_convertir = pesos_mex
        print("\n")
else:
    print("Valor invalido, ejecute nuevamente el programa")
    exit()

dinero_cantidad = float(input("Cuánto dinero tienes?: "))

if moneda == 1:
    dinero_convertido = dinero_cantidad * moneda_convertir
    print("Su cantidad de dinero en " + moneda_text +
          " es de " + str(round(dinero_convertido, 2)))
elif moneda == 2:
    dinero_convertido = (dinero_cantidad / pesos_col) * moneda_convertir
    print("Su cantidad de dinero en " + moneda_text +
          " es de " + str(round(dinero_convertido, 2)))
elif moneda == 3:
    dinero_convertido = (dinero_cantidad / pesos_ar) * moneda_convertir
    print("Su cantidad de dinero en " + moneda_text +
          " es de " + str(round(dinero_convertido, 2)))
else:
    dinero_convertido = (dinero_cantidad / pesos_mex) * moneda_convertir
    print("Su cantidad de dinero en " + moneda_text +
          " es de " + str(round(dinero_convertido, 2)))
