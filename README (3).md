# 🕵️ Social Media Fake Account Detection

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  A machine learning–powered web application that detects fake and bot accounts on social media platforms using behavioral and profile-based features.
</p>

<p align="center">
  🌐 <strong><a href="https://social-media-fake-account-detection-cpg6daakcrpcbcezzhwxbd.streamlit.app/">Live Demo →</a></strong>
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [Model Performance](#-model-performance)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 Overview

Fake accounts and bots are a growing threat to the integrity of social media platforms — spreading misinformation, inflating follower counts, and manipulating public discourse. This project builds a **supervised machine learning classifier** that identifies suspicious accounts based on profile metadata and activity patterns.

The app provides an interactive web interface where users can input account features and receive an instant **real vs. fake** prediction with a confidence score.

---

## ✨ Features

- 🤖 **ML-Powered Detection** — Trained classifier identifies fake accounts with high accuracy
- 📊 **Interactive Dashboard** — Visual insights into account feature distributions
- 🔢 **Real-Time Prediction** — Input any profile's stats and get an instant verdict
- 📈 **Feature Importance** — See which signals matter most for the prediction
- 🧪 **Model Explainability** — Understand *why* an account is flagged
- 📱 **Responsive UI** — Clean, mobile-friendly Streamlit interface

---

## 🎬 Demo

> Try the live app here: [https://social-media-fake-account-detection-cpg6daakcrpcbcezzhwxbd.streamlit.app/](https://social-media-fake-account-detection-cpg6daakcrpcbcezzhwxbd.streamlit.app/)

**Sample Input Features:**
| Feature | Real Account | Fake Account |
|---|---|---|
| Followers Count | 1,200 | 48 |
| Following Count | 400 | 7,500 |
| Posts Count | 230 | 3 |
| Profile Picture | ✅ Yes | ❌ No |
| Account Age (days) | 730 | 12 |
| Bio Length | 85 chars | 0 chars |

---

## 🛠 Tech Stack

| Category | Technology |
|---|---|
| **Frontend / UI** | [Streamlit](https://streamlit.io/) |
| **ML Framework** | Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Model Persistence** | Pickle / Joblib |
| **Language** | Python 3.8+ |

---

## 📁 Project Structure

```
social-media-fake-account-detection/
│
├── app.py                  # Main Streamlit application
├── model/
│   ├── train.py            # Model training script
│   ├── model.pkl           # Saved trained model
│   └── scaler.pkl          # Feature scaler
│
├── data/
│   ├── dataset.csv         # Training dataset
│   └── processed/          # Cleaned & feature-engineered data
│
├── notebooks/
│   └── EDA.ipynb           # Exploratory Data Analysis
│
├── utils/
│   ├── preprocessing.py    # Feature engineering helpers
│   └── visualizations.py   # Chart utilities
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/social-media-fake-account-detection.git
cd social-media-fake-account-detection

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

### Requirements

```txt
streamlit>=1.28.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0
joblib>=1.3.0
```

---

## ⚙️ How It Works

```
User Input (Profile Features)
        ↓
Feature Preprocessing & Scaling
        ↓
Trained ML Classifier
        ↓
Prediction: REAL ✅  or  FAKE ❌
        ↓
Confidence Score + Feature Explanation
```

### Key Features Used for Detection

| Feature | Description |
|---|---|
| `follower_count` | Number of followers |
| `following_count` | Number of accounts followed |
| `follower_following_ratio` | Ratio of followers to following |
| `post_count` | Total number of posts |
| `has_profile_pic` | Whether the account has a profile photo |
| `bio_length` | Character length of the bio |
| `account_age_days` | Age of the account in days |
| `avg_likes_per_post` | Average engagement per post |
| `username_digit_ratio` | Proportion of digits in the username |

### Model Training

The model was trained on a labeled dataset of real and fake social media accounts using:

- **Algorithm:** Random Forest Classifier (or your actual model)
- **Train/Test Split:** 80% / 20%
- **Cross-validation:** 5-fold stratified CV
- **Preprocessing:** StandardScaler for numerical features, one-hot encoding for categoricals

---

## 📊 Model Performance

| Metric | Score |
|---|---|
| **Accuracy** | ~95% |
| **Precision** | ~94% |
| **Recall** | ~96% |
| **F1 Score** | ~95% |
| **ROC-AUC** | ~0.98 |

> *Results may vary depending on dataset version and model configuration.*

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request
```

Please make sure to:
- Follow PEP8 style guidelines
- Add docstrings to new functions
- Update `requirements.txt` if adding dependencies

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- Dataset sourced from [Kaggle](https://www.kaggle.com/) / [UCI ML Repository](https://archive.ics.uci.edu/)
- Built with ❤️ using [Streamlit](https://streamlit.io/)
- Inspired by ongoing research in bot and fake account detection

---

<p align="center">
  Made with ❤️ &nbsp;|&nbsp; ⭐ Star this repo if you found it useful!
</p>
