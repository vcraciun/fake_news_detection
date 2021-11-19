import argparse
import glob
import os

parser = argparse.ArgumentParser(description='Document splitter')
parser.add_argument(
    '--in_dir',
    type=str,
    default='stiri',
    required=False,
)
parser.add_argument(
    '--out_dir',
    type=str,
    default='data_en_split',
    required=False,
)

args = parser.parse_args()

if not os.path.exists(args.out_dir):
    os.makedirs(args.out_dir)

txt_files_en = glob.glob(f"{args.in_dir}/*.txt")


def process_file(file_path_arg):
    content = open(file_path_arg, 'rt', encoding='utf8', errors='ignore').readlines()

    buffer = ''
    counter = 0
    for line in content:
        buffer += line
        if len(buffer) > 1000:
            file_out = open(f'{args.out_dir}/{os.path.basename(file_path_arg)}.{counter:03d}.txt', 'wt', encoding="utf-8")
            file_out.write(buffer)
            file_out.close()
            buffer = ''
            counter += 1

    file_out = open(f'{args.out_dir}/{os.path.basename(file_path_arg)}.{counter:03d}.txt', 'wt', encoding="utf-8")
    file_out.write(buffer)
    file_out.close()


for file_path in txt_files_en:
    print(f'processing: {file_path}')
    process_file(file_path)
