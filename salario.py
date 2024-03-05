porcentaje_creditoFlt = 0.60
nombreStr = input('Nombre -> ')
salariofLt = float(input('Salario -> '))
montoFlt =float(input('Monto -> '))
plazoInt = int(input('Plazo -> '))

cap_descFlt = salariofLt * porcentaje_creditoFlt
cuotaFlt = montoFlt / plazoInt

if cap_descFlt >= cuotaFlt:
    print('Credito aprobado')
else:
    print('Credito denegado')