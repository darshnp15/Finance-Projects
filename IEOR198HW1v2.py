import random

"""
One player is the maker and the other is the taker. They agree on a width beforehand, such as 10.
The taker generates a random integer between 1 and 100 inclusive (so each number has a 1% chance of appearing).
This number is the true value of the contract. The taker sees the true value; the maker does not.
There are ten rounds of action. What is the width at which neither player has an advantage? This is hard!
"""

takerPnLAvgarray = []
makerPnLAvgarray = []
trueValAvgarray = []

widthTestRange = 4

for k in range(0,widthTestRange):
    takerPnLarray = []
    makerPnLarray = []
    trueValarray = []

    width = 12 + k

    # A million runs is more than enough to find a statistically signficiant result
    for j in range(0,1000000):
        takerPnL = 0
        makerPnL = 0
        mid = 50

        trueVal = random.randrange(0,101,1)
        # Use the following comment to test specific scenarios
        # trueVal = 33

        for i in range(0,10):
            if mid > trueVal:
                roundPnL1 = (mid-(width/2)-trueVal)
                takerPnL = takerPnL + roundPnL1
                makerPnL = makerPnL - roundPnL1
                # The following print statement is used for closer inspection of a singular game
                # print("Sold! | Mid: ", mid, " | Price: ", mid-(width/2), " | PnL: ", roundPnL1)

                if roundPnL1 > 0 and mid-width > 0:
                    mid = mid - width
                elif roundPnL1 > 0  and mid-width <= 0:
                    mid = 0
                else:
                    mid = mid

            else:
                roundPnL2 = (trueVal-(mid+(width/2)))
                takerPnL = takerPnL + roundPnL2
                makerPnL = makerPnL - roundPnL2
                # The following print statement is used for closer inspection of a singular game
                # print("Take! | Mid: ", mid, " | Price: ", mid+(width/2), " | PnL: ", roundPnL2)

                if roundPnL2 > 0 and mid+width < 100:
                    mid = mid + width
                elif roundPnL2 > 0  and mid+width >= 100:
                    mid = 100
                else:
                    mid = mid
                
        # The following print statement is used for closer inspection of a singular game
        # print(takerPnL, " | ", makerPnL)
        takerPnLarray.append(takerPnL)
        makerPnLarray.append(makerPnL)
        trueValarray.append(trueVal)

    trueValAvgarray.append(sum(trueValarray)/len(trueValarray))
    takerPnLAvgarray.append(sum(takerPnLarray)/len(takerPnLarray))
    makerPnLAvgarray.append(sum(makerPnLarray)/len(makerPnLarray))

for i in range(0,widthTestRange):
    print("========================================")
    print("True Value: ", trueValAvgarray[i])
    print("Width: ", 10+i)
    print("Taker Avg PnL: ", takerPnLAvgarray[i])
    print("Maker Avg PnL: ", makerPnLAvgarray[i])
print("========================================")