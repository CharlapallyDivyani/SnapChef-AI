# 🍽️ SnapChef AI

SnapChef AI is an interactive, full-stack Applied Artificial Intelligence web application built using Python, Streamlit, and the Google Gemini 2.5 Flash model. The app allows users to capture or upload food images, instantly analyze their nutritional value, get a step-by-step cooking recipe, and chat with an AI assistant with real-time context.

## 🚀 Key AI Features
- **📸 Multimodal Computer Vision:** Processes raw image files or live camera inputs (`st.camera_input`) using advanced vision models to accurately recognize dishes.
- **🧠 Context-Aware Natural Language Processing (NLP):** Features an interactive chat engine that dynamically uses the identified dish as active conversational context.
- **⏱️ Live Session Memory Engine:** Implements temporary state-management (`st.session_state`) to log scanned items into a clean, readable user history timeline.

## 🧱 Application Architecture
The system is engineered across three functional pillars:
1. **Frontend (UI Layer):** Built with Streamlit, custom HTML injection, and dark-themed CSS glassmorphism.
2. **AI Core (Processing Layer):** Powered by the `gemini-2.5-flash` model via the `google-genai` SDK.
3. **Data Parsing Logic:** Utilizes custom string-segmentation helper functions (`.split()`) to structurally extract unstructured text dynamically.

---

## 🛠️ Installation & Setup (Local Machine)

Follow these simple steps to run this project on your local computer:

1. Clone this repository.
2. Install dependencies: `pip install streamlit google-genai pillow`
3. Open `app.py` and paste your Gemini API key into the `API_KEY` variable.
4. Run the app: `streamlit run app.py`
