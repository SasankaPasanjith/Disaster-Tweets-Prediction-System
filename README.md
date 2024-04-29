# Disaster-Tweets-Prediction-System
This repository contains my Machine Learning model for the Natural Language Processing with Disaster Tweets competition on Kaggle, along with the AI mini-project developed in connection with it.

This project is designed to help users determine whether a tweet or sentence relates to a disaster or not. The application utilizes machine learning techniques and is connected to the app through pickle. To evaluate the model, I tested several machine learning algorithms, including Support Vector Machine, Decision Tree, K Nearest Neighbors, Random Forest, and Logistic Regression. Among these, the Logistic Regression algorithm performed the best with the highest accuracy.

## Special Libraries Used to Model Development
* NLTK = Natural language tool kit
* nltk.corpus stopwords = Various languages stopwords.
* sklearn = For ML algorithems & other evaluation stuffs
* re = Regular expression library for text cleaning
* TfidfVectorizer = Converting text data into TF-IDF (numerical values)

## Technologies

* Python, Streamlit, Jupyter Notebooks

##  Prerequisites
* Python 3
* Anaconda navigator or any other related software

## How to Run the Project
* Clone this repository into your local machine.
* Open the Anaconda prompt.
* Provide the correct directory where the relevant code is located
  e.g : D:
        cd NLP disaster tweets\Source code
* After getting to the correct directory, if streamlit is not installed on the computer, install it.
    use this command : pip install streamlit
* Using the name given to the Python project, type as follows and enter
   e.g : streamlit run app.py
* Then the relevant project is run through the web browser.

* Enter the tweet you want in the textbox and press the "Predict Tweet" button.

* According to the Tweet you entered, the result will appear below on the same page.


![Kaggle Leaderboard](https://github.com/SasankaPasanjith/Disaster-Tweets-Prediction-System/blob/main/img/Kaggle%20Leaderboard.png)

*Kaggle Leaderboard* 

![Homepage](https://github.com/SasankaPasanjith/Disaster-Tweets-Prediction-System/blob/main/img/home.PNG)

*Homepage of the System*

![Non disaster Tweets](https://github.com/SasankaPasanjith/Disaster-Tweets-Prediction-System/blob/main/img/not%20disaster.PNG)

*Non disaster Tweets*

![Disaster Tweets](https://github.com/SasankaPasanjith/Disaster-Tweets-Prediction-System/blob/main/img/disaster%20tweets.PNG)

*Disaster Tweets*
