# 🍽️ SnapChef AI

SnapChef AI is an interactive, full-stack Applied Artificial Intelligence web application built using **Python**, **Streamlit**, and the **Google Gemini 2.5 Flash** model. Upload or capture a food photo and instantly get nutritional analysis, a step-by-step recipe, and a context-aware AI chef to chat with!

🌐 **Live App:** [👉 Click here to open SnapChef AI](https://snapchef-ai-eepkyucdb9uvkyv7lf7k4n.streamlit.app/)

---

## 🚀 Key AI Features

- **📸 Multimodal Computer Vision** — Processes uploaded images or live camera captures (`st.camera_input`) using Gemini's vision model to accurately recognize any dish.
- **🧠 Context-Aware NLP Chat** — An interactive AI chef assistant that uses the identified dish as active conversational context for follow-up questions.
- **🔥 Nutrition & Recipe Engine** — Instantly returns calories, macros (protein, carbs, fat), spice level, cuisine origin, and a full step-by-step cooking guide.
- **⏱️ Live Session Memory** — Uses `st.session_state` to maintain a clean history log of all scanned dishes during the session.
- **🎨 Custom Dark UI** — Dark-themed glassmorphism CSS design with a polished, professional look.

---

## 🧱 Application Architecture

The system is engineered across three functional pillars:

1. **Frontend (UI Layer)** — Built with Streamlit, custom HTML injection, and dark-themed CSS glassmorphism.
2. **AI Core (Processing Layer)** — Powered by the `gemini-2.5-flash` model via the `google-genai` SDK.
3. **Data Parsing Logic** — Custom string-segmentation helper functions (`.split()`) to structurally extract unstructured AI text output into clean UI sections.

```
SnapChef-AI/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🛠️ Installation & Setup (Local Machine)

Follow these steps to run SnapChef AI on your local computer:

**1. Clone this repository**
```bash
git clone https://github.com/CharlapallyDivyani/SnapChef-AI.git
cd SnapChef-AI
```

**2. Install dependencies**
```bash
pip install streamlit google-genai pillow
```

**3. Set up your Gemini API key**

Create a folder and file: `.streamlit/secrets.toml` and add:
```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```
> Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📦 Requirements

| Package | Purpose |
|---|---|
| `streamlit` | Web app framework |
| `google-genai` | Gemini AI SDK |
| `pillow` | Image processing |

---

## 🤖 How It Works

1. User uploads a food image or takes a live camera shot
2. Image is converted to base64 and sent to Gemini 2.5 Flash with a structured prompt
3. The AI returns dish name, cuisine, calories, nutrition, recipe, and fun facts
4. Custom parser extracts each section and displays it in organized UI cards
5. User can then chat with the AI chef using the dish as context

---

## 👩‍💻 Built By

**Divyani Charlaplly**
B.Tech CSE | Bhaskar Engineering College, Hyderabad


[![GitHub](https://img.shields.io/badge/GitHub-CharlapallyDivyani-181717?logo=github)](https://github.com/CharlapallyDivyani)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
