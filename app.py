import streamlit as st
from google import genai
from PIL import Image
import base64
import io
import random

# ==========================================
# 🔑 PASTE YOUR ACTUAL GEMINI API KEY HERE
# ==========================================
# ==========================================
# 🔑 SECURE API MANAGEMENT FOR CLOUD DEPLOYMENT
# ==========================================
try:
    # This automatically pulls the key from Streamlit's secure dashboard settings
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    # Fallback placeholder if running locally
    API_KEY = "YOUR_GEMINI_API_KEY_HERE"

# Initialize the Gemini Client
client = genai.Client(api_key=API_KEY)

# List of fun food quotes
FOOD_QUOTES = [
    "🍽️ 'Food is not just eating energy. It's an experience!' — Guy Fieri",
    "👨‍🍳 'Cooking is love made visible!' — Unknown",
    "🌮 'Life is too short for bad food!' — Unknown",
    "🍕 'Food brings people together on many different levels!' — Emeril Lagasse",
    "🥘 'Food is the ingredient that binds us together!' — Unknown",
]

# The structural prompt for the AI model
FOOD_PROMPT = """
You are SnapChef AI — the world's most enthusiastic food expert! 🍽️

Analyze this food image and provide a detailed response in this EXACT format. Do not change the headers:

DISH_NAME
[Name of the dish]

CUISINE_ORIGIN
[Which country or region]

FOODIE_RATING
[Rate out of 10]

SPICE_LEVEL
[Mild / Medium / Spicy]

CALORIES
[Approximate calories]

NUTRITION_INFO
[Protein, Carbs, Fat details]

RECIPE_STEPS
[Ingredients and step-by-step instructions]

FUN_FACT
[One interesting fact]

HEALTHY_TIP
[One healthy tip]

PAIRS_WELL
[What goes well with it]
"""

# Configure Streamlit Page Layout
st.set_page_config(
    page_title="SnapChef 🍽️", 
    page_icon="🍽️", 
    layout="wide"
)

# --- UI CSS CUSTOM STYLING ---
st.markdown("""
<style>
#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
.stApp { background: linear-gradient(135deg, #0f0c1b 0%, #1a101f 50%, #140b16 100%); font-family: sans-serif; }
.snap-header { text-align: center; padding: 20px; }
.snap-title { font-size: 50px; font-weight: 900; color: #ff6b00 !important; margin: 0; }
.snap-subtitle { font-size: 18px; color: #b0a8ba !important; margin-bottom: 10px; }
.snap-quote { display: inline-block; margin-top: 10px; font-size: 14px; color: #ffaa44 !important; background: rgba(255, 107, 0, 0.08); padding: 8px 20px; border-radius: 20px; border: 1px solid rgba(255, 107, 0, 0.2); font-style: italic; }
.result-card { background: #151124; border-left: 4px solid #ff6b00; border-radius: 12px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.25); }
.history-card { background: #151124; border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 15px; margin-bottom: 10px; }
.stButton button { background: linear-gradient(135deg, #ff6b00 0%, #ff8800 100%) !important; color: white !important; border-radius: 10px !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Initialize memory arrays if they don't exist yet
if "history" not in st.session_state: st.session_state.history = []
if "chat_messages" not in st.session_state: st.session_state.chat_messages = []
if "current_analysis" not in st.session_state: st.session_state.current_analysis = None
if "dish_context" not in st.session_state: st.session_state.dish_context = ""
if "active_quote" not in st.session_state: st.session_state.active_quote = random.choice(FOOD_QUOTES)

# --- APP HEADER BANNER WITH FIXED QUOTATIONS ---
st.markdown(f"""
<div class='snap-header'>
    <h1 class='snap-title'>🍽️ SnapChef</h1>
    <p class='snap-subtitle'>Get The Complete Food Story!</p>
    <div class='snap-quote'>{st.session_state.active_quote}</div>
</div>
""", unsafe_allow_html=True)

# Main Application Tabs (Now with 3 easy-to-click buttons/tabs!)
tab1, tab2, tab3 = st.tabs(["📸 Snap & Analyze", "💬 Chat with SnapChef", "📜 Food History"])

# --- TAB 1: VISION ENGINE ---
with tab1:
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 📸 Input Media Source")
        input_mode = st.radio("Choose source:", ["Upload Image File", "Use Live Camera Shot"], label_visibility="collapsed")
        
        uploaded_file = None
        if input_mode == "Upload Image File":
            uploaded_file = st.file_uploader("Upload a photo...", type=["jpg", "jpeg", "png"])
        else:
            uploaded_file = st.camera_input("Take a photo of your food! 📸")
            
        if uploaded_file:
            image = Image.open(uploaded_file)
            if input_mode == "Upload Image File":
                st.image(image, use_container_width=True)
            
            if st.button("🔍 Analyze This Food!", use_container_width=True):
                with st.spinner("👨‍🍳 Analyzing..."):
                    img_byte_arr = io.BytesIO()
                    image.save(img_byte_arr, format='PNG')
                    img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode()
                    
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[
                            {"inline_data": {"mime_type": "image/png", "data": img_base64}},
                            {"text": FOOD_PROMPT}
                        ]
                    )
                    
                    st.session_state.current_analysis = response.text
                    st.session_state.active_quote = random.choice(FOOD_QUOTES)
                    st.rerun()

    with col2:
        st.markdown("### 🍽️ SnapChef Report")
        raw_text = st.session_state.current_analysis
        
        if raw_text:
            def find_text_section(full_text, keyword, next_keyword=None):
                if keyword not in full_text: return "Not Available"
                start = full_text.split(keyword)[1]
                if next_keyword and next_keyword in start:
                    return start.split(next_keyword)[0].strip()
                return start.strip()

            dish = find_text_section(raw_text, "DISH_NAME", "CUISINE_ORIGIN")
            cuisine = find_text_section(raw_text, "CUISINE_ORIGIN", "FOODIE_RATING")
            rating = find_text_section(raw_text, "FOODIE_RATING", "SPICE_LEVEL")
            spice = find_text_section(raw_text, "SPICE_LEVEL", "CALORIES")
            calories = find_text_section(raw_text, "CALORIES", "NUTRITION_INFO")
            nutrition = find_text_section(raw_text, "NUTRITION_INFO", "RECIPE_STEPS")
            recipe = find_text_section(raw_text, "RECIPE_STEPS", "FUN_FACT")
            fact = find_text_section(raw_text, "FUN_FACT", "HEALTHY_TIP")
            tip = find_text_section(raw_text, "HEALTHY_TIP", "PAIRS_WELL")
            pairs = find_text_section(raw_text, "PAIRS_WELL")

            if not st.session_state.history or st.session_state.history[-1]["dish"] != dish:
                st.session_state.history.append({"dish": dish, "calories": calories, "rating": rating})
                st.session_state.dish_context = dish

            st.markdown(f"""
            <div class='result-card'>
                <h2 style='margin:0; color:#ff6b00;'>{dish}</h2>
                <p style='color:#ffffff; margin: 8px 0 4px 0;'>🌍 <b>Origin:</b> {cuisine} | ⭐ <b>Rating:</b> {rating}</p>
                <p style='color:#ffffff; margin: 0;'>🌶️ <b>Spice:</b> {spice} | 🔥 <b>Calories:</b> {calories}</p>
            </div>
            """, unsafe_allow_html=True)

            with st.expander("📊 Nutrition Summary", expanded=True):
                st.write(nutrition)
            with st.expander("👨‍🍳 Recipe & Cooking Guide", expanded=False):
                st.write(recipe)
            with st.expander("💡 Tips & Fun Facts", expanded=False):
                st.markdown(f"**Fact:** {fact}")
                st.markdown(f"**Healthy Tip:** {tip}")
            with st.expander("🍹 Pairing Ideas", expanded=False):
                st.write(pairs)
        else:
            st.info("Upload an image file or capture a live shot on the left side panel to trigger the AI analysis!")

# --- TAB 2: CHAT ENGINE ---
with tab2:
    st.markdown("### 💬 Chat about this food")
    if st.session_state.dish_context:
        st.write(f"Discussing active topic: **{st.session_state.dish_context}**")
        
    for msg in st.session_state.chat_messages:
        st.chat_message(msg["role"]).write(msg["content"])
        
    user_chat = st.chat_input("Ask a question about alternatives or preparation modifications...")
    if user_chat:
        st.session_state.chat_messages.append({"role": "user", "content": user_chat})
        
        prompt = f"Context: The user is looking at {st.session_state.dish_context}. Question: {user_chat}"
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        
        st.session_state.chat_messages.append({"role": "assistant", "content": response.text})
        st.rerun()

# --- TAB 3: NEW VISIBLE HISTORY ENGINE ---
with tab3:
    st.markdown("### 📜 Your Scanned Food History Log")
    
    if len(st.session_state.history) == 0:
        st.info("📸 No food analyzed yet! Head over to the 'Snap & Analyze' tab to scan your first dish.")
    else:
        # Loop through saved items and show them beautifully in the main screen space
        for item in reversed(st.session_state.history):
            st.markdown(f"""
            <div class='history-card'>
                <h4 style='margin:0; color:#ff6b00;'>🍽️ {item['dish']}</h4>
                <p style='margin:4px 0 0 0; color:#b0a8ba; font-size:14px;'>
                    🔥 Energy Estimate: <b>{item['calories']}</b> | ⭐ Culinary Rating: <b>{item['rating']}</b>
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        if st.button("🗑️ Clear History Log", use_container_width=True):
            st.session_state.history = []
            st.session_state.current_analysis = None
            st.session_state.dish_context = ""
            st.rerun()