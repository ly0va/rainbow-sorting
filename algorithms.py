n = 105
step = 1
scl = 6
time = 0.02

def cshell(a):
    dlist = (301, 132, 57, 23, 10, 4, 1)
    #dlist = (255, 127, 63, 31, 15, 7, 3, 1)
    for d in dlist:
        for i in range(n):
            j = i
            while j >= d and a[j] < a[j-d]:
                a[j], a[j-d] = a[j-d], a[j]
                j -= d
                yield True
    yield False

def cheap(a):
    def sift(i, j):
        while True:
            big = i
            for c in (2*i+1, 2*i+2):
                if c < j and a[c] > a[big]:
                    big = c
            if big == i: break
            a[i], a[big] = a[big], a[i]
            i = big
            yield
    for i in range(n//2-1, -1, -1):
        for j in sift(i, n):
            yield True
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        yield True
        for j in sift(0, i):
            yield True
    yield False

def cshaker(a):
    flag = False
    right = n-1
    left = 0
    while not flag:
        flag = True
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = False
                right = j
            yield True
        for i in range(right, left, -1):
            if a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]
                flag = False
                left = i
            yield True
    yield False

def cbubble(a):
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            yield True
    yield False

def cinsertion(a):
    for i in range(1, n):
        j = i-1
        while a[j] > a[j+1] and j >= 0:
            a[j+1], a[j] = a[j], a[j+1]
            j -= 1
            yield True
    yield False

def cmerge(a):
    unit = 1
    while unit < n:
        for h in range(0, n, unit*2):
            p, q, r = h, h+unit, min(n, h+unit*2)
            while p < q < r:
                if a[p] > a[q]:
                    a[p], a[p+1:q+1] = a[q], a[p:q]
                    q += 1
                p += 1
                yield True
        unit *= 2
    yield False

def cquick(a):
    def qsort(left, right):
        i, j = left, right
        comp = a[(left + right)//2]
        while i < j:
            while a[i] < comp: i += 1
            while a[j] > comp: j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i, j = i+1, j-1
            yield
        if left < j:
            for k in qsort(left, j): yield
        if right > i:
            for k in qsort(i, right): yield
    for k in qsort(0, n-1):
        yield True
    yield False
