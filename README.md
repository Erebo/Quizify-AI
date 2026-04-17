# 🚀 Quizify Learn AI

**Quizify Learn AI** is a multimodal AI-powered study assistant that transforms handwritten or printed notes into structured summaries, interactive quizzes, and audio explanations.

🔗 **Live App:** https://quizify-learn-ai.streamlit.app/

---

## ✨ Features

* 📄 **Smart Summarization**
  Upload note images and get concise, structured summaries.

* 🧠 **Automatic Quiz Generation**
  Generate quizzes with adjustable difficulty (Easy, Medium, Hard).

* 🔊 **Text-to-Speech Output**
  Listen to your notes with built-in audio generation.

* 🖼️ **Image-Based Input**
  Supports multiple image uploads (up to 3 at a time).

---

## ⚙️ How It Works

1. Upload images of your notes
2. AI extracts and summarizes the content
3. Generates quizzes based on difficulty
4. Converts summary into audio for better learning

The system uses:

* **Gemini API** for multimodal understanding and generation 
* **gTTS** for audio synthesis 
* **Streamlit** for the interactive UI 

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* gTTS (Text-to-Speech)
* Pillow (Image Processing)

---

## 🚀 Installation (Run Locally)

```bash
git clone https://github.com/Erebo/note-summary-and-quiz-generator.git
cd note-summary-and-quiz-generator
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the app:

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
├── app.py                  # Main Streamlit application
├── api_calling.py         # Core AI logic (summary, quiz, audio)
├── working_image.py       # Image preprocessing
├── working_audio.py       # Audio generation
├── requirements.txt
└── README.md
```

---

## 🎯 Use Cases

* Students converting handwritten notes into study material
* Quick revision using summaries + quizzes
* Audio-based learning for better retention

---

## 📌 Future Improvements

* PDF support
* Multi-language summaries
* User authentication & saved sessions
* Better UI/UX enhancements

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed by **Mahadi Rahman Jihad**

---
