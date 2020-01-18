import sys
import time
from marraige_org import Marriage1

fp = open("chapel2.txt", 'r')
lines = fp.readlines()

# Call the closest_pair function passing in the
# contents of the file
start = time.time()
m = Marriage1()
print(m.compute(lines))
print(m.getLukePath())
print(m.getLorelaiPath())
end = time.time()
print("time: "+ str(end-start))