import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


class DataGrabber:
    def __init__(self, file_name):
        self.filename = file_name
        self.data = self.load_data()
        self.groups = self.get_groups("typ", "cena")

    def load_data(self):
        """
        Loads the data from the given path.
        """
        if self.filename.exists():
            data = pd.read_csv(self.filename)
            data = data.set_index(data.columns[0])
        else:
            data = pd.DataFrame(columns=["id", "typ", "cena"]).set_index("id")
        return data

    def plot_data(self, y_column="cena", pyplot=True):
        """
        Plots the data from the dataframe.
        """
        if pyplot:
            fig = plt.figure()
        else:
            fig = mpl.figure.Figure()
        ax = fig.add_subplot(111)
        ax.bar(self.data.index.values, self.data[y_column])
        return fig

    def get_groups(self, group_by="typ", param="cena"):
        """
        Returns a dictionary of the groups in the data.
        """
        if len(self.data) >= 1:
            grouped = self.data.groupby(by=group_by).sum()
            output = {}
            for idx, row in grouped.iterrows():
                output[idx] = row[param]
            return output
        else:
            return None

    def append_row(self, row):
        """
        Appends a row to the data.
        """
        self.data = self.data.append(row, ignore_index=True)
    
    def save_data(self):
        """
        Saves the data to the given path.
        """
        self.data.to_csv(self.filename)

