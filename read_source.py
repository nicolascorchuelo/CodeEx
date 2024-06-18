import pandas as pd
import json
from common import config

class FileReader:
    """ Read files from a path"""

    def __init__(self,filemame) -> None:
        self.filename = filemame

    def read_and_process_file(self):
        with open(self.filename, 'r') as f:
            data = [json.loads(line) for line in f]

        df = pd.DataFrame(data)
        return df

    def read_csv_file(self):
        return pd.read_csv(self.filename)