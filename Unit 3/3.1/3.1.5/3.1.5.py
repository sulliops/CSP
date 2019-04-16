import numpy as np
import matplotlib.pyplot as plt
def make_PLTW_style(axes):
    for item in ([axes.title, axes.xaxis.label, axes.yaxis.label] +
             axes.get_xticklabels() + axes.get_yticklabels()):
        item.set_family('Georgia')
        item.set_fontsize(16)
import os.path
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'household_size_feb14.csv')
datafile = open(filename,'r')
data = datafile.readlines()

householdSizes=[]
for line in data[3:]:
    age, householdSize = line.split(',')
    householdSizes.append(int(householdSize[1:-1]))
fig_householdSizes, ax  = plt.subplots(1, 1)
ax.hist(householdSizes, color='cyan', bins=100) 
ax.set_title('Average House Size in Feb 2014 U.S. Sample')
ax.set_xlabel('# of people living in house')
ax.set_ylabel('Frequency (# people)')
make_PLTW_style(ax)
fig_householdSizes.show()