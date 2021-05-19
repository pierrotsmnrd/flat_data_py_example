import sys
import pandas as pd
import numpy as np

# Simple script to show the parameters sent to the script, and generate a dummy file

if __name__ == "__main__":

    print("argv :", sys.argv)

    df = pd.DataFrame(np.random.randint(
        0, 100, size=(10, 4)), columns=list('ABCD'))

    df.to_csv("df_output.csv")
