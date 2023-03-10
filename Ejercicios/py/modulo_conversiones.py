"""
Módulo en Python que implementa las siguientes conversiones:
    - Segundos a minutos: recibe segundos y retorna minutos y segundos
    - Segundos a horas: recibe segundos y retorna horas, minutos y segundos
    - Minutos a segundos: recibe minutos y segundos y retorna segundos
    - Minutos a horas: recibe minutos y segundos y retorna horas, minutos y segundos

Author: Darío Huallpa
"""
SEGUNDOS_POR_MINUTO = 60
MINUTOS_POR_HORA = 60


def segundos_a_minutos(segundos):
    """
    Función que convierte segundos a minutos
    :param: segundos
    :return: minutos
    """
    mins = segundos // SEGUNDOS_POR_MINUTO
    segs = segundos % SEGUNDOS_POR_MINUTO
    return mins, segs


def minutos_a_segundos(minutos, segundos):
    segs = minutos * SEGUNDOS_POR_MINUTO + segundos
    return segs


def minutos_a_horas(minutos, segundos=0):
    """
    Convierte la cantidad de minutos y segundos a horas, minutos y segundos
    :param minutos:
    :param segundos: (default 0)
    :return: horas, minutos, segundos
    """
    hrs = minutos // MINUTOS_POR_HORA
    mins = minutos % MINUTOS_POR_HORA
    segs = segundos
    return hrs, mins, segs


def segundos_a_horas(segundos):
    mins, segs = segundos_a_minutos(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)
    return hrs, mins, segs
