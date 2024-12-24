# Detecting AI-Generated Disinformation in News Media

## Project Overview

In today's digital age, ensuring the credibility of news is paramount, as even reputable journalism platforms face challenges from AI-generated disinformation. This project addresses the critical issue of distinguishing between human-written and AI-generated news articles, particularly identifying authentic versus fake content.

We developed a machine learning framework to classify news articles into four categories:
- **Human Real (HR)**
- **Human Fake (HF)**
- **Machine Real (MR)**
- **Machine Fake (MF)**

The goal is to enhance the integrity of news dissemination and combat the spread of misinformation.

## Research Question

*How effective are different machine learning models at differentiating between human-generated and AI-generated fake news?*

## Dataset

The dataset used for this project was sourced from **GossipCop++** and **PolitiFact++**, encompassing:
- **Celebrity gossip and entertainment news**
- **Political news and fact-checking**

### Key Features
- **Text:** Main body of the news article.
- **Title:** Headline of the article.
- **Description:** Brief summary of the article.

## Methodology

### Text Preprocessing
1. **Cleaning:** Removing HTML tags, punctuation, and special characters.
2. **Tokenization:** Splitting text into tokens for analysis.
3. **Stopword Removal:** Removing common, non-predictive words.
4. **TF-IDF Vectorization:** Extracting meaningful features for classification.

### Machine Learning Models
We evaluated and compared the following models:
- **Logistic Regression**
- **Naive Bayes**
- **XGBoost**
- **Support Vector Machines (SVM)**

### Results
- **SVM** emerged as the top-performing model, achieving high accuracy across all tasks.
- Logistic Regression and Naive Bayes exhibited overfitting and sensitivity to training data.
- **XGBoost** performed well in specific cases but required additional tuning.

## Deliverable: Web Application

A Flask-based web application was developed, allowing users to:
- Input news article text.
- Classify the article into one of the four categories (HR, HF, MR, MF).

This application provides an intuitive interface for detecting the authenticity of news articles.

## Future Work

- **Dataset Expansion:** Collecting data from diverse genres and languages to improve generalization.
- **Advanced Models:** Exploring Large Language Models (LLMs) and hybrid architectures.
- **Feature Analysis:** Conducting a deeper analysis of linguistic patterns.
- **Collaboration:** Open-sourcing the project to foster innovation and transparency.

## Conclusion

This project demonstrates the potential of machine learning in identifying AI-generated disinformation, laying the groundwork for tools that preserve the integrity of news dissemination in the digital era.

---
