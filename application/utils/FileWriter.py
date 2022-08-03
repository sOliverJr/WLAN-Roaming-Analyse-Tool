from datetime import datetime
import pandas as pd
import numpy as np


class FileWriter:
    responses = []

    def add_response(self, element):
        self.responses.append(element)

    def get_responses(self):
        return self.responses

    def write_responses(self):
        to_write = np.asarray(self.responses)
        pd.DataFrame(to_write).to_csv("logs/pings.csv", index_label="Index", header=['Date: ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S')])
        self.responses = []
        print('Wrote Array to file.')
