from PyPDF2 import PdfFileMerger, PdfFileReader
from io import BytesIO
import base64

def merge_b64_pdf_files(file_strings):
    merged_object = PdfFileMerger()

    for fs in file_strings:
        decoded = base64.b64decode(fs)
        merged_object.append(PdfFileReader(BytesIO(decoded)))

    output = BytesIO()

    merged_object.write(output)

    return output

