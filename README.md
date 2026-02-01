# Detection of Autism Using Machine Learning

This project aims to enhance the detection of Autism Spectrum Disorder using advanced machine learning techniques and a user-friendly web interface. A multi-dataset approach is adopted, incorporating data from four age groups — **Children, Adolescents, Young Adults, and Adults** — to increase diagnostic accuracy across the lifespan.

## ✅ Key Features

- Multi-dataset integration for diverse age groups

- Interactive web-based prediction tool

- Real-time model predictions

- Modular and extensible architecture

## 🧪 Technologies Used

- **Python**
- **Flask** – Web application framework
- **HTML/CSS** – Frontend design
- **Jupyter Notebook** – Data analysis and model training
- **VS Code** – Development environment
- **Scikit-learn / Pandas / NumPy / Matplotlib** – (assumed common ML stack)

## 🧠 Machine Learning Approach

- **Data Preprocessing**: Cleaning, normalization, and handling missing values
- **Feature Selection**: Correlation analysis and importance ranking
- **Model Training**: Multiple algorithms tested with cross-validation
- **Evaluation**: Accuracy, precision, recall, F1-score
- **Deployment**: Trained models integrated into a Flask web application

## 🌐 Web Interface

The system provides a responsive and user-friendly interface built with Flask, allowing users to:

- Select their age group
- Fill out an ASD-related questionnaire
- Submit responses to receive real-time predictions


## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` for package management

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/asd-detection-ml.git
cd asd-detection-ml
Install dependencies:
pip install -r requirements.txt
Run the flask app 
python app.py
Open your browser and go to:
http://localhost:5000


## Project Structure : 

├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── models/
│   └── trained_models.pkl
├── datasets/
│   └── [Multiple age group datasets]
├── notebooks/
│   └── data_analysis.ipynb
└── README.md

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

