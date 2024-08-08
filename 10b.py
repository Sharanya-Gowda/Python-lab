import pandas as pd

def iris_dataset_operations():
    df = pd.read_csv('iris.csv')
    
    print("First 5 rows:")
    print(df.head())
    
    print("Last 5 rows:")
    print(df.tail())
    
    print("Dataset information:")
    print(df.info())
    
    print("Overview of each column:")
    print(df.describe())
    
    print("Plotting dataset:")
    df.plot()
    plt.show()

iris_dataset_operations()
