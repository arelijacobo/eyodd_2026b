# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # O(n)

def random_function(students):
    first = students[0] # O(1)
    total = 0 # O(1)
    new_list = [] # O(1)

    for student in students: # O(n)
        total += 1 # O(1)
        new_list.append(student) # O(1)

    print(new_list) # O(n)
    return total # O(1)

print(random_function(student_list_01)) # O(n)

# Calcular O(n)