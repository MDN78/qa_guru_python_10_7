import pypdf
from utils.path import Path as P
from openpyxl import load_workbook
import csv

def test_read_pdf_file(directory_manager):
    reader = pypdf.PdfReader(P.resources_directory + '/' + 'Python Testing with Pytest (Brian Okken).pdf')
    reader.pages[1].extract_text()
    assert "Python Testing with pytest" in reader.pages[1].extract_text()

def test_read_xlsx_file(directory_manager):
    workbook = load_workbook(P.resources_directory + '/' + 'file_example_XLSX_50.xlsx')
    sheet = workbook.active
    assert sheet.cell(1, 2).value == 'First Name'
    assert sheet.cell(2, 2).value == 'Dulce'
    assert sheet.cell(2, 3).value == 'Abril'

def test_read_csv_file(directory_manager):
    with open(P.resources_directory + '/' + 'catalog_auto_google.csv', 'r') as read:
        reader = csv.DictReader(read, delimiter=",")
        assert [row['id'] for row in reader] == ['K456653443']