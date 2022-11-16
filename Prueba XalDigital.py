#Librerias

import  requests



class Procces:
    #Conexion con API, obteniendo los valores del json y convertirlos a diccionario
    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
    request_get = requests.get(url)
    data = dict(request_get.json())

    #Variables Globales
    global data_items,data_views,cont
    data_items = data['items']
    data_views = data_items[0]['view_count']
    cont = 0

    #se genera la funcion anwers para calcular las respuestas contestadas y no contestadas
    def anwers(data_set,cont):
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)):
            # se genera la condicion si el valor es verdadero se incrementa contador
            if data_set[i]['is_answered']:
                cont += 1
        # se realiza una resta del valor de la data con el contador para obtner la no contestadas
        result = len(data_set) - cont
        # se returna el valor
        return f'Repuestas\nContestadas : {cont}\nNo contestadas : {result}'

    # se genera la funcion minor_view para obtener la respuesta con menor vistas
    def minor_views(data_set,data_set2,cont):
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)):
            #se genera condicion si el valor de la data es menor al valor de la data que tomamos como referencia
            #se actualiza y tome ese valor como el nuevo valor de referencia
            if data_set[i]['view_count'] < data_set2:
                data_set2 = data_set[i]['view_count']
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont = i
        # se returnan los valores
        return f'Menor Vista\nRespuesta n.: {cont}\nNumero de vistas :  {data_set2}'

    # se genera la funcion anwers_hold_new para obtener la respuesta mas vieja y mas nueva
    def anwers_hold_new(data_set,cont):
        # se generan dos varibles que tienen el mismo valor
        anwers_new = anwers_hold = data_set[0]['creation_date']
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)) :
            # se genera la condicion indicando que si el valor de la data es mayor al de referencia
            # se actualiza y tome ese valor como el nuevo valor de referencia
            if data_set[i]['creation_date'] > anwers_hold:
                anwers_hold = data_set[i]['creation_date']
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont = i
            # se genera la condicion en dado caso de que no es mayor y es menor la compare con la de referencia y si es menor
            # que se actualice y tome ese valor como el nuevo valor de referencia
            elif data_set[i]['creation_date'] < anwers_new:
                anwers_new = data_set[i]['creation_date']
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont1 = i
        # se returnan los valores
        return f'Respuesta\nMas vieja : {cont}  = {anwers_hold}\nMas Nueva : {cont1}  = {anwers_new}'

    # se genera la funcion elderly_reputation para obtener la respuesta con mas reputacion
    def elderly_reputation(data_set,data_set2):
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)):
            # se genera la condicion indicando que si el valor de la data es mayor al de referencia
            # se actualiza y tome ese valor como el nuevo valor de referencia
            if data_set[i]['owner']['reputation'] > data_set2:
                data_set2 = data_set[i]['owner']['reputation']
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont = i
        # se returnan los valores
        return f'Mayor Reputacion\nRespuesta n.: {cont}\nReputacion : {data_set2}'


    def impresion(data_set,num1,num2):
        # se genera un ciclo for tomando como rango el valor num1 y num2
        for i in range(num1,num2):
            # se imprimen los valores que estan dentro del rango
            print(f'{i} : {data_set[i]}')

if __name__ == '__main__':
    print(Procces.anwers(data_items,cont))
    print(Procces.minor_views(data_items,data_views,cont))
    print(Procces.anwers_hold_new(data_items,cont))
    print(Procces.elderly_reputation(data_items,data_views))
    Procces.impresion(data_items,2,6)