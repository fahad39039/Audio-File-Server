"""Main file to run."""
from flask import Flask, request, jsonify
import json
from settings.database import init_db, db_session
from utils.utils import mapping_dict, row_to_dict

app = Flask(__name__)

init_db()
session = db_session


@app.route('/create', methods=['POST'])
def create_file():
    """'create_file' method is used for adding a new audio file record."""
    if request.method == 'POST':
        input_data = json.loads(request.data)
        file_type = input_data.get('audioFileType', None)

        if file_type is None:
            return "400 bad request"
        file_metadata = input_data.get('audioFileMetadata')

        if file_metadata["duration_in_sec"] <= 0:
            file_metadata["duration_in_sec"] = 0

        if file_type == "podcast":
            participants = file_metadata.get("participants", None)

            if (participants is None or len(participants) > 10 or
                    any(i for i in participants if len(i) > 100)):
                return "400 bad request"

            file_metadata['participants'] = ', '.join(participants)

        try:
            new_record_data = mapping_dict[file_type](**file_metadata)
            session.add(new_record_data)
            session.commit()
        except:
            return "400 bad request"

        return "200 OK"
    return "400 bad request"


@app.route('/delete/<audio_file_type>/<int:audio_file_id>', methods=['DELETE'])
def delete_file_by_id(audio_file_type, audio_file_id):
    """
    'delete_file_by_id' method is used for deleting existing audio file record.
    """
    if request.method == 'DELETE':
        try:
            get_record = session.query(mapping_dict[audio_file_type])\
                                .filter_by(id=audio_file_id)
            get_record.delete()
            session.commit()
            return "200 OK"
        except:
            return "400 bad request"
    return "400 bad request"


@app.route('/update/<audio_file_type>/<int:audio_file_id>', methods=['PUT'])
def update_file_by_id(audio_file_type, audio_file_id):
    """
    'update_file_by_id' method is used for updating existing audio file record.
    """
    if request.method == "PUT":
        input_data = json.loads(request.data)
        file_metadata = input_data.get('audioFileMetadata')
        try:
            session.query(mapping_dict[audio_file_type])\
                   .filter_by(id=audio_file_id).update(file_metadata)
            session.commit()
            return jsonify(success=True)
        except:
            return "400 bad request"

    return "400 bad request"


@app.route('/get/<audio_file_type>', methods=['GET'])
@app.route('/get/<audio_file_type>/<int:audio_file_id>', methods=['GET'])
def get_files(audio_file_type, audio_file_id=None):
    """'get_files' method is used for retrieving audio file records."""
    if request.method == 'GET':
        try:
            if audio_file_id:
                audio_file_data = session.query(mapping_dict[audio_file_type])\
                                         .filter_by(id=audio_file_id).first()
                final = row_to_dict(audio_file_data)
            else:
                audio_file_data = session.query(mapping_dict[audio_file_type])\
                                         .all()
                final = [row_to_dict(x) for x in audio_file_data]

            return jsonify(final)
        except:
            return "400 bad request"
    return "400 bad request"
