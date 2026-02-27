from flask import Flask, request, jsonify
import re

app = Flask(__name__)

transactions = []

@app.route("/process-payment", methods=["POST"])
def process_payment():
    data = request.json
    card = data.get("card")
    amount = data.get("amount")

    if not re.match(r"/d{16}", card):
        return jsonify({"error": "Invalid card number"}), 400
    transactions.append({"card":card, "amount": amount})
    return jsonify({"message":"Payment processed successsfully"}), 200

@app.route("/health")
def health():
    return {"status":UP}

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)