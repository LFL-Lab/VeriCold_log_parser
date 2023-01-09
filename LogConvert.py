import pandas as pd
import sys, os
from log_parser import parse

class LogConvert:

    def __init__(self, file_name):
        self.file_path = file_name
        self.name = self.get_formatted_name()
        self.titles, self.data = self.get_data()

    def get_formatted_name(self):
        name = os.path.split(self.file_path)[1].replace("vcl","csv")
        fpath = os.path.split(self.file_path)[0]
        if sys.platform == "win32":
            try:
                save_path = fpath+r"\\data_csv\\"
                try:
                    os.makedirs(save_path)
                except:
                    pass
                name = save_path + name
            except:
                raise SystemError()
        else:
            save_path = fpath+r"/data_csv/"
            try:
                os.makedirs(save_path)
            except:
                pass
            name = save_path + name

        return name

    def get_data(self):
        if not self.file_path:
            raise ValueError()
        try:
            titles, data = parse(self.file_path)
        except (IOError, RuntimeError) as ex:
            print(' '.join(repr(a) for a in ex.args))
        return titles, data

    def get_df(self) -> bool:
        df = pd.DataFrame(self.data.T)
        df.columns = self.titles
        return df

    def to_csv(self) -> bool:
        df = self.get_df()
        df.to_csv(self.name, index=False)
        print("{} has been generated!".format(self.name))

