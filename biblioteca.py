


def piramide(nmr):
    for i in range(nmr+1):
        for x in range(i):
            print(i, end=" ")
        print()

#essav atv tem outras duas extensoes.

def piramidde2(nmr):
    for x in range(1,nmr+2):
        for y in range(1, x+1):
            print(y,end= " ")
        print()