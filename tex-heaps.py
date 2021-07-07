from sort import (
    siftDown
)

def log2Floor(n):
    res = 1
    while (n >> res) > 0:
        res += 1
    
    return res - 1


def heapToTeX(arr,
             heapSize = -1,
             config="[scale=0.7,heapnode/.style={circle, draw=black, very thick}" + 
             ",arraynode/.style={circle, draw=black, fill=black!20, very thick}]"
             ):
    assert len(arr) > 0
    assert 0 <= heapSize <= len(arr)
    if heapSize == -1:
        heapSize = len(arr)


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


    return  "\\begin{{tikzpicture}}{}{}\n{}\n\\end{{tikzpicture}}".format(config, "\n".join(nodes), "\\draw\n" + "\n".join(lines) + ";")


def TeXHeapSort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        siftDown(arr, len(arr), i)

    procedure = [heapToTeX(arr, len(arr))]

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        procedure.append(heapToTeX(arr, i))
        siftDown(arr, i, 0)
    
    return "\n\n".join(["\\begin{{figure}}[H]\n\\centering\n{}\n\n({})\n\\end{{figure}}".format(procedure[i], i + 1) for i in range(len(procedure))])
