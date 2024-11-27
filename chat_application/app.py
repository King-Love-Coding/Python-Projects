import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)

# Define upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_media', methods=['POST'])
def upload_media():
    file = request.files.get('file')
    if file:
        try:
            # Save the file to the uploads directory
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Return the file URL and name to the client
            file_url = f'/uploads/{file.filename}'
            return jsonify({'url': file_url, 'name': file.filename})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'No file provided'}), 400

@app.route('/uploads/<filename>')
def serve_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': f'File not found: {e}'}), 404

@socketio.on('send_message')
def handle_send_message(data):
    # Add timestamp to the message data
    data['timestamp'] = datetime.now().strftime("%H:%M:%S")
    data['delivered'] = False  # Initially set to False
    # Emit message to all connected clients
    emit('receive_message', data, broadcast=True)

@socketio.on('message_read')
def handle_message_read(data):
    # Broadcast message read status to all clients
    emit('update_read_status', data, broadcast=True)

@socketio.on('typing')
def handle_typing(data):
    emit('display_typing', data, broadcast=True, include_self=False)

@socketio.on('stop_typing')
def handle_stop_typing(data):
    emit('hide_typing', data, broadcast=True, include_self=False)


if __name__ == "__main__":
    socketio.run(app, host="192.168.1.100", port=5000, debug=True)



