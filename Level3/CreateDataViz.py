"""Build a tool that takes a dataset and
generates interactive visualizations using
libraries such as Matplotlib, Seaborn, or
Plotly. This task will enhance their
understanding of data visualization principles
and plotting techniques."""

import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df):
    # Example: Plotting a bar chart for a specific column
    plt.figure(figsize=(10, 6))
    df['column_name'].value_counts().plot(kind='bar')
    plt.title('Bar Chart of Column Name')
    plt.xlabel('Categories')
    plt.ylabel('Counts')
    plt.show()
def main():
    try:
        df = pd.read_csv("H:\Cognifyz\Level3\sample.csv")
        print("Dataset loaded successfully.")
        print(df.head())
        visualize_data(df)
    except FileNotFoundError:
        print("The specified dataset file was not found.")
    except pd.errors.EmptyDataError:
        print("The dataset file is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()