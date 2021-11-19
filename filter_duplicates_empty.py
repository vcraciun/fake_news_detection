import argparse
import glob
import os

parser = argparse.ArgumentParser(description='Athos article filter')
parser.add_argument(
    '--in_dir',
    type=str,
    default='stiri',
    required=False,
)
args = parser.parse_args()

txt_files_en = glob.glob(f'{args.in_dir}/*.txt')

content_hash = {}
for file_path in txt_files_en:
    content = open(file_path, encoding='utf8', errors='ignore').read()
    if len(content) == 0:
        print(f'empty: {file_path}')
        os.unlink(file_path)
        continue

    file_hash = hash(content)
    if file_hash in content_hash:
        print(f'duplicate: {file_path}')
        os.unlink(file_path)

    content_hash[file_hash] = True
