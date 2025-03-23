import sys
from pathlib import Path
from pdf2image import convert_from_path

# Is input PDF name?
try:
    pdf_file = sys.argv[1]
except:
    print('''
        error: PDF file name not nound
        ex. 
        python pdf2img.py hoge.pdf
    ''')
    sys.exit(1)

pdf_path = Path(f'./{pdf_file}')
img_path = Path('./output')

if pdf_path.exists() == False:
    print(f'error: {pdf_file} is not found')
    sys.exit(1)

# Make output dir
if img_path.exists() == False:
    img_path.mkdir()

# Convert
convert_from_path(pdf_path, output_folder=img_path, fmt='jpeg', output_file=pdf_path.stem)

