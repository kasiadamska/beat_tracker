import mir_eval
import os
import numpy as np

#Open ground truth file and delete second column to obtain 1D data
f = open('BallroomAnnotations-master/Albums-Cafe_Paradiso-05.txt', "r")
#Save 1D text files to a new folder
g = open("1DBallroomAnnotations/Albums-Cafe_Paradiso-05.txt", "w")

for line in f:
    if line.strip():
        g.write("\t".join(line.split()[:1]) + "\n")

f.close()
g.close()
#new reference beats file created

#load estimated_beats from beatTracker.py
estimated_beats = mir_eval.io.load_events('estimated_beats.txt')
#load 1D reference
reference_beats = mir_eval.io.load_events('1DBallroomAnnotations/Albums-Cafe_Paradiso-05.txt')

scores = mir_eval.beat.evaluate(reference_beats, estimated_beats)
print(scores)
