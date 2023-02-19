import os
from PyPDF2 import PdfMerger


# Ask the user for the path containing the PDFS that are about to get merge.
path = input("Enter the path to the directory containing the PDFs: ")

# Get list of PDFs in that directory that are a .PDF
pdf_files = [file for file in os.listdir(path) if file.endswith(".pdf")]

# List how many pdfs are inside 
print("PDFs in directory:")
for i, pdf in enumerate(pdf_files):
    print(f"{i}. {pdf}")
selected_pdfs = input("Enter the numbers of the PDFs you want to merge (separated by spaces): ").split()

# Merger object, takes the inputs confirm is a digit and then adds it to the merger list. 
merger = PdfMerger()
for pdf_num in selected_pdfs:
    if pdf_num.isdigit():
        pdf_num = int(pdf_num)
        merger.append(path + "\\" + pdf_files[pdf_num])
    else:
        print(f"Invalid input: {pdf_num} is not a number.")

# Ask the user for a name for the new merged pdf file.
output_file = input("Enter the name of the output file: ")
merger.write(path + "\\" + output_file)