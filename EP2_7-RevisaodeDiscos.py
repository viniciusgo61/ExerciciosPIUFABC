def requer_revisao(ano, motor, distancia):
    if (1901 <= ano <= 2000) and (motor == 100 or motor == 101):
        return True
    elif 2001 <= ano <= 2020 and distancia > 5000:
        return True
    elif ano == 2021 and (motor == 200 or motor == 201) and distancia > 200:
        return True
    else:
        return False

ano_producao = int(input("Ano de produção do disco voador: "))
motor_principal = int(input("Código do motor principal: "))
distancia_percorrida = int(input("Distância percorrida em anos-luz: "))

if requer_revisao(ano_producao, motor_principal, distancia_percorrida):
    print("SIM")
else:
    print("NAO")