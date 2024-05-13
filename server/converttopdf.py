import os
import zipfile
from docx2pdf import convert
import tempfile
import argparse

def process_zip_file(input_zip_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Unzip the file
        with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        # Convert all .docx files to .pdf
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.endswith('.docx'):
                    docx_path = os.path.join(root, file)
                    pdf_path = os.path.splitext(docx_path)[0] + '.pdf'
                    convert(docx_path, pdf_path)
                    os.remove(docx_path)  # Remove the original .docx file

        # Zip the files again
        with zipfile.ZipFile(input_zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zip_ref.write(file_path, arcname)

def convert_docs_in_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item_path.endswith('.zip'):
            process_zip_file(item_path)
            
def main():
    parser = argparse.ArgumentParser(description='Convert DOCX files in a folder to PDF.')
    parser.add_argument('--folder', type=str, help='Folder containing DOCX files')
    args = parser.parse_args()

    # Your conversion code here using args.folder

if __name__ == "__main__":
    main()