import  requests


#Conexion con API, obteniendo los valores del json y convertirlos a diccionario
url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
request_get = requests.get(url)
data = dict(request_get.json())
#Variables
data_items = data['items']
cont = 0


class Proccess:

    #se genera la funcion anwers para calcular las respuestas contestadas y no contestadas
    def anwers(data_set,cont,value):
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)):
            # se genera la condicion si el valor es verdadero se incrementa contador
            if data_set[i][value]:
                cont += 1
        # se realiza una resta del valor de la data con el contador para obtner la no contestadas
        result = len(data_set) - cont
        # se returna el valor
        return f'Repuestas\nContestadas : {cont}\nNo contestadas : {result}'

    # se genera la funcion minor_view para obtener la respuesta con menor vistas
    def minor_views(data_set,cont,value):
        #se genera una variable de referencia
        data_reference = data_set[0]['view_count']
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)):
            #se genera una variable para realizar la comparacion
            data = data_set[i][value]
            #se genera condicion si el valor de la data es menor al valor de la data que tomamos como referencia
            #se actualiza y tome ese valor como el nuevo valor de referencia
            if data < data_reference:
                data_reference = data
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont = i
        # se returnan los valores
        return f'Menor Vista\nRespuesta n.: {cont}\nNumero de vistas : {data_reference}'

    # se genera la funcion anwers_hold_new para obtener la respuesta mas vieja y mas nueva
    def anwers_hold_new(data_set,cont,value):
        # se generan dos varibles que tienen el mismo valor
        anwers_new = anwers_hold = data_set[0][value]
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)) :
            #se genera una variable de referencia
            data_reference = data_set[i][value]
            # se genera la condicion indicando que si el valor de la data es mayor al de referencia
            # se actualiza y tome ese valor como el nuevo valor de referencia
            if data_reference > anwers_hold:
                anwers_hold = data_reference
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont = i
            # se genera la condicion en dado caso de que no es mayor y es menor la compare con la de referencia y si es menor
            # que se actualice y tome ese valor como el nuevo valor de referencia
            elif data_reference < anwers_new:
                anwers_new = data_reference
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont1 = i
        # se returnan los valores
        return f'Respuesta\nMas vieja : {cont}  = {anwers_hold}\nMas Nueva : {cont1}  = {anwers_new}'

    # se genera la funcion elderly_reputation para obtener la respuesta con mas reputacion
    def elderly_reputation(data_set,cont,value_1,value_2):
        #se genera una variable con 0
        reply = 0
        # se genera un ciclo for tomando como rango el valor de la data
        for i in range(len(data_set)):
            # se genera un try except para saber si existe ese valor en el diccionario, si no existe le da un valor de 0
            try:
                value = data_set[i][value_1][value_2]
            except:
                value = 0
            # se genera la condicion indicando que si el valor de value es mayor al de reply
            # se actualiza y toma ese valor como el nuevo
            if value > reply:
                reply = value
                # se genero un contador tomando como refencia i para imprimir el numero de la respuesta
                cont = i
        # se returnan los valores
        return f'Mayor Reputacion\nRespuesta n.: {cont}\nReputacion : {reply}'


    def print_range(data_set,num1,num2):
        # se genera un ciclo for tomando como rango el valor num1 y num2
        for i in range(num1,num2):
            # se imprimen los valores que estan dentro del rango
            print(f'{i} : {data_set[i]}')

if __name__ == '__main__':
    print(Proccess.anwers(data_items,cont,'is_answered'))
    print(Proccess.minor_views(data_items,cont,'view_count'))
    print(Proccess.anwers_hold_new(data_items,cont,'creation_date'))
    print(Proccess.elderly_reputation(data_items,cont,'owner','reputation'))
    Proccess.print_range(data_items,2,6)