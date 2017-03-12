'''
Instrucciones del manejo de la libreria

1. Funcion que recibe el punto y lo devuelve trasladado con respecto al punto de origen
    Recibe el centro, y el punto que desea convertir
    Cart(centro,punto)
    RETORNA (X,Y)

2. Funcion que dibuja el plano cartesiano
    Recibe el ancho, alto y el nombre de la ventana
    PlanoCartesiano(ANCHO, ALTO, pantalla)

3. Funcion que dibuja una linea
    linea(pantalla, color, [puntoInicial], [puntoFinal])

4. Funcion que dibuja un poligono
    poligono(pantalla, color, ListaPuntos)

5. Funcion de escalamiento (agranda la figura segun el valor de S)
    escalar(punto, s_escalar) -> [s_x, s_y]
    RETORNA (X,Y)

6. Funcion de Rotacion respecto a un punto (d)
    rotacionPunto(punto, d, theta) ->
        Punto que desea rotar
        d -> con respecto a que punto desea rotar
        theta -> el angulo de rotacion
        RETORNA (X,Y)

7. Funcion de Rotacion con respecto al plano
    rotacionPlano(punto, theta)
    (no rota con respecto a ningun punto)
    RETORNA (X,Y)

'''
