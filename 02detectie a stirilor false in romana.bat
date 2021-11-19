python cautare4.py
mkdir documente
copy logs.txt documente
python final3.py logs.txt
python filter_duplicates_empty.py
python document_splitter.py --out_dir data_ro
python textautomat2.py
cd data_ro
start result.txt
python vorbeste.py