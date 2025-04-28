#1. Using Airthmetic Operators for Power
THICKNESS = 0.00008

folded_thickness = THICKNESS * (2**43)

thickness_km = folded_thickness / 1000 / 1000000

print("Thickness: {: .2f} million kilometers" .format(thickness_km))

#2. Using for loop
THICKNESS = 0.00008

folded_thickness = THICKNESS

for _ in range(43):
    folded_thickness *= 2

thickness_km = folded_thickness / 1000 / 1000000

print("Thickness: {: .2f} million kilometers" .format(thickness_km))

#3. Comparing execution time of the two methods
import time

start = time.time()
folded_thickness = THICKNESS * (2 ** 43)
elapsed_time = time.time() - start
print("Using Arithmetic Operator time: {:.8f} seconds".format(elapsed_time))

start = time.time()
folded_thickness = THICKNESS
for _ in range(43):
    folded_thickness *= 2

elapsed_time = time.time() - start
print("Using for Loop Time: {:.8f} seconds".format(elapsed_time))

#4. Recording and visualizing in a graph
import matplotlib.pyplot as plt

THICKNESS = 0.00008
folded_thickness = [THICKNESS]
for _ in range(43):
    THICKNESS *= 2
    folded_thickness.append(THICKNESS)

plt.title("Thickness of Folded Paper")
plt.xlabel("Number of folds")
plt.ylabel("Thickness [m]")
plt.plot(folded_thickness)
plt.show()

#5. Customizing the graph
plt.title("Thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("Thickness[m]")
plt.tick_params(labelsize=20)
plt.plot(folded_thickness, color='red', linewidth=2, linestyle='dotted')
plt.show()
