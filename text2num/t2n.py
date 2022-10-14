# +
from text_to_num import text2num
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--output_csv', type=str, default='example_output.csv',
                    help='name for save output csv')

args = parser.parse_args()

def t2n(transcribe):
    return text2num(transcribe, 'ru')


def main(args):
    data = pd.read_csv('../examples/transcribe_numbers.csv', sep = '|')

    data['digit'] = data['transcribe'].apply(t2n)
    data = data.drop(['transcribe'], axis=1)

    data.to_csv(f'../examples/{args.output_csv}', index=False, sep='|')

if __name__ == "__main__":
    main(args)
