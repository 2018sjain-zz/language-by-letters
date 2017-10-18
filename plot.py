import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = open("third.txt", "r").read().split(']')[:-1]

x_points = []
y_points = []
z_points = []

for each in data[:250]:
	nums = re.findall('\d+', each)
	x_points.append(int(nums[0]))
	y_points.append(int(nums[1]))
	z_points.append(int(nums[2]))

ax.scatter(x_points, y_points, z_points)
ax.set_xlabel('Single Letter')
ax.set_ylabel('Double Letter')
ax.set_zlabel('Triple Letter')

plt.show()