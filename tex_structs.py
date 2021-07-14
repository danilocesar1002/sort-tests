from sort import (
    siftDown
)


def log2Floor(n):
    res = 1
    while (n >> res) > 0:
        res += 1
    
    return res - 1

# put a lot of strings into a figure
def finalString(procedure):
    return "\n\n".join(["\\begin{{figure}}[H]\n\\centering\n{}\n\n({})\n\\end{{figure}}".format(procedure[i], i + 1) for i in range(len(procedure))])

# take a heap (array coded) and convert it to TeX
def heapToTeX(arr,
             heapSize = -1,
             config="[scale=0.7,heapnode/.style={circle, draw=black, very thick}" + 
             ",arraynode/.style={circle, draw=black, fill=black!20, very thick}]"
             ):
    if heapSize == -1:
        heapSize = len(arr)
    
    assert len(arr) > 0
    assert 0 <= heapSize <= len(arr)


    coords = [[0, log2Floor(len(arr))]] + [None for _ in range(len(arr) - 1)]
    for i in range(len(arr) // 2):
        left, right = i * 2 + 1, i * 2 + 2
        siblingDistance = 2 ** (coords[i][1] - 1)

        if left < len(arr):
            coords[left] = [
                coords[i][0] - siblingDistance,
                coords[i][1] - 1
            ]
        if right < len(arr):
            coords[right] = [
                coords[i][0] + siblingDistance,
                coords[i][1] - 1    
            ]

    heapNodes = ["\\node[heapnode] ({}) at ({}, {}) {{{}}};".format(i, coords[i][0], coords[i][1], arr[i]) for i in range(heapSize)]
    arrayNodes = ["\\node[arraynode] ({}) at ({}, {}) {{{}}};".format(i, coords[i][0], coords[i][1], arr[i]) for i in range(heapSize, len(arr))]
    nodes = heapNodes + arrayNodes

    lines = []
    for i in range(len(arr) // 2):
        left, right = i * 2 + 1, i * 2 + 2
        if left < heapSize:
            lines.append("({}) edge ({})".format(i, left))
        if right < heapSize:
            lines.append("({}) edge ({})".format(i, right))


    return  "\\begin{{tikzpicture}}{}\n{}\n{}\n\\end{{tikzpicture}}".format(config, "\n".join(nodes), "\\draw\n" + "\n".join(lines) + ";")


def TeXHeapSort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        siftDown(arr, len(arr), i)

    procedure = [heapToTeX(arr, len(arr))]

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        siftDown(arr, i, 0)
        procedure.append(heapToTeX(arr, i))
    
    return finalString(procedure)


def TeXSiftDown(arr, length, parent):
    procedure = [heapToTeX(arr, length)]
    stack = [parent]

    while len(stack) > 0:
        #recicled from siftDown
        i = stack.pop()
        maxIndex = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < length and arr[left] > arr[maxIndex]:
            maxIndex = left
        if right < length and arr[right] > arr[maxIndex]:
            maxIndex = right

        if i != maxIndex:
            arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
            procedure.append(heapToTeX(arr, length))
            stack.append(maxIndex)
    
    return procedure


def TeXExtractMax(arr):
    procedure = [heapToTeX(arr)]
    arr[0], arr[-1] = arr[-1], arr[0]
    
    procedure += TeXSiftDown(arr, len(arr) - 1, 0)
    return finalString(procedure)


def TeXAddHeapKey(arr, key):
    procedure = [heapToTeX(arr)]
    arr.append(key)

    i = len(arr) - 1
    while i > 0:
        parent = (i - 1) // 2
        if arr[parent] >= arr[i]:
            break
        # else...
        procedure.append(heapToTeX(arr))
        arr[i], arr[parent] = arr[parent], arr[i]
        i = parent
    
    procedure.append(heapToTeX(arr))
    return finalString(procedure)




# Take a step from a Partition procedure (from quickSort) and convert it to TeX
def TeXPartitionString(arr, i, j, left, right):
    assert len(arr) > 0
    colors = [None for _ in range(len(arr))]

    if j == right + 1:
        for k in range(len(arr)):
            if left > k or k > right:
                colors[k] = "yellow!30"
            elif left <= k < i:
                colors[k] = "green!30"
            elif k == i and not i == j == -1:
                colors[k] = "gray!30"
            elif i < k <= right:
                colors[k] = "red!30"
            else:
                colors[k] = "white"
    else:
        for k in range(len(arr)):
            if   k == right and not i == j == -1:
                colors[k] = "gray!30"
            elif left > k or k > right:
                colors[k] = "yellow!30"
            elif left <= k <= i:
                colors[k] = "green!30"
            elif i < k <= j:
                colors[k] = "red!30"
            else:
                colors[k] = "white"


    string = "\\begin{{tabular}}{{{}}}\n\\hline\n".format("|l"*len(arr) + "|")

    for k in range(len(arr)):
        string += "\\cellcolor{{{}}}{} &\n".format(colors[k], arr[k])
    
    string = string[:-2] +  "\\\\ \n\\hline\n"
    string += "\\end{tabular}"

    return string


def TeXPartition(arr, left, right):
    procedure = [TeXPartitionString(arr,-1,-1, left, right)]

    x = arr[right]
    i = left - 1
    
    for j in range(left, right):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        procedure.append(TeXPartitionString(arr, i, j, left, right))
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    procedure.append(TeXPartitionString(arr, i + 1, right + 1, left, right))
    
    return (i + 1, procedure)


def TeXQuickSort(arr):
    stack = [(0, len(arr) - 1)]
    procedure = [TeXPartitionString(arr, -1, -1, 0, len(arr) - 1)]
    
    while len(stack) > 0:
        left, right = stack.pop()
        pivot, subProcedure = TeXPartition(arr, left, right)

        #procedure += subProcedure[1:]
        procedure.append(subProcedure[-1])
        
        if pivot + 1 < right:
            stack.append((pivot + 1, right))
        if left < pivot - 1:
            stack.append((left, pivot - 1))
    
    procedure.append(TeXPartitionString(arr, -1, -1, 0, len(arr) - 1))

    return finalString(procedure)

# aux function for TeXCountingSort
def TeXCountingSortArray(A=[], B=[], C=[]):
    res = ""

    x = [A,B,C]
    names = "ABC"

    for i in range(3):
        arr = x[i]
        if len(arr) == 0:
            continue

        string = "$" + names[i] + "$\n"
        string += "\\begin{{tabular}}{{{}}}\n\\hline\n".format("|l"*len(arr) + "|")
        colors = ["gray!40" if element == "" else "gray!5" for element in arr]

        for k in range(len(arr)):
            string += "\\cellcolor{{{}}}{} &\n".format(colors[k], arr[k])
        
        string = string[:-2] +  "\\\\ \n\\hline\n"
        string += "\\end{tabular}"
        
        res += string
        if i != 2:
            res += "\n\n\\hfill\n\n"
        else:
            res += "\n"

    return res

# Counting sort in TeX, just like an example in Cormen's book
def TeXCountingSort(arr):
    leftLimit, rightLimit = min(arr), max(arr)
    procedure = []

    freqs = [0] * (rightLimit - leftLimit + 1)
    ordered = [""] * len(arr)

    for i in range(len(arr)):
        freqs[arr[i] - leftLimit] += 1
    procedure.append(TeXCountingSortArray(A=arr, C=freqs))
    
    for i in range(1, len(freqs)):
        freqs[i] += freqs[i - 1]
    procedure.append(TeXCountingSortArray(C=freqs))

    for i in range(len(arr) - 1, -1, -1):
        ordered[freqs[arr[i] - leftLimit] - 1] = arr[i]
        freqs[arr[i] - leftLimit] -= 1

        procedure.append(TeXCountingSortArray(B=ordered, C=freqs))
    
    return finalString(procedure)


def TeXRadixSort(arr):
    procedure = []
    
    for i in range(len(arr[0]) - 1, -1, -1):
        arr.sort(key = lambda x: x[i])

        string = "\\begin{{tabular}}{{{}}}\n\\hline\n".format("|l"*len(arr) + "|")

        for k in range(len(arr)):
            string += "\\scalebox{{0.6}}{{{}}} &\n".format(arr[k])
        
        string = string[:-2] +  "\\\\ \n\\hline\n"
        string += "\\end{tabular}"

        procedure.append(string)

    return finalString(procedure)
