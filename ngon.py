#!/usr/bin/python3

# Number of ways to color edges of a n-gon using c colors, allowing only rotations
# Wolfgang Lauffher 2024

import sys

COLORINGS=0
Color = []
Seen = set()

def find_unique_colorings (edges):
    global Color
    global Seen
    global COLORINGS
    global COLORS, EDGES
    edges-=1
    for c in range(0,COLORS):
        Color[edges]=c
        if edges <= 0:
            counted_within_this_rotation=0
            for r in range(0,EDGES):
                colors="#"
                for e in range(r,EDGES+r):
                    colors=f"{colors} {Color[e % EDGES]}"
                if colors not in Seen and not counted_within_this_rotation: COLORINGS+=1
                Seen.add(colors)
                counted_within_this_rotation=1
        else:
            find_unique_colorings(edges)

# MAIN
EDGES=1
COLORS=1

if len(sys.argv) >= 2:
    EDGES=int(sys.argv[1])
if len(sys.argv) >= 3:
    COLORS=int(sys.argv[2])

for i in range(EDGES): Color.append(0)
find_unique_colorings(EDGES)

print(f"Edges: {EDGES} Colors: {COLORS} Unique Colorings: {COLORINGS}")

