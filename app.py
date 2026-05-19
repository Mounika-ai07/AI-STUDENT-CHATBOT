from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key="gsk_xxxxxxxxx"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():

    user_message = request.json["message"]

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI student chatbot."
                },

                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        bot_reply = response.choices[0].message.content

        return jsonify({
            "reply": bot_reply
        })

    except Exception as e:

        return jsonify({
            "reply": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)