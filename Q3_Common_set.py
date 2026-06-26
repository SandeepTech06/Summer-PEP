def getMaxProfit(pnl, k):
    net_profit = pnl[0]

    for i in range(len(pnl)):
        s = 0
        for j in range(i, min(i + k, len(pnl))):
            s += pnl[j]

            if s > net_profit:
                net_profit = s
    return net_profit


pnl = [4, 3, -2, -9, -4, 2, 7]
k = 6

print(getMaxProfit(pnl, k))