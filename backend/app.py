
from flask import Flask , jsonify , request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message" : "Accessible Backend Running"})


@app.route('/submit-url' , methods=["POST"])
def submit_url():
    data = request.get_json()

    return jsonify({
        "status" : "received",
        "url" : data["url"]
    })

if __name__ == "__main__":
    app.run(debug= True)

