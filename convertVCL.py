from LogConvert import *
import sys
import glob
import argparse
from tqdm import tqdm

def convert_1_file(fname):
    LogConvert(fname).to_csv()

def convert_all_files(fpath):
    fnames = glob.glob(fpath+"/*.vcl")
    for fname in tqdm(fnames):
        try:
            LogConvert(fname).to_csv()
        except:
            print("="*30+"\nLogfile {} needs to be looked at manually\n".format(fname)+"="*30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Conversion tool from .vcl files to .csv for Oxford Instrument Dilution Refridgerators with Triton System')
    parser.add_argument('--file', type=str, help='convert the .vcl file argument (FILE) to .csv')
    parser.add_argument('--all', type=str, help='converts all files in the path argument (ALL)')

    args = parser.parse_args()
    if args.file:
        convert_1_file(args.file)
    elif args.all:
        convert_all_files(args.all)
    else:
        raise IOError()
