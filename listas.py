# Programa para entender las listas en Python
# v 0.1
# (c) 2024, José Enrique Álvarez

l = [1,2,3,5,7,11,13]

longitud = len(l)

print("La longitud de l=", longitud)
for i in l:
    print(i)
l.append(17)
print("La nueva longitud de l=", len(l))
for i in l:
    print(i)