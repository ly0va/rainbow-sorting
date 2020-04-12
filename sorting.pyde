# vim: ft=python
from random import shuffle
from time import sleep
from algorithms import *

sorts = (
    cbubble,
    cshaker, 
    cinsertion,
    cshell,
    cmerge,
    cheap,
    cquick,
)

def setup():
    global m, coros, flags
    size(scl*n, scl*n)
    noStroke()
    colorMode(HSB, n)
    m = [list(range(0, n, step))*step for i in range(n)]
    k = len(sorts)
    coros = sum(([s(m[i]) for i in range(j*n//k, (j+1)*n//k)] 
                 for j, s in enumerate(sorts)), [])
    flags = [True]*n
    for row in m:
        shuffle(row)
        #row.reverse()
    
def draw():
    background(255)
    for i, row in enumerate(m):
        for j, cell in enumerate(row):
            fill(cell, n, n)
            rect(j*scl, i*scl, scl, scl)
    for i in range(n):
        if flags[i]:
            flags[i] = next(coros[i])
    if not any(flags):
        noLoop()
    sleep(time)

        

        
