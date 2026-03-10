import streamlit as st
import numpy as np
import joblib
import os
import re

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Fake Account Detector",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* Dark background */
.stApp {
    background: #0a0e1a;
    color: #e0e6ff;
}

/* Header */
.hero-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.6rem;
    background: linear-gradient(135deg, #4f8ef7 0%, #a78bfa 60%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 0.2rem;
}
.hero-sub {
    text-align: center;
    color: #7c8db0;
    font-size: 1rem;
    margin-bottom: 2rem;
    font-family: 'Space Mono', monospace;
}

/* Card */
.card {
    background: #111827;
    border: 1px solid #1e2a42;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}

/* Result boxes */
.result-fake {
    background: linear-gradient(135deg, #3b0a0a, #1a0505);
    border: 2px solid #ef4444;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
}
.result-real {
    background: linear-gradient(135deg, #052e16, #061a0e);
    border: 2px solid #22c55e;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
}
.result-label {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 2.2rem;
}
.result-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #94a3b8;
    margin-top: 0.5rem;
}

/* Metric bar */
.metric-row {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    color: #64748b;
    margin-bottom: 0.3rem;
}
.bar-bg {
    background: #1e2a42;
    border-radius: 99px;
    height: 6px;
    margin-bottom: 1rem;
}
.bar-fill {
    height: 6px;
    border-radius: 99px;
}

/* Divider */
hr { border-color: #1e2a42; }

/* Streamlit overrides */
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label {
    color: #94a3b8 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.82rem !important;
}
.stButton > button {
    background: linear-gradient(135deg, #4f8ef7, #a78bfa);
    color: white;
    border: none;
    border-radius: 10px;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 0.75rem 2rem;
    width: 100%;
    cursor: pointer;
    transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }

section[data-testid="stSidebar"] { display: none; }
</style>
""", unsafe_allow_html=True)


# ── Load or train model ─────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    """Load saved model or train a demo one if not present."""
    MODEL_PATH = "model.joblib"
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    # ── Fallback: train a lightweight demo model ──
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    import pandas as pd

    # Try loading the repo CSVs if present
    if os.path.exists("train.csv"):
        df = pd.read_csv("train.csv")
        # Assume last column is label, rest are features
        X = df.iloc[:, :-1].select_dtypes(include=[np.number])
        y = df.iloc[:, -1]
    else:
        # Synthetic demo data
        rng = np.random.default_rng(42)
        n = 2000
        X = pd.DataFrame({
            "profile_pic": rng.integers(0, 2, n),
            "nums_length_username": rng.uniform(0, 1, n),
            "fullname_words": rng.integers(0, 5, n),
            "nums_length_fullname": rng.uniform(0, 1, n),
            "name_equals_username": rng.integers(0, 2, n),
            "description_length": rng.integers(0, 200, n),
            "external_url": rng.integers(0, 2, n),
            "private": rng.integers(0, 2, n),
            "num_posts": rng.integers(0, 500, n),
            "num_followers": rng.integers(0, 5000, n),
            "num_follows": rng.integers(0, 5000, n),
        })
        # Simple rule-based fake label for demo
        y = ((X["num_followers"] < 30) & (X["num_follows"] > 400) |
             (X["profile_pic"] == 0) & (X["num_posts"] < 5)).astype(int)

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42)),
    ])
    pipe.fit(X, y)
    joblib.dump(pipe, MODEL_PATH)
    return pipe


model = load_model()


# ── Helper ──────────────────────────────────────────────────────────────────────
def count_nums_ratio(s: str) -> float:
    if not s:
        return 0.0
    digits = sum(c.isdigit() for c in s)
    return round(digits / len(s), 4)


def predict(features: list) -> tuple[str, float]:
    arr = np.array(features).reshape(1, -1)
    pred = model.predict(arr)[0]
    proba = model.predict_proba(arr)[0]
    confidence = float(proba[pred])
    label = "FAKE" if pred == 1 else "REAL"
    return label, confidence


# ── UI ──────────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">🛡️ Fake Account Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">social media • ML-powered • binary classification</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("#### 👤 Profile Identity")

col1, col2 = st.columns(2)
with col1:
    username = st.text_input("Username", placeholder="e.g. john_doe123")
    fullname = st.text_input("Full Name", placeholder="e.g. John Doe")
with col2:
    has_profile_pic = st.selectbox("Has Profile Picture?", ["Yes", "No"])
    has_external_url = st.selectbox("Has External URL?", ["No", "Yes"])

name_equals_username = 1 if username and fullname and username.lower() == fullname.lower().replace(" ", "_") else 0
nums_length_username = count_nums_ratio(username)
fullname_words = len(fullname.split()) if fullname else 0
nums_length_fullname = count_nums_ratio(fullname)

st.markdown("#### 📝 Bio & Privacy")
col3, col4 = st.columns(2)
with col3:
    bio = st.text_area("Bio / Description", placeholder="Write bio here...", height=80)
    description_length = len(bio)
with col4:
    is_private = st.selectbox("Private Account?", ["No", "Yes"])

st.markdown("#### 📊 Activity & Engagement")
col5, col6, col7 = st.columns(3)
with col5:
    num_posts = st.number_input("Posts", min_value=0, max_value=100000, value=10)
with col6:
    num_followers = st.number_input("Followers", min_value=0, max_value=10000000, value=100)
with col7:
    num_follows = st.number_input("Following", min_value=0, max_value=100000, value=200)

st.markdown('</div>', unsafe_allow_html=True)

# ── Predict button ──────────────────────────────────────────────────────────────
if st.button("🔍 Analyse Account"):
    features = [
        1 if has_profile_pic == "Yes" else 0,
        nums_length_username,
        fullname_words,
        nums_length_fullname,
        name_equals_username,
        description_length,
        1 if has_external_url == "Yes" else 0,
        1 if is_private == "Yes" else 0,
        num_posts,
        num_followers,
        num_follows,
    ]

    label, confidence = predict(features)

    st.markdown("---")
    if label == "FAKE":
        st.markdown(f"""
        <div class="result-fake">
            <div class="result-label" style="color:#ef4444;">⚠️ FAKE ACCOUNT</div>
            <div class="result-sub">Confidence: {confidence*100:.1f}% — This account shows patterns typical of fake profiles.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-real">
            <div class="result-label" style="color:#22c55e;">✅ REAL ACCOUNT</div>
            <div class="result-sub">Confidence: {confidence*100:.1f}% — This account appears to be legitimate.</div>
        </div>
        """, unsafe_allow_html=True)

    # Feature breakdown bars
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Signal Breakdown**")

    signals = {
        "Profile Picture": (1 if has_profile_pic == "Yes" else 0, 1),
        "Numeric Username Ratio": (nums_length_username, 1),
        "Bio Length": (min(description_length / 200, 1), 1),
        "Follower Count": (min(num_followers / 5000, 1), 1),
        "Following Count": (min(num_follows / 5000, 1), 1),
        "Post Count": (min(num_posts / 500, 1), 1),
    }

    for name, (val, _) in signals.items():
        pct = int(val * 100)
        color = "#4f8ef7" if val > 0.4 else "#f472b6"
        st.markdown(f"""
        <div class="metric-row"><span>{name}</span><span>{pct}%</span></div>
        <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;background:{color};"></div></div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p style="text-align:center;color:#334155;font-size:0.75rem;font-family:Space Mono,monospace;">Powered by scikit-learn · Streamlit · sonikadeshwal</p>', unsafe_allow_html=True)
