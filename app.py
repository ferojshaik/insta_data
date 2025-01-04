from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json
import os

app = Flask(__name__)

# Store activity data
activity_data = []

@app.route('/')
def home():
    return render_template('tracker.html')

@app.route('/track', methods=['POST'])
def track_activity():
    try:
        data = request.json
        activity = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': data.get('type', 'unknown'),
            'url': data.get('url', ''),
            'username': data.get('username', ''),
            'content': data.get('content', ''),
            'duration': data.get('duration', 0)
        }
        
        activity_data.append(activity)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/view')
def view_activity():
    return render_template('view.html', activities=activity_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)