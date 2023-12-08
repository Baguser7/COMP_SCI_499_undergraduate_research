import pandas as pd
import matplotlib.pyplot as plt

def calculate_column_averages(csv_file, column_names):
 # Read the CSV file into a DataFrame, skipping the header
    df = pd.read_csv(csv_file, header=None, skiprows=1, names=column_names, encoding='latin-1')

    # Calculate the averages for each specified column
    average_values = {column: df[column].mean() for column in column_names}

    return average_values

def show_comparison_bar_chart(average_values):
    # Create a bar chart for the comparison of average values
    columns = list(average_values.keys())
    values = list(average_values.values())

    plt.bar(columns, values)
    plt.xlabel('Columns')
    plt.ylabel('Average Values')
    plt.title('Comparison of Average Values')
    plt.show()

# Example usage
csv_file_path = r'COMP_SCI_499_undergraduate_research\artificial_intelligence\dataset\data_raw\score_10_2.csv'
columns_to_average = ['base-tiny', 'base-google', 'base-houndify']  # Replace with the actual column names

average_results = calculate_column_averages(csv_file_path, columns_to_average)

for column, average_value in average_results.items():
    print(f'The average of column "{column}" is: {average_value}')

show_comparison_bar_chart(average_results)
