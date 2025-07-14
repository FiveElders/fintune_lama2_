from flask import Flask
from transformers import pipeline
from model.load_model import load_model

model, tokenizer = load_model()
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=50)

def create_app():
    app = Flask(__name__)
    app.config['PIPE'] = pipe

    from .routes import chatbot_bp
    app.register_blueprint(chatbot_bp)

    return app
