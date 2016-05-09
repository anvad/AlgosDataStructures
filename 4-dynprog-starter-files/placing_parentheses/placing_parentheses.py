# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max_recursive_naive_slow(dataset, i, j):
    if i == j:
        return (int(dataset[i]),int(dataset[j]))
    m = float("infinity")
    M = float("-infinity")
    for k in range(i+1, j, 2): #k is the operation index... so it goes as odd numbers. i and j are number indices, so they go as even numbers
        m_left,M_left = min_max(dataset, i, k-1) #i.e. the expression to the left of the operator
        m_right,M_right = min_max(dataset, k+1, j) #i.e. the expression to the right of the operator
        opk = dataset[k]
        a = evalt(m_left, m_right, opk)
        b = evalt(m_left, M_right, opk)
        c = evalt(M_left, m_right, opk)
        d = evalt(M_left, M_right, opk)
        m = min(m, a, b, c, d)
        M = max(M, a, b, c, d)
    return (m, M)

#notice, this is still recursive.. except i am storing and looking up intermediate results, vs re-computing them each time
def min_max_dyn(dataset, i, j, mM):
    if i == j:
        return (int(dataset[i]),int(dataset[j]))
    key = str(i) + "_" + str(j)
    if key in mM:
        return mM[key]

    m = float("infinity")
    M = float("-infinity")
    for k in range(i+1, j, 2): #k is the operation index... so it goes as odd numbers. i and j are number indices, so they go as even numbers
        m_left,M_left = min_max_dyn(dataset, i, k-1, mM) #i.e. the expression to the left of the operator
        m_right,M_right = min_max_dyn(dataset, k+1, j, mM) #i.e. the expression to the right of the operator
        opk = dataset[k]
        a = evalt(m_left, m_right, opk)
        b = evalt(m_left, M_right, opk)
        c = evalt(M_left, m_right, opk)
        d = evalt(M_left, M_right, opk)
        m = min(m, a, b, c, d)
        M = max(M, a, b, c, d)
    mM[key] = (m, M)
    return (m, M)
def get_maximum_value(dataset):
    #write your code here
    #m,M = min_max_recursive_naive_slow(dataset, 0, len(dataset)-1)
    #num_digits = (len(dataset)-1)/2
    #mM = []
    #for i in num_digits:
    #    mM.append
    mM = {}
    m,M = min_max_dyn(dataset, 0, len(dataset)-1, mM)
    return M


if __name__ == "__main__":
    print(get_maximum_value(input()))
