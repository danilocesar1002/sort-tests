import os
from sort import sortingAlgorithms
from test import Test


if __name__ == "__main__":
    path = os.getcwd() + "/test.txt"

    print("Este es un script de pruebas para algoritmos de ordenamiento.")
    print("Las pruebas pueden tomar varias horas.")
    print("Los resultados se guardarán en \"{0}\". Si el archivo ya existe,".format(path)
        + " su contenido será borrado y reemplazado.")
    
    while (inpt := input("¿Desea iniciar con las pruebas? (s/n): ")) != "n":
        if inpt == "s":
            testFile = open(path, "w")
            testFile.write("")
            testFile.close()

            tests = [Test(algorithm) for algorithm in sortingAlgorithms]
            for test in tests:
                test.test(path)
            break
        else:
            continue
