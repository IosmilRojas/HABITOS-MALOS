def AreaRectangulo(Largo, Ancho):
    result = Largo * Ancho
    return result

def AreaTriangulo(Base, Altura):
     r = 0.5 * Base * Altura
     return r

def principal():
    Largo = 4
    Ancho = 6
    print("Área del rectángulo:", AreaRectangulo(Largo, Ancho))

    base = 5
    altura = 8

    print("Área del triángulo:", AreaTriangulo(base, altura))

principal()
