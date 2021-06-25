'''
There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [from_i, to_i, price_i] indicates
that there is a flight from city fromi to city toi with cost price i.
You are also given three integers src, dst, and k, return the cheapest price from src to dst
with at most k stops. If there is no such route, return -1.
'''

def findCheapestPrice(n, flights, src, dst, k):
    W = []
    for i in range(n):
        W.append([])
        for j in range(n):
            if i == j:
                W[-1].append(0)
            else:
                W[-1].append(float('inf'))
    for flight in flights:
        W[flight[0]][flight[1]] = flight[2]
    D = [W]
    for K in range(1, k + 1):
        d = []
        for i in range(n):
            d.append([])
            for j in range(n):
                d[-1].append(min([D[-1][i][j], D[-1][i][K-1] + D[-1][K-1][j]]))
        D.append(d)
    return D[k]

# did not work
