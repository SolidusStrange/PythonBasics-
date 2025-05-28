for num in range(1, 11):  # Bucle externo: va del 1 al 10 (tablas del 1 al 10)
    print(f"Tabla de multiplicar del {num} hasta el 10: ", end="")
    for mult in range(1, 11):  # Bucle interno: multiplica el número actual por 1 hasta 10
        resultado = num * mult
        print(f"{resultado} ", end="")  # Imprime en la misma línea
    print()  # Salto de línea después de terminar cada tabla
    