# 🛡️ YT Sanitizer: YouTube Spam Detection and Filtering System

YT-Sanitizer is a machine learning-based text classification system designed to detect and filter spam comments across various YouTube artist channels. By leveraging Natural Language Processing (NLP) and supervised learning, this project achieves high generalization across different content creators.

---

## 📊 Dataset Overview

The project utilizes five distinct CSV datasets representing YouTube comment sections for major artists:
- **Artists:** Psy, Katy Perry, LMFAO, Eminem, and Shakira.
- **Structure:** Each dataset contains the comment text (`CONTENT`) and a binary label (`CLASS`), where **1 = Spam** and **0 = Not Spam (Ham)**.
- **Consolidation:** The individual files are merged into a single master dataframe (`df_all`) for robust training and cross-artist validation.
- **Source:** https://archive.ics.uci.edu/dataset/380/youtube+spam+collection

---  

## Features

- Detect spam comments automatically  
- Preprocess text data with NLP techniques  
- Multiple ML models for comparison  
- Model evaluation and visualization  
- Clean and modular project structure suitable for collaboration

---

## 🛠️ Technical Workflow  
### 1. Data Preprocessing
- **Concatenation:** Merging multiple sources into a unified feature set.
- **Cleaning:** Removal of unnecessary columns (e.g., `COMMENT_ID`, `AUTHOR`, `DATE`) to focus purely on text patterns.
- **Shuffling:** Randomizing the data to ensure the model doesn't learn sequence-based biases.

### 2. Feature Engineering
Utilized TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization to convert raw text into numerical vectors.
- **Stop Words:** Common English words are removed to highlight unique "spammy" keywords.
**N-grams:** The model considers both single words and word pairs (unigrams and bigrams) to capture context like "check out" or "my channel."

### 3. Model Architecture
The champion model is **Logistic Regression**, chosen for its:
- **Efficiency:** Fast training and low latency for real-time inference in the Streamlit app.
- **Explainability:** High transparency in how specific words contribute to a "Spam" score.
- **Stability:** Excellent performance in "Leave-One-Artist-Out" cross-validation.
 
### 4. Evaluation Metrics
The model was tested against an unseen artist (Shakira) to verify its real-world effectiveness:
- **Accuracy:** ~92%
- **Spam Precision:** ~99% (Minimizing "False Positives" to ensure real fans aren't blocked).
- **Generalization:** The model successfully identifies spam patterns regardless of the specific artist's fanbase language.

---

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/YT-Sanitizer.git  
cd YT-Sanitizer  
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```

3. **Activate the environment**
```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. **Install required packages**
```bash
pip install -r requirements.txt
```

5. **Set up Jupyter kernel**
```bash
python -m ipykernel install --user --name yt_sanitizer --display-name "Python (YT Sanitizer)"
```

6. **Launch the UI**  
```bash
streamlit run app.py
```


