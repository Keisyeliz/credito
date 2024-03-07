
porcentaje_creditoFlt = 0.60
tasa_interesFlt = 0.12  # Asumimos una tasa de interés del 12% anual

nombreStr = input('Nombre -> ')
salarioFlt = float(input('Salario -> '))
montoFlt = float(input('Monto -> '))
plazoInt = int(input('Plazo (en meses) -> '))

cap_descFlt = salarioFlt * porcentaje_creditoFlt
interesFlt = montoFlt * (tasa_interesFlt / 12) * plazoInt
tasa_interesmentFlt = montoFlt * (tasa_interesFlt / 12)
montoTotalFlt = montoFlt + interesFlt
cuotaFlt = montoTotalFlt / plazoInt

if cap_descFlt >= cuotaFlt:

    print('Crédito aprobado')
    print('Nombre del prestatario: ',nombreStr)
    print('Monto solicitado: ','$', montoFlt)
    print('Interés mensual: ','$',tasa_interesmentFlt)
    print('Interés total: ',' $ ',interesFlt)
    print('Monto total a pagar: ','$',montoTotalFlt)
    print('Cuota mensual: ', '$',cuotaFlt)

else:
    print('Crédito denegado')