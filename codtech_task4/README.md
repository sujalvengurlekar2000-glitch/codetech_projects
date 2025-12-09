#MACHINE LEARNING MODEL IMPLEMENTATION(SPAM CLASSIFICATION)

*COMPANY NAME*:CODTECH IT SOLUTIONS

*NAME*:SUJAL VENGURLEKAR

*INTERN ID*:CT06DR2365

*DOMAIN*:PYTHON PROGRAMMING

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTOSH

*TASK DESCRIPTION*

This project is part of CODTECH Python & Machine Learning Internship – Task 4,
where the objective is to build a predictive machine learning model using Scikit-learn. The chosen application for this task is SMS Spam Detection, 
a classic text classification problem.
In this project, a dataset of SMS messages is processed, cleaned, and transformed into numerical features using TF-IDF vectorization.
A Multinomial Naive Bayes algorithm is then trained to classify messages as “spam” or “ham” (not spam).
This project demonstrates the complete pipeline of a ML model—data loading, preprocessing, vectorization, model training, evaluation, and prediction. 
It is simple but very practical and widely used in real-world applications.

> Tools & Technologies Used

Programming & Libraries

Python 3 – Main language used for building the ML pipeline

Pandas – For loading and processing datasets

Scikit-learn (sklearn) –

train_test_split for splitting data

TfidfVectorizer for text vectorization

MultinomialNB for model training

accuracy_score, classification_report, confusion_matrix for evaluation


Development Environment

Jupyter Notebook / Google Colab / WPS Office Notebook


> Project Workflow

1. Dataset Loading

SMS dataset loaded from GitHub

Two columns: label (spam/ham) and message


2. Data Preprocessing

Labels converted from text to numeric (ham=0, spam=1)


3. Train-Test Split

Dataset split into 80% training and 20% testing


4. Text Vectorization

TF-IDF Vectorizer converts text messages into numerical vectors

Stops words removed to improve accuracy


5. Model Training

Multinomial Naive Bayes used (best algorithm for text classification)


6. Model Evaluation

The trained model achieved:

Accuracy: ~97.8%

High precision & recall for both spam and ham classes

Confusion Matrix shows strong classification performance


7. Prediction Function

A custom function check_spam(text) predicts whether a new input message is SPAM or NOT SPAM.


> Where This Project is Applicable

This kind of predictive model is used widely in many industries. Some real-world applications include:

* Email Spam Detection

Automatically classifies incoming emails as spam or important.

*SMS Filtering in Mobile Networks

Telecom operators use similar models to filter fraudulent or promotional messages.

* Fraud Detection

Identifying phishing messages, scam attempts, or fake lottery notifications.

*Customer Support Automation

Detecting spam or irrelevant content in customer messages.

*Text Classification Tasks

This model can be adapted for:

Sentiment analysis

Fake news detection

Toxicity classification

Complaint categorization


*Cyber Security Applications

Early detection of malicious links or harmful content.


*OUTPUT*:
