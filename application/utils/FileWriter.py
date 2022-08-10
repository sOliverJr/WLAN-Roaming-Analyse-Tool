from datetime import datetime
import pandas as pd
import numpy as np


class FileWriter:
    responses = []
    date = datetime.today().strftime('%Y.%m.%d-%H:%M:%S')

    def add_response(self, element):
        self.responses.append(element)

    def write_responses(self):
        to_write = np.asarray(self.responses)
        pd.DataFrame(to_write).to_csv("logs/pings_" + self.date + ".csv", index_label="Index", header=['Date: ' + self.date])
        self.responses = []
        print('Wrote Array to file.')
