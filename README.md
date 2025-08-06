
# 📊 Student Performance Predictor 

A complete end-to-end machine learning project that predicts student performance based on academic and socio-economic data. This project follows industry best practices for structuring, version control, data processing, model development, and deployment using Flask.


## 🚀 Features

- Data ingestion and preprocessing pipeline
- EDA and data validation
- Model training with hyperparameter tuning
- Prediction pipeline
- Flask-based deployment
- Modular and production-ready structure


## 📦 Tech Stack

**Programming Language:** Python

**Libraries & Tools:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Flask

**Version Control:** Git & GitHub

**Logging & Exception Handling:** Custom implementation

## 🛠️ Installation

Clone the repository:

```bash
  git clone https://github.com/your-username/Student_Performance_Predictor.git
  cd Student_Performance_Predictor

```
Create a virtual environment and install dependencies:

```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt
```
##  💻 Run Locally

Start the Flask app:

```bash
  python app.py
```
Open your browser and go to http://127.0.0.1:5000/
## 📁 Project Structure

```bash
Student_Performance_Predictor/
├── artifacts/                  # Saved datasets and model files
├── src/                        # Core project source code
│   ├── components/             # Data ingestion, transformation, training modules
│   ├── pipeline/               # Training and prediction pipelines
│   └── utils/                  # Utility and helper functions
├── templates/                  # HTML templates for Flask frontend
├── app.py                      # Flask app for deployment
├── requirements.txt
└── README.md

```
## 📈 Lessons Learned

- Structuring an ML project for scalability and reusability
- Building custom data pipelines
- Importance of clean data validation and transformation
- Deploying models using Flask in a simple web interface

## 📤 Deployment

- Flask used for building a lightweight API

- Easily deployable to platforms like Heroku, Render, or Railway


## 🤝 Contributing

Contributions are welcome! Fork the repo and open a pull request.




## License

[MIT](https://choosealicense.com/licenses/mit/)

