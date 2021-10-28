from flask import Flask, request, send_file
from flask_cors import CORS
from pdf import merge_b64_pdf_files, pdf_to_b64

app = Flask(__name__)
CORS(app)


@app.route("/merge", methods=['POST'])
def merge():
    data = request.json
    if data is None:
        pass
    files = data.get('files')
    merged_file = merge_b64_pdf_files(files)
    merged_file.seek(0)
    mime ='application/pdf' 

    if data.get('base64') is not None:
        merged_file = pdf_to_b64(merged_file.read())
        merged_file.seek(0)
        mime = 'application/text'

    return send_file(merged_file, as_attachment=True, attachment_filename="merged.pdf", mimetype=mime)
