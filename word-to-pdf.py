import sys
import os
import comtypes.client


#   HOW TO USE FROM MAIN

#       > In Explorer   > Shift+RMB     > Open Powershell window here
#   OR  > In Explorer   > CTRL+L    > cmd

#   > python word-to-pdf.py folder\word-file.docx folder\pdf-file.pdf


def word_to_pdf(in_file, out_file):
    wd_format_pdf = 17
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wd_format_pdf)
    doc.Close()
    word.Quit()

    return


def main():

    in_file = os.path.abspath(sys.argv[1])
    out_file = os.path.abspath(sys.argv[2])

    word_to_pdf(in_file, out_file)

    return


if __name__ == '__main__':
    main()
