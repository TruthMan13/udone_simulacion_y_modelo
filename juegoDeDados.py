from random import randint


def Perder(fondo, apuesta):
    
    return fondo-apuesta

def Ganar(fondo, apuesta):
    
    return fondo+apuesta

def RollDado():
    return randint(1,2)

def Apostar(fondo, apuesta):
    tirada = RollDado()
    if (tirada%2)==0:
        
        return Ganar(fondo, apuesta)
    else:
        return Perder(fondo, apuesta)
    
def Play(fondo):
    apuesta = fondo
    ronda  = 0
    while (fondo > 0):
        ronda += 1
        resultado= Apostar(fondo, apuesta)
        fondo =resultado
    return ronda

def Simulacion(fondo, max)-> int:
    acumulador = 0
    for i in range(1,max):
        juego = Play(fondo)
        acumulador+=juego    

    return acumulador

def promedio(fondo, max):
    print(f'El promedio es de {Simulacion(fondo, max)/max}')

    



if __name__== "__main__":
    fondo_inicial=100
    max = 100
    promedio(fondo_inicial,max)