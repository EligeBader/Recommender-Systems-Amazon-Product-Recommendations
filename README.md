# 📚 Amazon Books Product Recommender System 📚

![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![License](https://img.shields.io/badge/License-MIT-orange) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-yellow) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24.2-blue) ![Pandas](https://img.shields.io/badge/Pandas-1.2.3-green)

## 🏆 Overview
Welcome to my Amazon Books Product Recommender System project! This system recommends books to users based on various collaborative filtering techniques and SVD (Singular Value Decomposition). It features a Streamlit web app for user interaction and provides a seamless experience for book recommendations.

![Recommender System](https://img.shields.io/badge/Recommender-System-yellow) ![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-red)

## 📜 Description
The main goal of this project is to build a book recommender system using collaborative filtering and SVD. The system utilizes Amazon book ratings and provides recommendations based on user preferences. I created a Streamlit web app for an interactive recommendation experience.

## 💾 Dataset
The datasets used in this project include:
- `Books.csv`: Contains book ratings and information.
- `popular_books.csv`: Created by me after filtering books.
- `um.csv`: The utility matrix of user ratings.
- `um_repro.csv`: Reconstructed utility matrix using SVD.

## 🛠 Tools & Technologies
For this project, I used the following tools and technologies:
- **Python 3.8+**: The backbone of my project.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For collaborative filtering and SVD.
- **Streamlit**: For building the web application.
- **Jupyter Notebook**: For interactive coding and exploration.

## 🔍 Workflow

1. **Libraries and Data Reading**:
   - Imported necessary libraries including pandas, numpy, and scikit-learn.
   - Read the data from `Books.csv`.

2. **Data Preprocessing**:
   - Cleaned and prepared the data for analysis.
   - Created the `popular_books.csv` file after filtering popular books.

3. **Popularity-Based Model**:
   - Built a model based on book popularity and provided recommendations.

4. **Item-Based Collaborative Filtering**:
   - Constructed a utility matrix.
   - Built a KNN model using the utility matrix for recommendations.
   - Created `um.csv` and `um_repro.csv` files for further analysis.

5. **SVD Model**:
   - Applied SVD to the utility matrix to reduce dimensionality.
   - Reconstructed the utility matrix using SVD.
   - Evaluated the model using RMSE and explained variance ratio.

6. **Streamlit Web App**:
   - Built a Streamlit web app to provide an interactive recommendation system.
   - Users can enter their ID to get book recommendations.

## 📂 Project Structure
```
- Amazon_Books_Recommender_System
  - data/
    - Books.csv
    - popular_books.csv
    - um.csv
    - um_repro.csv
  - notebooks/
    - recommender-system.ipynb
    - webscraping.ipynb
  - streamlit_app/
    - streamlit_WebPage.py
  - models/
    - svd.pickle
    - U_sigma_Vt.pickle
    - recommender_books_svd.pickle
  - README.md
```

## 🎯 Results
After training the models, the results are saved in the `models/` directory. I evaluated the performance of my models using RMSE and explained variance ratio. The Streamlit web app provides an interactive way for users to get book recommendations.

## 📊 Graph of Results
Below is a graphical representation that compares the RMSE and explained variance for different models used in the Amazon Books Recommender System:
![RMSE vs Variance](https://github.com/EligeBader/Recommender-Systems-Amazon-Product-Recommendations/blob/main/Amazon%20Products%20Recommeneder%20System.png)


## 🌟 Improvements
To further enhance this project, I can explore the following:

- **Experiment with Different Models**:
  - Fine-tune other collaborative filtering models such as Matrix Factorization, ALS (Alternating Least Squares), and Hybrid models.
  - Incorporate content-based filtering to improve recommendations.

- **Optimize Hyperparameters**:
  - Use techniques like grid search to find the best hyperparameters for the models.

- **Feature Engineering**:
  - Explore additional text preprocessing techniques and feature engineering methods to improve model performance.
