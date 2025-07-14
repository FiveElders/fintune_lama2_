# Agri Chatbot 🌾🤖

مساعد زراعي مبني على نموذج LLaMA2 مدرب على البيانات الزراعية.

## ✅ المتطلبات

```bash
pip install -r requirements.txt
```

## 🚀 التشغيل

1. أضف مفتاح ngrok داخل بيئتك:
   ```bash
   ngrok config add-authtoken YOUR_NGROK_TOKEN
   ```

2. شغّل التطبيق:
   ```bash
   python run.py
   ```

3. انسخ الرابط الذي يظهر، وافتحه في المتصفح.

## 📁 الهيكل

- `app/` يحتوي على ملفات Flask.
- `model/` لتحميل النموذج.
- `run.py` لتشغيل التطبيق.
- `requirements.txt` لتثبيت المكتبات.
