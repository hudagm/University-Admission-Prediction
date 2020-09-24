# University Admission Prediction
Using the supplied predictive variables (GRE score, TOEFL score, University Rating, etc) to predict the likelihood of admission of a new candidate aspiring for graduate schools. 
Deployed on Heroku: https://uni-admission-predict.herokuapp.com/

## Tasks 
- Exploratory Data Analysis (EDA)
- Data Visualization
- Trained and tested on various models and evaluated their corresponding losses and accuracies
- Evaluated KPIs of the best model
- Used the model to predict on new data to evaluate the possibility of a student getting into a university

## Data
Dataset used in this task ('Admission_Predict.csv') is from https://www.kaggle.com/mohansacharya/graduate-admissions. The dataset contains several parameters which are considered important during the application for Masters Programs.
### Input
- GRE Scores (out of 340)
- TOEFL Scores (out of 120)
- University Rating (out of 5)
- Statement of Purpose (out of 5)
- Letter of Recommendation Strength (out of 5)
- Undergraduate GPA (out of 10)
- Research Experience (either 0 or 1)
### Output
- Chance of Admit (ranging from 0 to 1)

## Models Used
Artificial Neural Network, Decison Tree, Random Forest, and Linear Regressor.

## Requirements
Install requirements.txt file to make sure correct versions of libraries are being used.
  - Python 3.6x
  - Numpy 1.15.0
  - Pandas 0.23.3
  - Tensorflow 2.1.0
  - Scikit-learn 0.22.1
  - Matplotlib 2.2.2
  - Seaborn 0.10.1

## Todos
- Perform MORE EDA
- Shortlist the features to 3-4 features
- Predict on other models
- Lower the RMSE even more

## License
[MIT](https://choosealicense.com/licenses/mit/)
