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

#Faltan las variables sobre festividades del año como DIA_TRABAJO etc

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
    if (a%4==0 and a%100!=0) or a%400==0:
        return True
    else:
        return False


def dias_mes(m,a):

    if es_bisiesto(a)==True and m==2:
        return DIAS_FEBRERO_BISIESTO

    else:
        return asoci[m]


def fecha_valida(d,m,a):
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
    if ((a1==a2) and (m1==m2) and (d1==d2)):
        return True
    else:
        return False



def dias_transcurridos(d,m,a):
    n = 0
    for i in range(1,m):
        n = n + dias_mes(i,a)
    n = int(n + d)
    return round(int(n))



def siglo(a):
    return int((a//100)+1)



def siglo_numeral_romano(a):
    return roman.toRoman(siglo(a))

print(dias_mes(2,2021))
