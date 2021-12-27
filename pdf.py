from PyPDF2 import PdfFileMerger, PdfFileReader
from io import BytesIO, StringIO
import base64

def merge_b64_pdf_files(file_strings):
    merged_object = PdfFileMerger()

    for fs in file_strings:
        try:
            decoded = base64.b64decode(fs)
            reader = PdfFileReader(BytesIO(decoded))
            if reader.isEncrypted:
                reader.decrypt('')
            merged_object.append(reader, import_bookmarks=False)
        except NotImplementedError:
            continue

    output = BytesIO()

    merged_object.write(output)

    return output

def pdf_to_b64(bstring):
    bio  = BytesIO()
    b64string = base64.b64encode(bstring)

    bio.write(b64string)

    return bio


