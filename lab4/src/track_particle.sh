#!/bin/bash/
#this will run track_particle.py and then delete all "0 feature" images and run track_particle.py again
python track_particle.py > outfile; cat outfile | grep " 0 f" | cut -d' ' -f4 | cut -d':' -f1 | awk '{ print ($0 + 1)}' | xargs printf "%07d\n" | sed 's/\(.*\)/output\1.png/' | xargs rm ; rm outfile trajectory.csv; python track_particle.py; rm *.png
