# ♡ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ Problem 1 Main ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ
# Decided to organise the problem into tasks for clarity and ease of debugging.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd  # Pandas for data handling
import matplotlib.pyplot as plt  # Matplotlib for plotting
import numpy as np  # NumPy for numerical calculations

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 1: Read The database~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Loading data
data_a = pd.read_csv('targetA.csv')  # TargetA is assigned to data_a
data_b = pd.read_csv('targetB.csv')  # TargetB is assigned to data_b

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 2: Plotting Graphs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(data_a.head())  # Preview data structure
# Extracting sequence numbers from 'Info' column
data_a['Sequence'] = data_a['Info'].str.extract(r'Seq=(\d+)', expand=False).astype(
    int)  # extracts sequence numbers from
# a column named 'Info' in the DataFrame data_a and assigns these extracted numbers to a new column named 'Sequence'.
print(data_a[['Time', 'Sequence']].head())  # This line is used to print the first few rows of the data_a DataFrame,
# but only for the columns Time and Sequence. It's a way to quickly inspect and verify that the data has been loaded
# correctly and that the sequence numbers have been properly extracted and assigned.

# Sequence numbers over time
plt.figure(figsize=(10, 6))
plt.plot(data_a['Time'], data_a['Sequence'], marker='.', linestyle='none', color='thistle')
plt.xlabel('Time')
plt.ylabel('Sequence Number')
plt.title('Figure 1: Sequence Numbers Over Time')
plt.grid(True)
plt.show()

# Frequency of packet lengths as a probability distribution
packet_length_counts = data_a['Length'].value_counts(normalize=True)  # Count & normalize packet lengths
plt.figure(figsize=(10, 6))  # Set figure size to 10x6 inches
packet_length_counts.sort_index().plot(kind='line', color='darkgreen')  # Plot packet lengths as a sorted line chart
plt.xlabel('Packet Length')  # Label x-axis
plt.ylabel('Probability')  # Label y-axis
plt.title('Figure 2: Probability of Packet Lengths')  # Set chart title
plt.grid(True)
plt.show()  # Display the plot


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TASK 3: Statistical Analysis~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3.1 Calculating mean of packet lengths
mean_length = data_a['Length'].mean()
print(f"Mean Packet Length: {mean_length}")

# Calculating mode of packet lengths
mode_length = data_a['Length'].mode()[0]
print(f"Mode Packet Length: {mode_length}")

# 3.2 Calculating standard deviation of packet lengths
std_dev_length = data_a['Length'].std()
print(f"Standard Deviation of Packet Length: {std_dev_length}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 4: Plot Distribution of Packet Lengths~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Calculating and plotting CDF
packet_lengths = data_a['Length']  # Extract packet lengths into a separate variable
sorted_data = np.sort(packet_lengths)  # Sort packet lengths for accurate CDF calculation as CDF requires ordered data
cdf = np.arange(len(sorted_data)) / float(len(sorted_data))  # Calculate CDF values, representing cumulative probability

# Plotting CDF and PDF on separate graphs in the same window
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

# CDF
ax1.plot(sorted_data, cdf, linestyle='-', color='thistle')
ax1.set_title('Figure 3: Cumulative Disribution of Packet Lengths')
ax1.set_xlabel('Packet Length')
ax1.set_ylabel('CDF')
ax1.grid(True)

# PDF
ax2.hist(packet_lengths, bins=30, density=True, alpha=0.6, color='darkgreen')
ax2.set_title('Figure 4: Probability Density Function of Packet Lengths')
ax2.set_xlabel('Packet Length')
ax2.set_ylabel('Density')
ax2.grid(True)

plt.tight_layout()  # Optimizes the layout to prevent overlap of plot elements
plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 5: Calculate and Plot Packet Delays~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extracting sequence numbers from 'Info' column
data_b['Sequence'] = data_b['Info'].str.extract(r'Seq=(\d+)', expand=False).astype(int)

# Sorting and merging data for delay calculation
data_a_sorted = data_a.sort_values(by='Sequence')
data_b_sorted = data_b.sort_values(by='Sequence')
merged_data = pd.merge(data_a_sorted, data_b_sorted, on='Sequence', suffixes=('_A', '_B'))  # Merge sorted datasets on
# 'Sequence' number to match
# corresponding packets between A and B.
merged_data['Delay'] = merged_data['Time_B'] - merged_data['Time_A']  # Calculate the delay for each packet by
# subtracting Time_A from Time_B.

unique_data_target_a = data_a.drop_duplicates(subset=['Sequence'], keep='first')
unique_data_target_b = data_b.drop_duplicates(subset=['Sequence'], keep='first')

# Merge the unique dataframes on the sequence number to calculate delays
unique_merged_df = pd.merge(unique_data_target_a[['Sequence', 'Time']], unique_data_target_b[['Sequence', 'Time']],
                            on='Sequence', suffixes=('_A', '_B'))

# Calculate delay
unique_merged_df['Delay'] = unique_merged_df['Time_B'] - unique_merged_df['Time_A']


# Plotting the delays
plt.figure(figsize=(10, 6))
plt.plot(unique_merged_df['Sequence'], unique_merged_df['Delay'], marker='o', linestyle='', markersize=2,
         color='thistle')
plt.title('Figure 5: Packet Delay from Node A to Node B')
plt.xlabel('Sequence Number')
plt.ylabel('Delay (seconds)')
plt.grid(True)
plt.show()