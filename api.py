from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
from tempfile import NamedTemporaryFile
# from resumeConvertFromYAML.process_data import process_data
from resumeConvertFromYAML import process_data


app = Flask(__name__)
cors = CORS(app, resources={r"/convert_resume": {"origins": "http://localhost:3000"}})

@app.route('/convert_resume', methods=['POST'])
def convert_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    print(file.filename)

    # Print a sample of the data
    file.seek(0)
    print(file.read(100))
    file.seek(0)

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    print(f"Received file: {file.filename}")

    if file and file.filename.endswith('.yaml'):
        try:
            # Use a temporary file to handle the YAML file
            with NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                output_filename = temp_file.name

                print(f"Processing file: {file.filename} to {output_filename}")

                # Process the YAML file to PDF
                data = process_data(file, output_filename, "pdf")  # Ensure this function writes to the given filename
                print(f"Data: {data}")


                attachment_filename = os.path.basename(output_filename)
                print(f"Sending file: {attachment_filename}")

                # Send the PDF file back
                # return output_filename, as_attachment=True, attachment_filename1
                return data, 200
        except Exception as e:
            # Handle exceptions from process_data
            return jsonify({"error": str(e)}), 500
        finally:
            # Clean up the temporary file
            if os.path.exists(output_filename):
                os.remove(output_filename)
    else:
        return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(debug=True)
