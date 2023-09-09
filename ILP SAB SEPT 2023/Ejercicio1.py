import datetime

fecha_actual = datetime.datetime.now()
fecha_nacimiento = input("Ingrese su fecha de nacimiento 'dd/mm/aaaa': ")

fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y').strftime('%d-%m-%Y')

edad = fecha_actual - fecha_nacimiento

print(edad)
