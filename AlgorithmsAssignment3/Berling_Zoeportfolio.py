"""Berling Zoe Assignment3 Portfolio Optimization"""

# InvestmentName, InvestmentCost, EstimatedReturnOnInvestment

def loadInvestments(filename):
    """Takes in the investmentFilename and returns a list of possible investment options: name, cost, estimated return"""
    investments = []  # [name(2), cost(4), ereturn([4] * [9])]  # investments[2] list is the cost times the estimated return
    f = open(filename, "r")
    # Skip the first line since it is header info and USA info
    f.readline()
    f.readline()
    for investmentLine in f:
        investmentLine = investmentLine.split(",")
        # investments is a list of lists.  Each sublist is name, initial cost, and estimated 10 year return
        # print(investmentLine[2], investmentLine[4], investmentLine[9])
        investments.append(
            [investmentLine[2], int(investmentLine[4]), int(investmentLine[4]) * float(investmentLine[9])])

    # print("\nInvestments list:\n", investments)

    f.close()

    return investments


def optimizeInvestments(mylist, tot):
    """takes in list of possible investments along with the amount of money available to spend
    This function should return both the optimal return on investment amount as well as the actual investments selected
    to achieve this. Implement using Dynamic Programming"""
    rows = len(mylist)+1 # add one row for return on no investments
    # print(rows)
    col = tot + 1
    m = [[0 for i in range(col)] for j in range(rows)]  # optimal vlaue matrix
    t = [[False for i in range(col)] for j in range(rows)]  # traceback matrix
    for i in range(col):
        m[0][i] = 0
    for i in range(col):
        t[0][i] = False
    for co in range(1, len(mylist)+1): # iterate over each row (company)
        for amt in range(1, col):  # iterate over every price point
            if mylist[co-1][1] <= amt:
                # print(co,amt, mylist[co - 1][2] + m[co - 1][amt - mylist[co - 1][1]]< m[co - 1][amt])
                m[co][amt] = max(mylist[co - 1][2]
                              + m[co - 1][amt - mylist[co - 1][1]],
                              m[co - 1][amt])
                if m[co][amt] == m[co-1][amt]:
                    t[co][amt] = False
                else:
                    t[co][amt] = True
            else:
                m[co][amt] = m[co - 1][amt]
                t[co][amt] = False

    return m, t



investments = loadInvestments("zhvi-short.csv")
# investments = loadInvestments("state_zhvi_summary_allhomes.csv")
money = 15
m, t = optimizeInvestments(investments, money)

cash = []
while money > 0:
    for row in range(len(t)-1, -1, -1): # iterate over the rows in the traceback backwards
            if t[row][money] == True:
                cash.append(investments[row-1][0])
                money -= investments[row-1][1]

print("picked: ", cash)



