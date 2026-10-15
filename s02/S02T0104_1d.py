from array import array as arr

# importar una funcion de otro
# archivo
from s02t0102_1d import print_array

my_array = arr('i', [2, 10, 15, 20, 10])

print("--- ANTES DE LA INSERCION ---")
print_array(my_array)

# Eliminación
try:
        my_array.remove(100)
except:
 print("NO SE ENCUENTRA EN EL ARREGLO")
print("--- DESPUES DE LA ELIMINACION ---")
print_array(my_array)
