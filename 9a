import pandas as pd
import matplotlib.pyplot as plt

def pandas_visualization():
    df = pd.read_csv('dataset.csv')
    print("Dataset:")
    print(df.head())

    print("Plotting dataset:")
    df.plot()
    plt.show()

    print("Scatter plot for a column:")
    df.plot.scatter(x='column1', y='column2')
    plt.show()

    print("Histogram for a column:")
    df['column1'].plot.hist()
    plt.show()

pandas_visualization()
