from flask import Flask, request, render_template
import joblib
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Load vectorizers
vectorizer_hr_vs_hf = joblib.load('tfidf_vectorizer_hr_vs_hf.joblib')
vectorizer_mr_vs_mf = joblib.load('tfidf_vectorizer_mr_vs_mf.joblib')
vectorizer_human_machine = joblib.load('tfidf_vectorizer_human_machine.joblib')

# Load models
svm_hr_vs_hf = joblib.load('svm_hr_vs_hf.joblib')
svm_mr_vs_mf = joblib.load('svm_mr_vs_mf.joblib')
svm_human_machine = joblib.load('svm_human_machine.joblib')

def preprocess_text(text):
    # Normalize text to lowercase
    text = text.lower()

    # Remove unwanted characters
    text = re.sub(r'\W', ' ', text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]  # remove single character words

    # Rejoin tokens into a single string
    return ' '.join(tokens)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        if not text.strip():
            error = "Text is required to perform classification."
            return render_template('index.html', prediction='', message='', text=text, error=error)
        prediction, message = classify_text(text)
        return render_template('index.html', prediction=prediction, message=message, text=text, error='')
    return render_template('index.html', prediction='', message='', text='', error='')

def classify_text(text):
    features_human_machine = vectorizer_human_machine.transform([text])
    human_or_machine = svm_human_machine.predict(features_human_machine)[0]

    if human_or_machine == 0:
        features_hr_vs_hf = vectorizer_hr_vs_hf.transform([text])
        real_or_fake = svm_hr_vs_hf.predict(features_hr_vs_hf)[0]
        if real_or_fake == 0:
            category = 'Human: Real'
            likelihood_message = "This text is highly likely written by a real human and contains genuine content."

            category = 'Human: Fake'
            likelihood_message = "This text is highly likely written by a human but contains some fabricated or misleading content."

    else:
        features_mr_vs_mf = vectorizer_mr_vs_mf.transform([text])
        real_or_fake = svm_mr_vs_mf.predict(features_mr_vs_mf)[0]
        if real_or_fake == 0:
            category = 'Machine: Real'
            likelihood_message = "This text is highly likely generated by a machine but contains accurate information."

        else:
            category = 'Machine: Fake'
            likelihood_message = "This text is highly likely generated by a machine and contains fabricated or misleading content."

    return category, likelihood_message


if __name__ == '__main__':
    app.run(debug=True)

