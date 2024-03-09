# reloj.py
# (c) 2024, Jose Enrique Alvarez
# Programa que pasa de segundos a horas, minutos y segundos

tiempo = 153869

# 1 día tiene 86400 segundos, 24 horas de 3600 segundos c/u
dias = tiempo // 86400
tiempo = tiempo % 86400

# 1 hora tiene 3600 segundos, 60 minutos de 60 segundos cada uno
# 60 x 60 = 3600
horas = tiempo // 3600
tiempo = tiempo % 3600

# 1 minuto tiene 60 segundos
minutos = tiempo // 60
tiempo = tiempo % 60

print("dd: ", dias, " hh: ", horas, " mm: ", minutos, " ss: ", tiempo)
