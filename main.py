from clases.jugador import Jugador
from clases.enemigo import Enemigo
import random


def main():
    nombre_jugador = input(
        "Bienvenido a la aventura en la tierra media, por favor identificate: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Orco", 50, 10),
        Enemigo("Troll", 70, 7),
        Enemigo("Ciclope", 80, 15),
    ]
    enemigos_derrotados=[]

    print("Comienza la Aventura!")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue

        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud>0:
            accion= input("Que deseas hacer? (atacar/huir)").lower()

            if accion=="atacar":
                dano_jugador=jugador.atacar()
                print(f"Has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)
                if enemigo_actual.salud >0:
                    dano_enemigo=enemigo_actual.atacar()
                    print(f"El {enemigo_actual.nombre} te ataco y te causó {dano_enemigo} de daño")
                    jugador.recibir_dano(dano_enemigo)
                    jugador.ganar_experiencia(random.randint(15,25))
            elif accion=="huir":
                print("Has decidido huir del combate")
                jugador.descansar()
                break
        if jugador.salud <=0:
            print("Has sido derrotado!")
            break
        if enemigo_actual.salud <=0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        continuar= input("Quieres seguir explorando? (s/n)").lower()
        print(continuar)

        if continuar != "s":
            print("Gracias por jugar Tierra Media")
            break
    if not enemigos:
        print("Felicidades has derrotado a todos los enemigos")

if __name__ == "__main__": #nos asegura que solo podremos ejecutar este script desde el programa principal
    main()