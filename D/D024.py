degreeA = int(input())
degreeB = int(input())

while True:
    if degreeA >= 1 and degreeA <= 179 and degreeB >= 1 and degreeB < 179 and  degreeA+degreeB<= 179 and degreeA+degreeB>=2:
        degreeAB = degreeA+degreeB
        break
    else:
        degreeA = int(input())
        degreeB = int(input())

print(int(180-degreeAB))