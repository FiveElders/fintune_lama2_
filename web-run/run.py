from pyngrok import ngrok
from app import create_app

app = create_app()

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    print("Public URL:", public_url)
    app.run(port=5000)
