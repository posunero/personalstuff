def solve(zips, flights):
    # construct graph
    graph = [[False for y in zips] for x in zips]
    for t in flights:
        line = t.strip().split()
        a, b = int(line[0]), int(line[1])
        graph[a-1][b-1] = True
        graph[b-1][a-1] = True
    print(graph)
    # start at lowest zip
    lowest = [i for i, j in enumerate(zips) if j==min(zips)]
    return graph[lowest[0]]

def main():
    i = open('testsales.in')
    out = open('out.txt', 'w')

    lines = i.readlines()
    cases = int(lines[0])
    lines = lines[1:]

    for x in range(cases):
        nm = lines[0].strip().split()
        n, m = int(nm[0]), int(nm[1])
        zips = [int(x) for x in lines[1:n+1]]
        print(zips)
        flights = lines[n+1:n+m+1]
        print(flights)
        rv = solve(zips, flights)
        print(rv)

        lines = lines[n+m+1:]

if __name__ == '__main__':
    main()
