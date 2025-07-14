from flask import Blueprint, request, render_template, jsonify, current_app
import base64
import os

chatbot_bp = Blueprint('chatbot', __name__)

def get_background_image():
    image_path = os.path.join("app", "static", "images", "background.webp")
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode("utf-8")
            return f"data:image/webp;base64,{encoded}"
    except FileNotFoundError:
        return ""

@chatbot_bp.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        try:
            user_message = request.get_json().get("user_message", "")
            if not user_message:
                return jsonify({"bot_response": "الرسالة غير صالحة"}), 400

            pipe = current_app.config['PIPE']
            result = pipe(f"<s>[INST] {user_message} [/INST]", max_length=50)
            generated_text = result[0]['generated_text']
            response = generated_text.split("[/INST]")[-1].strip()
            return jsonify({"bot_response": response})
        except Exception as e:
            return jsonify({"bot_response": f"حدث خطأ: {str(e)}"}), 500
    return render_template("index.html", background_image=get_background_image())
