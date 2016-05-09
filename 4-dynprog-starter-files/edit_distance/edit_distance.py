# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    edit_dist = []
    #for i in range(m):
    #    edit_dist.append([i]) #filling the 0th column
    for i in range(m+1):
        edit_dist.append([i]) #filling the 0th column
        for j in range(1,n+1):
            if i > 0:
                right = edit_dist[i][j-1] + 1
                down = edit_dist[i-1][j] + 1
                if (s[i-1] == t[j-1]):
                    diag = edit_dist[i-1][j-1]
                else:
                    diag = edit_dist[i-1][j-1] + 1
                edit_dist[i].append(min(right, down, diag))
            else:
                edit_dist[i].append(j) #0th row
    
    return edit_dist[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
