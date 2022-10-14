import nemo.collections.asr as nemo_asr
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--input_csv', type=str, default='examples/example_input.csv',
                    help='path to your csv file')
args = parser.parse_args()


def main(args):
    print('Load ASR model')
    asr_model = nemo_asr.models.EncDecCTCModel.restore_from('checkpoint/My_model.nemo')
    print('Load Done')

    data = pd.read_csv(args.input_csv, sep = '|')

    print('Start recognition')
    transcript_numbers = asr_model.transcribe(data['path'])
    print('Recognized')

    data['transcribe'] = transcript_numbers
    data.to_csv('examples/transcribe_numbers.csv', index=False, sep='|')

if __name__ == "__main__":
    main(args)
