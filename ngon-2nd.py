#!/usr/bin/env python3
#
# Number of ways to color edges of a n-gon using c colors, allowing only rotations
# Wolfgang Lauffher 2024

import sys

def nrOfDifferentColorings (EDGES,COLORS):
    CurrentColoring = [0 for i in range(EDGES)]
    Seen = set()
    unique_colorings=0


    def ColoringIsNew ():
        nonlocal Seen
        new=0

        for r in range(0,EDGES):  # Rotate Edges
            coloring=f"{CurrentColoring[r % EDGES]}"
            for e in range(r+1,EDGES+r):
                coloring=f"{coloring} {CurrentColoring[e % EDGES]}"
            if r==0 and coloring not in Seen:
                new=1
            Seen.add(coloring)

        return new


    def permutateEdges (edge=1):
        # this runs COLORS**EDGES times
        nonlocal CurrentColoring
        nonlocal unique_colorings

        for c in range(0,COLORS):
            CurrentColoring[edge-1]=c
            if edge < EDGES:
                permutateEdges(edge+1)
            unique_colorings+=ColoringIsNew()


    if EDGES > 0: permutateEdges()
    return unique_colorings


### MAIN ###

edges  = int(sys.argv[1]) if len(sys.argv) >= 2 else 1
colors = int(sys.argv[2]) if len(sys.argv) >= 3 else 1

print(f"Edges: {edges} Colors: {colors} Different Colorings: {nrOfDifferentColorings(edges,colors)}")

