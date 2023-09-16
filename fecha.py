import roman

DIAS_ENERO=31

DIAS_MARZO=31

DIAS_MAYO=31

DIAS_JULIO=31

DIAS_AGOSTO=31

DIAS_OCTUBRE=31

DIAS_DICIEMBRE=31

DIAS_ABRIL=30

DIAS_JUNIO=30

DIAS_SEPTIEMBRE=30

DIAS_NOVIEMBRE=30

DIAS_FEBRERO=28

DIAS_FEBRERO_BISIESTO=29

asoci={1:DIAS_ENERO,2:DIAS_FEBRERO,3:DIAS_MARZO,4:DIAS_ABRIL,5:DIAS_MAYO,6:DIAS_JUNIO,7:DIAS_JULIO,8:DIAS_AGOSTO,9:DIAS_SEPTIEMBRE,10:DIAS_OCTUBRE,11:DIAS_NOVIEMBRE,12:DIAS_DICIEMBRE}

DIA_TRABAJO=1

MES_TRABAJO=5

DIA_NAVIDAD=24

MES_NAVIDAD=12

DIA_ANHO_NUEVO=1

MES_ANHO_NUEVO=1

DIA_FIN_ANHO=31

MES_FIN_ANHO=12

DIA_HALLOWEEN=31

MES_HALLOWEEN=10

def es_bisiesto(a):
    '''
    Determina si un año es bisiesto o no.

    :param a: Dato de tipo int que representa un año.
    :return: True en caso de que a sea bisiesto, False en caso contrario.
    '''
    if (a%4==0 and a%100!=0) or a%400==0:
        return True
    else:
        return False


def dias_mes(m,a):
    '''
    Retorna el número de días correspondientes al año y mes introducidos.

    :param m: Variable de tipo int que representa el número del mes (1-12).
    :param a: Variable de tipo int que representa el año.
    :return: Entero que representa cuantos días tiene cierto mes de cierto año.
    '''

    if es_bisiesto(a)==True and m==2:
        return DIAS_FEBRERO_BISIESTO

    else:
        return asoci[m]


def fecha_valida(d,m,a):
  '''
  Comprueba que una fecha sea válida.

  :param d: Entero que representa el día.
  :param m: Entero que representa el mes.
  :param a: Entero que representa el año.
  :return: True si la fecha es válida, False en caso contario.
  '''
  if es_bisiesto(a) and m==2:
    if d>0 and d<=29:
      return True
    else:
      return False

  else:
    if d>0 and d<=asoci[m]:
      return True

    else:
      return False



def es_posterior(d1,m1,a1,d2,m2,a2):
  '''
  Comprueba si el dia d1/m1/a1 ocurre/ocurrió/ocurrirá despues del día d2/m2/a2.

  :param d1: Entero que representa el día de la primera fecha.
  :param m1: Entero que representa el mes de la primera fecha.
  :param a1: Entero que representa el año de la primera fecha.
  :param d2: Entero que representa el día de la segunda fecha.
  :param m2: Entero que representa el mes de la segunda fecha.
  :param a2: Entero que representa el año de la segunda fecha.
  :return: True en caso de que la primera fecha sea posterior, False en caso contrario.
  '''
  if a1>a2:
    return True

  elif a1==a2:
    if m1>m2:
      return True

    elif m1==m2:
      if d1>d2:
        return True
      
      else:
        return False

    else:
      return False

  else: 
    return False



def es_anterior(d1,m1,a1,d2,m2,a2):
  '''
  Comprueba si el dia d1/m1/a1 ocurre/ocurrió/ocurrirá antes del día d2/m2/a2.

  :param d1: Entero que representa el día de la primera fecha.
  :param m1: Entero que representa el mes de la primera fecha.
  :param a1: Entero que representa el año de la primera fecha.
  :param d2: Entero que representa el día de la segunda fecha.
  :param m2: Entero que representa el mes de la segunda fecha.
  :param a2: Entero que representa el año de la segunda fecha.
  :return: True en caso de que la primera fecha sea anterior, False en caso contrario.
  '''
  if a1<a2:
    return True

  elif a1==a2:
    if m1<m2:
      return True

    elif m1==m2:
      if d1<d2:
        return True

      else:
        return False
    
    else:
      return False

  else:
    return False



def es_igual(d1,m1,a1,d2,m2,a2):
    '''
    Comprueba que una fecha sea igual a otra.

    :param d1: Entero que representa el día de la primera fecha.
    :param m1: Entero que representa el mes de la primera fecha.
    :param a1: Entero que representa el año de la primera fecha.
    :param d2: Entero que representa el día de la segunda fecha.
    :param m2: Entero que representa el mes de la segunda fecha.
    :param a2: Entero que representa el año de la segunda fecha.
    :return: True en caso de que la primera fecha sea igual a la segunda, False en caso contrario.
    '''
    if ((a1==a2) and (m1==m2) and (d1==d2)):
        return True
    else:
        return False



def dias_transcurridos(d,m,a):
    '''
    Calcula cuantos días han pasado desde el primero de Enero hasta la fecha introducida incluyéndola.

    :param d: Entero que representa el dia de la fecha introducida.
    :param m: Entero que representa el mes de la fecha introducida.
    :param a: Entero que representa el año de la fecha introducida.
    :return: Entero que representa el numero de días transcurridos.
    '''
    n = 0
    for i in range(1,m):
        n = n + dias_mes(i,a)
    n = int(n + d)
    return round(int(n))



def siglo(a):
    '''
    Indica cual es el siglo del año introducido.

    :param a: Entero que representa el año.
    :return: Entero que representa el siglo correspondiente al año a.
    '''
    return int((a//100)+1)



def siglo_numeral_romano(a):
    '''
    Devuelve el número en romano al que pertenece el año introducido.

    :param a: Entero que representa el año a evaluar.
    :return: String que representa el siglo en número romano.
    '''
    b=roman.toRoman(siglo(a))
    return b

