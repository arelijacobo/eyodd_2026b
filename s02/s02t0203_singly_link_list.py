# Importando clase Nodo
from s02t0201_linked_list import Node 

# 1 Creo funcion principal
def main():
    # 2. Coloco el codigo ejecutable
    test_node = Node("Prueba")
    print (f"Valor del nodo: {test_node.data}")

# Evaluo del valor de __name__
if __name__ == "__main__":
    main()