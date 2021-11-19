python cautare5.py
mkdir documente
copy logs.txt documente
cd documente
cd ..
python final3.py logs.txt
python filter_duplicates_empty.py
python document_splitter.py
python filter_duplicates_empty.py --in_dir data_en_split
python sterge_mari.py
python translator.py
python textautomat3.py
cd data_ro
start result.txt
python vorbeste.py
