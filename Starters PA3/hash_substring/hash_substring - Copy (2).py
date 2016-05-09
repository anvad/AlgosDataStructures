# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def get_hash(s, _prime, _multiplier):
    ans = 0
    for c in reversed(s):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans % self.bucket_count

def are_equal(s1, s2):
    if len(s1) != len(s2):
        return False
    lS = len(s1)
    for i in range(lS):
        if s1[i] != s2[i]:
            return False
    return True

def precompute_hashes(pattern, text, p, x):
    lT = len(text)
    lP = len(pattern)
    H = [None] * (lT - lP + 1)
    S = text[(lT - lP):]
    H[lT - lP] = get_hash(S, p, x)
    y = 1
    for i in range(lP):
        y = (y * x) % p
    for i in range(lT - lP - 1, 0, -1):
        H[i] = (x * H[i+1] + T[i] - y * T[i + lP]) % p
    return H
    
def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]
    x = 263
    p = 1000000007
    result = []
    pattern_hash = get_hash(pattern, p, x)
    H = precompute_hashes(pattern, text, p, x)
    for i in range(len(text) - len(pattern)):
        if pattern_hash != H[i]:
            continue
        if are_equal(pattern, text[i:i+pattern]):
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

