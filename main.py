import os
from sort import (
    insertionSort,
    mergeSort,
    countingSort,
    heapSort,
    quickSort
)
from test import test


def makeTest(filePath, sortingAlgorithms, starters, deltas, measures):
    assert(len(sortingAlgorithms) == len(starters) == len(deltas) == len(measures))
    # Runs the tests and saves them in filePath (assumes is a file path string)
    testFile = open(filePath, "w")
    testFile.write("")
    testFile.close()
    
    for i in range(len(deltas)):
        test(filePath, sortingAlgorithms[i], n=starters[i], dn=deltas[i], measure=measures[i], timeLimit=2)

def main():
    path = os.getcwd() + "/test.txt"

    print("Este es un script de pruebas para algoritmos de ordenamiento.")
    print("Las pruebas pueden tomar varias horas.")
    print("Los resultados se guardarán en \"{0}\". Si el archivo ya existe,".format(path)
        + " su contenido será borrado y reemplazado.")
    
    while (inpt := input("¿Desea iniciar con las pruebas? (s/n): ")) != "n":
        if inpt == "s":
            makeTest(
                path,
                [insertionSort, mergeSort, countingSort, heapSort, quickSort],
                [1] * 5,
                [1] * 5,
                ["median"] * 5
            )
            break
        else:
            continue


if __name__ == "__main__":
    main()
