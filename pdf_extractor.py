import argparse
import glob
import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

parser = argparse.ArgumentParser(description='PDF to TXT extractor')
parser.add_argument(
    '--in_dir',
    type=str,
    default='documente',
    required=False,
)
parser.add_argument(
    '--out_dir',
    type=str,
    default='stiri',
    required=False,
)

args = parser.parse_args()

if not os.path.exists(args.out_dir):
    os.makedirs(args.out_dir)


def pdf_to_txt(input_pdf, output_txt):
    outfp = open(output_txt, 'w', encoding='utf8')

    password = b''
    pagenos = None
    maxpages = None

    caching = True
    rsrcmgr = PDFResourceManager(caching=caching)

    laparams = LAParams()
    laparams.all_texts = True

    device = TextConverter(rsrcmgr, outfp, laparams=laparams,
                           imagewriter=None)

    with open(input_pdf, 'rb') as fp:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp, pagenos=pagenos,
                                      maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            interpreter.process_page(page)
    device.close()
    outfp.close()


print(args)
pdf_files_en = glob.glob(f"{args.in_dir}/*.pdf")
#pdf_files_en = [f for f in os.listdir(args.in_dir) if f.endswith('.pdf')]
print(pdf_files_en)
for file_path in pdf_files_en:
    print(f'processing: {file_path}')
    try:
        pdf_to_txt(file_path, f'{args.out_dir}/{os.path.basename(file_path)}.txt')
    except: 
        print('fisier pdf invalid')
