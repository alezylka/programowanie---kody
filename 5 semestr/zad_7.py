from sys import argv
import pandas as pd
import csv
import numpy as np

with open("5 semestr\dummy1.dat") as f:
    with open("filename.csv", "w") as f1:
        for line in f:
            df = f1.write(line)
        
        print(df)

