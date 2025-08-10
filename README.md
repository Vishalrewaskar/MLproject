
# 📊 Student Performance Predictor 

A complete end-to-end machine learning project to predict student performance based on academic and socio-economic data. The project covers everything from data ingestion to model deployment, using a custom training pipeline to select the best model exceeding an R² threshold of 0.6.

The final model (Ridge Regression) achieved an R² score of 0.88 on the test set.
Deployed via Flask, containerized using Docker, and published to DockerHub.


## 🚀 Features

- End-to-end model training pipeline with automated best-model selection.
- Comparison of 9 regression algorithms with hyperparameter tuning.
- Complete EDA, feature engineering, and preprocessing for numerical & categorical features.
- Flask API for real-time predictions.
- Dockerized application for consistent deployment.



## 📦 Tech Stack

- Python, Flask
- Scikit-learn, XGBoost, CatBoost
- Pandas, NumPy, Matplotlib, Seaborn
- Docker for containerization
## 🛠️ Installation

1. Clone the repository:

```bash
  git clone https://github.com/<your-username>/student-performance.git
  cd student-performance


```
2. Create a virtual environment and install dependencies:

```bash
  ppython -m venv venv
  source venv/bin/activate   # For Linux/Mac
  venv\Scripts\activate      # For Windows

  pip install -r requirements.txt

```
##  💻 Run Locally

Start the Flask app:

```bash
  python app.py
```
Open your browser and go to http://127.0.0.1:5000/

##  🐳 Docker Deployment

Build the Image

```bash
  docker build -t student-performance:latest .

```

Run the Container

```bash
  docker run -p 5000:5000 student-performance:latest
```

Push to Docker Hub
```bash
  docker tag student-performance:latest vishalrewaskar007/student-performance:tagname
  docker push vishalrewaskar007/student-performance:tagname

```


## 📁 Project Structure

```bash
Student_Performance_Predictor/
│
├── .ebextensions/
├── artifacts/
├── catboost_info/
├── logs/
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
├── setup.py
└── .gitignore

```
## 📌 How It Works

**1. Data Ingestion →** Loads dataset and splits into train/test sets.

**2. Data Transformation →** Preprocessing pipeline for numerical & categorical features.

**3. Model Training →** Trains 9 regression models, selects the best with R² > 0.6.

**4. Deployment →** Flask API for predictions, packaged into Docker for easy deployment.

## 📤 Deployment

- Flask used for building a lightweight API

- Easily deployable to platforms like Heroku, Render, or Railway


## 🤝 Contributing

Contributions are welcome! Fork the repo and open a pull request.




## License

This project is licensed under the [MIT License.](https://choosealicense.com/licenses/mit/)

