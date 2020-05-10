from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import xlrd

from logger import logger

# PDF file to split
input_pdf = r'data_files\mail_merge.pdf'

# Excel file used in merge
excel_loc = r'data_files\data.xlsx'

folder_output = "pdf_output"


def main():

    input_file = PdfFileReader(open(input_pdf, "rb"))
    wb_sheet = xlrd.open_workbook(excel_loc).sheet_by_index(0)

    for i in range(input_file.numPages):
        output = PdfFileWriter()
        output.addPage(input_file.getPage(i))

        _index = str(wb_sheet.cell_value(i+1, 0))
        _name = str(wb_sheet.cell_value(i+1, 1))
        _manager = str(wb_sheet.cell_value(i+1, 2))

        manager_folder = os.path.join(folder_output, _manager)

        if not os.path.exists(manager_folder):
            os.mkdir(manager_folder)

        output_file = os.path.join(manager_folder, _name + ".pdf")
        with open(output_file, "wb") as outputStream:
            output.write(outputStream)
            logger.info(f'[{_index} - {output_file}]')

    return


if __name__ == '__main__':
    main()
