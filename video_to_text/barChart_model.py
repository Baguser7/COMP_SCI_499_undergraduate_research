import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV file
csv_file = 'your_data.csv'  # Replace 'your_data.csv' with the actual file name
data = pd.read_csv(csv_file)

# Extract data
methods = data['Method']
values = data[['Value1', 'Value2', 'Value3', 'Value4', 'Value5', 'Value6', 'Value7', 'Value8', 'Value9']]

# Set up bar positions
bar_width = 0.2
bar_positions = np.arange(len(methods))

# Create grouped bar chart
for i in range(0, len(values.columns), 3):
    plt.bar(bar_positions + i * bar_width, values.iloc[:, i:i+3].values.T.flatten(), width=bar_width, label=f'Values {i+1}-{i+3}')

# Set chart labels and title
plt.xlabel('Methods')
plt.ylabel('Values')
plt.title('Comparison of Values for Different Methods')

# Set method labels
plt.xticks(bar_positions + (len(values.columns)//6) * bar_width, methods)

# Display legend
plt.legend()

# Show the plot
plt.show()
