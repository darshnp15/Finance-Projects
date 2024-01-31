def kelly(w, l, a, b):
    return w/a - l/b

perB = kelly(0.5,0.5,1,1.4)
perC = kelly(0.5,0.5,0.8,1.2)
perD = kelly(0.5,0.5,0.5,0.9)
perA = 1 - perB - perC - perD
# perA = 1 - perC - perD

expVal = perA*1.1 + perC*((0.2+2.3)/2) + perD*((0.5+2)/2)

varX = 0.25*(((1.1*perA+0.2*perC+0.5*perD)-expVal)**2 + ((1.1*perA+2.3*perC+0.5*perD)-expVal)**2 + ((1.1*perA+0.2*perC+2*perD)-expVal)**2 + ((1.1*perA+2.3*perC+2*perD)-expVal)**2)

print(perA, " | ", perB, " | ", perC, " | ", perD)