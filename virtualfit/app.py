from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['photo']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"image_url": filepath})
    return jsonify({"error": "No file uploaded"})

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_msg = request.json['message']
    if "shirt" in user_msg.lower():
        reply = "I recommend our premium cotton shirts."
    elif "pants" in user_msg.lower():
        reply = "You can try our slim fit pants."
    else:
        reply = "I can help you choose outfits and styles!"
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
