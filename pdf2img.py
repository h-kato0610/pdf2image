import sys
from pathlib import Path
from pdf2image import convert_from_path

# Is input PDF name?
try:
    pdf_name = sys.argv[1]
except:
    print('''
        error: PDFfile NameNotFound
        ex. 
        python pdf2img.py hoge.pdf
    ''')
    sys.exit(1)

pdf_path = Path(f'./{pdf_name}')
img_path = Path('./output')

# Make output dir
if img_path.exists() == False:
    img_path.mkdir()

# Convert
convert_from_path(pdf_path, output_folder=img_path, fmt='jpeg', output_file=pdf_path.stem)

