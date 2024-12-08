# Spam Email Classification Project

## Overview
This project implements a machine learning-based spam classification system using the Naive Bayes algorithm. The goal is to develop an intelligent email filtering solution that can accurately distinguish between spam and legitimate emails.

## Internship Project | EduNet

### Project Details
- **Institution:** EduNet Internship Program
- **Duration:** November-December 2024
- **Domain:** Machine Learning & Data Science

## 🎯 Project Objectives
- Develop a robust spam classification model
- Implement Naive Bayes algorithm for email filtering
- Achieve high accuracy in spam detection
- Gain practical experience in machine learning techniques

## 🛠 Tech Stack
- **Programming Language:** Python
- **Machine Learning Libraries:** 
  - scikit-learn
  - pandas
  - numpy
- **Data Processing:** 
  - NLTK (Natural Language Toolkit)
- **Model:** Naive Bayes Classifier

## 📊 Dataset
The project utilizes a labeled dataset of emails, categorized into:
- Spam emails
- Non-spam (Ham) emails

### Data Preprocessing
- Text cleaning
- Tokenization
- Feature extraction using TF-IDF vectorization

## 🧠 Machine Learning Approach
### Naive Bayes Algorithm
Naive Bayes is chosen for its:
- Simplicity
- Efficiency with text classification
- Low computational complexity
- Good performance with small to medium-sized datasets

### Key Steps
1. Data Collection
2. Text Preprocessing
3. Feature Extraction
4. Model Training
5. Model Evaluation

## 🔍 Model Performance Metrics
- Accuracy
- Precision
- Recall

## 📈 Project Workflow
```
spam_classification/
│
├── data/
│   ├── spam.csv
│
├── notebooks/
│   ├── spam_det.ipynb
│
├── src/
│   ├── spamDetector.py
│
├── models/
│   └── naive_bayes_classifier.pkl
|   └── vectorizer.pkl
|
├── .gitignore
|
└── README.md
```

## 🚀 Setup and Installation
1. Clone the repository
```bash
gh repo clone notsolvablehat/spam_classification
cd spam_classification
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install pandas scikit-learn numpy streamlit
```

## 🧪 Running the Project
```bash
cd venv
streamlit run spamDetector.py
```

## 📝 Key Learnings
- Practical application of machine learning in email filtering
- Hands-on experience with Naive Bayes algorithm
- Data preprocessing techniques
- Model evaluation and performance measurement

## 🔮 Future Improvements
- Implement advanced feature engineering
- Explore ensemble methods
- Integrate deep learning approaches
- Real-time spam detection

## 📌 Challenges Overcome
- Handling imbalanced datasets
- Feature selection

## 👥 Contributors
- Mohammed Yaseen Agha
- Internship Mentor (Edunet)
- Abdul Aziz MD

## 📄 License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments
- EduNet Internship Program
- Open-source community
- Machine Learning libraries developers
- Abdul Aziz MD -> Mentor
