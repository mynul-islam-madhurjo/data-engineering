""" Create numpy array np_height_in that is equal to first column of np_baseball.
Print out the mean of np_height_in.
Print out the median of np_height_in."""
# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))


"""" The code to print out the mean height is already included. Complete the code for the median height. Replace None 
with the correct code. Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the 
correct code. Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and 
second column of np_baseball in corr. Replace None with the correct code."""


# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))



"""" Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions. 
Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for 
np_heights. Assign the result to gk_heights. Extract all the heights of all the other players. This time use 
np_positions != 'GK' as an index for np_heights. Assign the result to other_heights. Print out the median height of 
the goalkeepers using np.median(). Replace None with the correct code. Do the same for the other players. Print out 
their median height. Replace None with the correct code."""
# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))




