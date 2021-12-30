# Real_Estate_Price_Prediction
## End-to-End Machine Learning Project

The data used in this project is downloaded from Kaggle 'https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data' and also the dataset is provided in the folder 'model'.

The mojor steps involved in this project,

1. Data Preprocessing
2. Model Building
3. Model Deployment

## 1.Data Preprocessing

Data cleaning, Feature Engineering and Outlier Detection have been explained in detail in the Notebook. The Notebook is present in the folder 'model'.

## 2. Model Building

The model was trained using different candidate models with different parameters. Using GridSearch the best model 'Logistic Regression' with best parameters is obtained. 

## 3. Model Deployment

The Logistic Regression model is deployed. For backend, using the Python Flask for the http server and the for the frontend a Website is created using html, css and javascript. This has been deployed in the NGINX Web Server. This predicts the value of the specified property by taking the inputs such as 'Area', 'Number of bedrooms', 'Number of bathrooms' and 'location' from the user.

**The Notebook provides the detailed explanation about model building and the model deployment. Also, screenshots of Postman collections testing of the Endpoints are shown.**

## Aplication Endpoints are,

**1. /get_location_names**

**2. /price_prediction**





