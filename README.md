## Books's rating prediction

### Organization and structure
Our team firstly met online to define our different tasks and organization. It was deemed convenient to use GITHub for 
our project repository and work management tool, leaving the Master branch clean, each one creating an individual branch 
from it to work on the assigned tasks and a DEV branch to merge the updates for review before moving them to Master by 
the end of the project. The task assignment was structured as follows:

- **Souheil**: GitHub administration, data analysis, feature engineering, data cleaning for base dataset to be used by the team, 
partnering with Hugues on specific feature engineering and data cleaning for a logistic regression model and overall review
- **Hugues**: overall review, data analysis, partnering with Suheil on specific feature engineering and data cleaning for a logistic regression model, exploration on implementing an experimental smote
- **Yulu**: data analysis, specific feature engineering and data cleaning for a linear regression model 
- **Richard**: data analysis, specific feature engineering and data cleaning for a decission tree model 
- **Laurence**: data analysis, general feature engineering and overall review

We used teams to share our different advancements and request support from other team members. On top of it we scheduled 
4 online meetings to review project advancement and planify the additional steps to follow.

Our main challenges were mainly related to the type of the data we had access to and how they could be used to have a good 
result in our models, and figure out how to work as a team, although we weren’t in the same campus and never met physically.


### Description
A machine learning project aiming to present an end-to-end pipeline for predicting books' ratings.

The repository contains multiple python scripts and jupyter notebooks presenting the different steps through building 
and evaluating a machine learning model.

This work is part of an ML course

 - **Author**: 
     - Souheil Maatoug
     - Hugues Delattre
     - Ricardo Requena Delon
     - Yulu Wang
     - Laurence James
     
   **Date of last update**: 27/08/2023



The developed models are based on data collected from the social cataloging website [Goodreads](www.goodreads.com) 
and hold basic information about books as well as real user experience information (average rating, number of reviews, ...).

### Contents
The repository is structured as follows:
- `data`: contains raw and modified data
  - books.csv (raw data)
  - books_clean.csv (data with minor modifications by hand)
  - clean_books_automated.csv (data with minor modifications by an automated program)
  - books_analysis_output.csv (data after pre-processing from the first notebook)

- `scripts`: contains python scripts used in the pipeline (preprocessing), the README report and requirements
  - gitignore.txt
  - README.md
  - requirements.txt
  - normalize-data.py

- `notebooks`: contains a collection of different notebooks about exploring the data, building a model and evaluating it. 1 preprocessing notebook and 3 ML notebooks
  - dataset-exploration.ipynb (preprocessing notebook)
  - linear_regression.ipynb 
  - classification_decision_tree.ipynb
  - classification_logistic_regression.ipynb

## A brief overview:

**It is suggested to browse through the notebooks from preprocessing (dataset-exploration) to ML models and each notebook is commented and mostly self-explanatory.**

**dataset-exploration.ipynb**

The first notebook, dataset-exploration.ipynb, reviews the data, how to open it, explore it and preprocess it.
It first produces a "books_clean.csv" by removing the structural error before analyzing it's content.

Through it we learn the content of each columns, its duplicates, its structure and its distribution.

These are the columns treated:
---  ------              --------------  -----  
 0   bookID              11127 non-null  int64  
 1   title               11127 non-null  object 
 2   authors             11127 non-null  object 
 3   average_rating      11127 non-null  float64
 4   isbn                11127 non-null  object 
 5   isbn13              11127 non-null  int64  
 6   language_code       11127 non-null  object 
 7   num_pages           11127 non-null  int64  
 8   ratings_count       11127 non-null  int64  
 9   text_reviews_count  11127 non-null  int64  
 10  publication_date    11127 non-null  object 
 11  publisher           11127 non-null  object 

Through out the whole notebook, each column is being investigated, commented on whether or not it is usable in a notebook and preprocessed if it can be used.

The preprocessing includes for instance : 
- The removal of justified outliers
- The removal of apparently useless data (isbn/isbn13 being identifiers for instance)
- The transformation of the columns into others (publication_date being transfered into a year and months column for instance)

The pre-processed data is being exported as "books_analysis_output.csv"

**linear_regression.ipynb**

The second notebook, linear_regression.ipynb, contains a first modelization from the preprocessed data as it is with a Linear Regression Model.

Its results are as follow:

- **Mean Squared Error (MSE):** 0.07416325833412434
- **Mean Absolute Error (MAE):** 0.21242995946499926
- **R-squared (R2) Score:** 0.03428519568010524
- **Cross-Validation Scores:** [0.04932286 0.01271813 0.02139295 0.03089471 0.02067053]
- **Average CV Score:** 0.026999834867191996

**Interpretation:**
- **MSE:** On average, the squared difference between predicted and actual average ratings is 0.074, indicating improved accuracy.
- **MAE:** The predicted ratings are off by approximately 0.212 from actual ratings on average, showing better accuracy.
- **R2 Score:** About 3.4% of the variance in average ratings is explained by selected features, a slight improvement.
- **Cross-Validation Scores:** The model's generalization ability is consistent, with a slightly improved average score.

**classification_decision_tree**

The third notebook, classification_decision_tree, contains another modelization from the preprocessed data using a different approach and using a Decision Tree.

Its results are as follow:

- **Mean Squared Error (MSE):** 0.4031148134733792
- **Mean Absolute Error (MAE):** 0.3994929373415429
- **R-squared (R2) Score:** -0.5259900584475881
- **accuracy on training set** :  0.6430037426053362
- **accuracy on test set** :  0.6023180007243752
- **f1-score on training set** :  0.2781907554614287
- **f1-score on test set** :  0.24048228983846248

**Interpretation:**
We have a much higher R2 Score that could be attributed to overfitting as this model used much more features.
This model seems to have a much better accuracy and it's accuracy seems to be transferred from the training set to the test set.

**classification_logistic_regression**

The fourth notebook, classification_logistic_regression, contains a final modelization from the preprocessed data using yet another approach and using a Logistic Regression.


Its initial comparable results are as follow:

**Mean Squared Error**: 0.3955773955773956
**R-squared**: -0.500792458361581

Which puts it into a very comparable position as the previous classification_decision_tree model.

It has been updated since and now uses a different approach including a new subdivision where instead of labeling the grades into classes [1,2,3,4], it labels them [1,2,3,4,5] but they do not match with the previous grade as the grades are shifted:
1=[0-3.5] 2=[3.5-3.75] 3=[3.75-4] 4=[4-4.25] 5=[4.25-5]

This leads to a new result but that is not comparable to others:
**Mean Squared Error**: 1.1425061425061425
**R-squared**: 0.02512087666644558

This final version of the model is less overfitting data and includes more information about "out of boundaries" grades but it is much less efficient at finding usual grades around the 3-4 area.

As a final exploration, a smoted version of this final model has been attempted to tackle this loss of fitting.

Its final result gives:
**Mean Squared Error**: 3.8113022113022113
**R-squared**: -2.2521128948709883


---


