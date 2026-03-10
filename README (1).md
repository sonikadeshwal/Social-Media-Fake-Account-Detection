# 🛡️ Social Media Fake Account Detection — Streamlit App

## Files
| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `model.joblib` | *(Optional)* Pre-trained scikit-learn model |
| `train.csv` | *(Optional)* Training data from your repo |

---

## 🚀 Deploy on Streamlit Community Cloud (Free)

### Step 1 — Add files to your GitHub repo
Upload `app.py` and `requirements.txt` to:
```
https://github.com/sonikadeshwal/Social-Media-Fake-Account-Detection
```

### Step 2 — (Optional) Export your trained model
In your notebook, after training add:
```python
import joblib
joblib.dump(model, "model.joblib")   # or your pipeline variable
```
Upload `model.joblib` to the same repo.

### Step 3 — Deploy
1. Go to **https://share.streamlit.io**
2. Sign in with GitHub
3. Click **"New app"**
4. Fill in:
   - **Repository:** `sonikadeshwal/Social-Media-Fake-Account-Detection`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **Deploy!** 🎉

Your app will be live at:
`https://sonikadeshwal-social-media-fake-account-detection-app-xxxx.streamlit.app`

---

## 🏃 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📝 Notes
- If `model.joblib` is **not** found, the app auto-trains a demo Random Forest on synthetic data so it still works out-of-the-box.
- If `train.csv` is present in the same directory, it will be used automatically for training.
- The model expects these 11 features (in order):
  1. profile_pic (0/1)
  2. nums_length_username (ratio 0–1)
  3. fullname_words (count)
  4. nums_length_fullname (ratio 0–1)
  5. name_equals_username (0/1)
  6. description_length (character count)
  7. external_url (0/1)
  8. private (0/1)
  9. num_posts
  10. num_followers
  11. num_follows
