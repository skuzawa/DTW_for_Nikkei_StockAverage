def dtw(ts_a,ts_b):
    ts_a_len = len(ts_a)
    ts_b_len = len(ts_b)
    row=ts_a_len
    col=ts_b_len
    cost=[[0 for i in range(col)] for j in range(row)]
    dist=[[0 for i in range(col)] for j in range(row)]
    cost[0][0]=abs(ts_a[0]-ts_b[0])
    dist[0][0]=cost[0][0]
    window=max(ts_a_len,ts_b_len)
    for i in range(1,ts_a_len):
        cost[i][0] = abs(ts_a[i]-ts_b[0])
        dist[i][0] = dist[i-1][0] + cost[i][0]
    for j in range(1,ts_b_len):
        cost[0][j] = abs(ts_a[0]-ts_b[j])
        dist[0][j] = dist[0][j-1] + cost[0][j]
    for i in range(1,ts_a_len):
        window_start = max(1, i - window)
        window_end = min(ts_b_len, i + window)
        for j in range(window_start,window_end):
            choices = min(dist[i-1][j], min(dist[i][j-1], dist[i-1][j-1]))
            cost[i][j] =abs(ts_a[i]-ts_b[j])
            dist[i][j] = choices + cost[i][j]
        
    print(dist[row-1][col-1])

a=[]
b=[]
f=open("comp1.txt","r")
for line in f.readlines():
    date,value=line.split()
    a.append(float(value))
g=open("comp2.txt","r")
for line in g.readlines():
    date,value=line.split()
    b.append(float(value))

dtw(a,b)
    
