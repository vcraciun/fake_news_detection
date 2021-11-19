import argparse
import glob
import os
import time

from googletrans import Translator


def loop_translation(target_file_path):
    for loop in range(3):
        try:
            return translator.translate(open(target_file_path, 'rt', encoding='utf-8', errors='ignore').read(),
                                        src='en',
                                        dest='ro')
        except Exception as exception:
            print(str(exception))
        time.sleep(1)
    return None


parser = argparse.ArgumentParser(description='Athos article translator')
parser.add_argument(
    '--in_dir',
    type=str,
    default='data_en_split',
    required=False,
)
parser.add_argument(
    '--out_dir',
    type=str,
    default='data_ro',
    required=False,
)

args = parser.parse_args()

if not os.path.exists(args.out_dir):
    os.makedirs(args.out_dir)

txt_files_en = glob.glob("data_en_split/*.txt")

translator = Translator()
result = translator.translate('veritas lux mea', src='en', dest='ro')

translator.raise_Exception = True

counter = 0
for file_path in txt_files_en:
    print(f'processing: {file_path}')

    out = loop_translation(file_path)
    if out is not None:
        file_out = open(f'{args.out_dir}/{os.path.basename(file_path)}', 'wt', encoding='utf-8', errors='ignore')
        file_out.write(out.text)
        file_out.close()
    else:
        print('Failed to translate file {0}. Will continue.'.format(str(file_path)))
    time.sleep(1)

    counter += 1
    if counter == 100000:
        break
