# 🛡️ Social Media Fake Account Detection

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red?style=flat-square&logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4+-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat-square)

> A machine learning web app that detects fake or fraudulent social media accounts by analyzing profile patterns, user behavior, and engagement statistics.

---

## 📌 Overview

Fake accounts are a growing threat on social media platforms — used for spam, misinformation, and manipulation. This project builds a **supervised ML classifier** that flags suspicious accounts based on features like follower ratios, username patterns, bio length, and activity metrics.

The model is served through an interactive **Streamlit web app** that lets anyone analyze an account in seconds.

---

## ✨ Features

- 🔍 **Real-time prediction** — enter profile details and get instant fake/real classification
- 📊 **Signal breakdown** — visual confidence bars for each input feature
- 🤖 **Auto-training fallback** — works without a pre-trained model using `train.csv`
- 🎨 **Clean dark UI** — built with custom Streamlit CSS

---

## 🧠 How It Works

1. User inputs social media profile attributes
2. Features are preprocessed and passed to a trained **Random Forest classifier**
3. Model outputs a **binary label** (Fake / Real) with a confidence score
4. Results are displayed with a per-feature signal breakdown

### Features Used by the Model

| # | Feature | Description |
|---|---------|-------------|
| 1 | `profile_pic` | Has a profile picture (0/1) |
| 2 | `nums_length_username` | Ratio of digits in username (0–1) |
| 3 | `fullname_words` | Number of words in full name |
| 4 | `nums_length_fullname` | Ratio of digits in full name (0–1) |
| 5 | `name_equals_username` | Full name matches username (0/1) |
| 6 | `description_length` | Character count of bio |
| 7 | `external_url` | Has an external URL (0/1) |
| 8 | `private` | Is a private account (0/1) |
| 9 | `num_posts` | Total number of posts |
| 10 | `num_followers` | Follower count |
| 11 | `num_follows` | Following count |

---

## 🗂️ Project Structure

```
Social-Media-Fake-Account-Detection/
│
├── app.py                        # Streamlit web application
├── requirements.txt              # Python dependencies
├── model.joblib                  # Trained ML model (optional)
├── train.csv                     # Training dataset
├── test.csv                      # Test dataset
├── FAKE_ACCOUNTDETECTION.ipynb   # Model training notebook
└── README.md
```

---

## 🚀 Deployment (Streamlit Community Cloud — Free)

### Step 1 — Export your trained model
Add this to the end of your notebook before uploading:
```python
import joblib
joblib.dump(model, "model.joblib")  # replace 'model' with your variable name
```

### Step 2 — Push all files to GitHub
Make sure `app.py`, `requirements.txt`, and `model.joblib` are in your repo root.

### Step 3 — Deploy on Streamlit Cloud
1. Visit **https://share.streamlit.io** and sign in with GitHub
2. Click **"New app"**
3. Set:
   - **Repository:** `sonikadeshwal/Social-Media-Fake-Account-Detection`
   - **Branch:** `main`
   - **Main file path:** `app.py`
4. Click **Deploy** 🎉

Your app will be live at:
```
https://sonikadeshwal-social-media-fake-account-detection-app-xxxx.streamlit.app
```

---

## 🏃 Run Locally

```bash
# Clone the repo
git clone https://github.com/sonikadeshwal/Social-Media-Fake-Account-Detection.git
cd Social-Media-Fake-Account-Detection

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| ML Library | scikit-learn |
| Web App | Streamlit |
| Model Serialization | joblib |
| Data Handling | pandas, numpy |
| Deployment | Streamlit Community Cloud |

---

## 📊 Dataset

The dataset contains labeled social media profiles with behavioral and structural features. It is split into:
- `train.csv` — used for model training
- `test.csv` — used for evaluation

---

## 👩‍💻 Author

**Sonika Deshwal**
- GitHub: [@sonikadeshwal](https://github.com/sonikadeshwal)

---

## 📄 License

This project is licensed under the MIT License.
