# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    #print("segments ", segments)
    #sortedEndSegments = sorted(segments, key=lambda s: s.end)
    sortedStartSegments = sorted(segments, key=lambda s: s.start, reverse=True)
    #print("sortedEndSegments ", sortedEndSegments)
    #print("sortedStartSegments ", sortedStartSegments)
    #iMax = len(sortedSegments)
    while len(sortedStartSegments) > 0:
       smin = min(sortedStartSegments, key=lambda s: s.end)
       p = smin.end
       points.append(p)
       while ( (len(sortedStartSegments) > 0) and (p >= sortedStartSegments[-1].start) ):
           s = sortedStartSegments.pop()
    
    #for s in segments:
    #    points.append(s.start)
    #    points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
