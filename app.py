from flask import Flask, request, render_template, jsonify
import os
from werkzeug.utils import secure_filename
from extractor import extract_text, preprocess_text, extract_data_points

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = extract_text(file_path)
        preprocessed_text = preprocess_text(text)
        data_points = extract_data_points(preprocessed_text)
        return jsonify(data_points)
    return 'Invalid file format'

if __name__ == '__main__':
    app.run(debug=True)
