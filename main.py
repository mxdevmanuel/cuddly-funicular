from flask import Flask, request, send_file
from pdf import merge_b64_pdf_files

app = Flask(__name__)


@app.route("/merge", methods=['POST'])
def merge():
    data = request.json
    if data is None:
        pass
    files = data.get('files')
    merged_file = merge_b64_pdf_files(files)
    merged_file.seek(0)

    return send_file(merged_file, as_attachment=True, attachment_filename="merged.pdf", mimetype='application/pdf')
