# Array
# from array import *
import array as arr

# Creacion de un arreglo
# i: Entero con signo
# I: Entero sin signo
# f: Numero decimal
# d: Numero decimal doble
# u: Carácteres unicode
my_array = arr.array ('i',[10,22,300,3,7,
40,55,80,700,654,3])

# Interacion automatica 
#for num in my_array:
    #print(num)

# Acceso individual a los elementos 
#print(my_array[0]) # Primer elemento
#print(my_array[1]) # Segundo elemento
#print(my_array[2]) # Tercer elemento


# Tamaño de un arreglo
# Length
# #print(len(my_array))

# Interación por indices
#for i in range(len(my_array)):
    #print(f"Elemento {i+1}: {my_array[i]}")
    #if my_array[i] % 2 == 0:
        #print(f"Elemento Num {i+1}:{my_array[i]}")    

# Busqueda de un elemento
num_to_search = 200

3 #Modificando un valor
# Bracket notation
my_array[7] = 200

try:
    print(f"Localizando {num_to_search}: {my_array.index
    (num_to_search)}")
except:
    print("⚠️ Numero no encontrado !!!")

# Asignando el valor en un indice que no existe
try:
    my_array[100] = 3
except:
    print("⚠️ Indice no existe !!!")