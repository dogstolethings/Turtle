"""Plot Adjusted Closeing price"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    """Return the mean volume for stock indicated by symbol.
    
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/AAPL.csv")
    print df['Adj Close']
    df['Adj Close'].plot()
    plt.show() # must be called to show plots
 


if __name__ == "__main__":
    test_run()

    

