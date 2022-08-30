"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    input_file = open('./data.csv', 'r').readlines()
    sum = 0
    for row in input_file:
        row = row.replace('\t', '')
        sum += int(row[1])

    return sum



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict = {}

    for row in input_file:
        row = row.replace('\t', '')
        
        if row[0] not in dict: dict[row[0]] = 1
        else: dict[row[0]] += 1

    letters = list(dict.items())
    letters.sort(key = lambda x: x[0])
    
    return letters


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict_final = {'A': 0, 'B':0, 'C':0, 'D':0, 'E':0}

    for letter in dict_final:
        for row in input_file:
            row = row.replace('\t', '')

            if row[0] == letter:
                dict_final[letter] += int(row[1])

    return list(dict_final.items())



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict_months = {}

    for row in input_file:
        row = row.split('\t')
        date = row[2].split('-')
        
        if date[1] not in dict_months: dict_months[date[1]] = 1
        else: dict_months[date[1]] += 1

    months = list(dict_months.items())
    months.sort(key = lambda x: x[0])

    return months
    

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict_final = {'A':[0,11], 'B':[0,11], 'C':[0,11], 'D':[0,11], 'E':[0,11]}

    for row in input_file:
        row = row.replace('\t', '')
        
        letter = row[0]
        dict_final[letter][0] = max(dict_final[letter][0], int(row[1]))
        dict_final[letter][1] = min(dict_final[letter][1], int(row[1]))

    return dict_final


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict_passwords = {}

    for row in input_file:
        row = row.split('\t')
        
        passwords = row[4].replace('\n', '').split(',')
        
        for password in passwords:
            aux = password.split(':')
            key = aux[0]
            value = int(aux[1])

            if key not in dict_passwords:
                dict_passwords[key] = [11, 0]
                dict_passwords[key][0] = min(dict_passwords[key][0], value)
                dict_passwords[key][1] = max(dict_passwords[key][1], value)
            else:
                dict_passwords[key][0] = min(dict_passwords[key][0], value)
                dict_passwords[key][1] = max(dict_passwords[key][1], value)

    result = list(dict_passwords.items())
    result.sort(key = lambda x: x[0])

    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

    for row in input_file:
        row = row.split('\t')

        dict[int(row[1])].append(row[0])

    result = list(dict.items())
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    input_file = open('./data.csv', 'r').readlines()
    dict = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

    for row in input_file:
        row = row.split('\t')

        if row[0] not in dict[int(row[1])]:
            dict[int(row[1])].append(row[0])

    for i in dict:
        dict[i] = sorted(dict[i])

    result = list(dict.items())
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    input_file = open('./data.csv', 'r').readlines()
    dic = {}

    for row in input_file:
        row = row.split('\t')
        passwords = row[4].replace('\n', '').split(',')
        
        for password in passwords:
            aux = password.split(':')
            key = aux[0]

            if key not in dic: dic[key] = 1
            else: dic[key] += 1

    l = list(dic.items())
    l.sort()

    result = {k:v for k,v in l}
    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    input_file = open('./data.csv', 'r').readlines()
    result = []

    for row in input_file:
        row = row.split('\t')
        
        len_row_4 = len(row[3].split(','))
        len_row_5 = len(row[4].split(','))

        el = [0,0,0]
        el[0] = row[0]
        el[1] = len_row_4
        el[2] = len_row_5

        result.append(el)

    for i in range(len(result)):
        result[i] = tuple(result[i])

    return result


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    input_file = open('./data.csv', 'r').readlines()
    dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0}

    for row in input_file:
        row = row.split('\t')
        
        
        for i in row[3].split(','):
            dict[i] += int(row[1])

    return dict


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    input_file = open('./data.csv', 'r').readlines()
    dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0}

    for row in input_file:
        row = row.split('\t')

        for i in row[4].split(','):
            dict[row[0]] += int(i.split(':')[1])

    return dict
