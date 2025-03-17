import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 10

    print("Los Chiwiwiiss....")
    print("Adivina un número entre 1 y 100. Tienes solo 10 intentos.")

    while intentos < max_intentos:
        try:
            intento = int(input(f"Intento {intentos + 1}/{max_intentos}: Ingresa un número: "))
            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue

            intentos += 1

            if intento == numero_secreto:
                print(f"Ojoo Piojooo Adivinaste el número en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Ingresa un número entero.")

    else:
        print(f"Perdiste :( El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivina_el_numero()
