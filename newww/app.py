from flask import Flask, render_template, request, redirect, url_for # pyright: ignore[reportMissingImports]
import numpy as np # type: ignore
import pickle

app = Flask(__name__)

# Load the trained models for different age groups
children_model = pickle.load(open('models\\childrenmodel.pkl', 'rb'))
adolescent_model = pickle.load(open('models\\adolescentmodel.pkl', 'rb'))
young_model = pickle.load(open('models\\youngmodel.pkl', 'rb'))
adult_model = pickle.load(open('models\\adultmodel.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    age_group = request.form['age_group']
    if age_group == 'children':
        return redirect(url_for('predict_children'))
    elif age_group == 'adolescent':
        return redirect(url_for('predict_adolescent'))
    elif age_group == 'young':
        return redirect(url_for('predict_young'))
    elif age_group == 'adult':
        return redirect(url_for('predict_adult'))
    else:
        return 'Invalid age group'

@app.route('/predict_children', methods=['GET', 'POST'])
def predict_children():
    if request.method == 'POST':
        children_inputs = {
            'A1': request.form['A1'],
            'A2': request.form['A2'],
            'A3': request.form['A3'],
            'A4': request.form['A4'],
            'A5': request.form['A5'],
            'A6': request.form['A6'],
            'A7': request.form['A7'],
            'A8': request.form['A8'],
            'A9': request.form['A9'],
            'A10_Autism_Spectrum_Quotient': request.form['A10_Autism_Spectrum_Quotient'],
            'Age_Years': request.form['Age_Years'],
            'Jaundice': request.form['Jaundice'],
            'Family_mem_with_ASD': request.form['Family_mem_with_ASD'],
            'Who_completed_the_test_Family_Member': request.form['Who_completed_the_test_Family_Member'],
            'Who_completed_the_test_Health_Care_Professional': request.form['Who_completed_the_test_Health_Care_Professional']
        }

        children_input_array = np.array([list(children_inputs.values())])
        children_prediction = children_model.predict(children_input_array)
        children_result = 'Yes,Autism has been identified.' if children_prediction[0] == 1 else 'No,Autism has not been identified.'

        return render_template('result.html',selected_age_group='children', children_result=children_result)
    else:
        return render_template('children_questions.html')

@app.route('/predict_adolescent', methods=['GET', 'POST'])
def predict_adolescent():
    if request.method == 'POST':
        adolescent_inputs = {
            'A1': request.form['A1'],
            'A2': request.form['A2'],
            'A3': request.form['A3'],
            'A4': request.form['A4'],
            'A5': request.form['A5'],
            'A6': request.form['A6'],
            'A7': request.form['A7'],
            'A8': request.form['A8'],
            'A9': request.form['A9'],
            'A10_Autism_Spectrum_Quotient': request.form['A10_Autism_Spectrum_Quotient'],
            'Age_Years': request.form['Age_Years'],
            'Jaundice': request.form['Jaundice'],
            'Family_mem_with_ASD': request.form['Family_mem_with_ASD'],
            'Who_completed_the_test_Family_Member': request.form['Who_completed_the_test_Family_Member'],
            'Who_completed_the_test_Health_Care_Professional': request.form['Who_completed_the_test_Health_Care_Professional']
        }

        adolescent_input_array = np.array([list(adolescent_inputs.values())])
        adolescent_prediction = adolescent_model.predict(adolescent_input_array)
        adolescent_result = 'Yes,Autism has been identified.' if adolescent_prediction[0] == 1 else 'No,Autism has not been identified.'

        return render_template('result.html',selected_age_group='adolescent', adolescent_result=adolescent_result)
    else:
        return render_template('adolescent_questions.html')

@app.route('/predict_young', methods=['GET', 'POST'])
def predict_young():
    if request.method == 'POST':
        young_inputs = {
            'A1': request.form['A1'],
            'A2': request.form['A2'],
            'A3': request.form['A3'],
            'A4': request.form['A4'],
            'A5': request.form['A5'],
            'A6': request.form['A6'],
            'A7': request.form['A7'],
            'A8': request.form['A8'],
            'A9': request.form['A9'],
            'A10_Autism_Spectrum_Quotient': request.form['A10_Autism_Spectrum_Quotient'],
            'Age_Years': request.form['Age_Years'],
            'Jaundice': request.form['Jaundice'],
            'Family_mem_with_ASD': request.form['Family_mem_with_ASD'],
            'Who_completed_the_test_Family_Member': request.form['Who_completed_the_test_Family_Member'],
            'Who_completed_the_test_Health_Care_Professional': request.form['Who_completed_the_test_Health_Care_Professional'],
            'Who_completed_the_test_Self': request.form['Who_completed_the_test_Self']
        }

        young_input_array = np.array([list(young_inputs.values())])
        young_prediction = young_model.predict(young_input_array)
        young_result = 'Yes,Autism has been identified.' if young_prediction[0] == 1 else 'No,Autism has not been identified.'

        return render_template('result.html', selected_age_group='young',young_result=young_result)
    else:
        return render_template('young_questions.html')

@app.route('/predict_adult', methods=['GET', 'POST'])
def predict_adult():
    if request.method == 'POST':
        adult_inputs = {
            'A1': request.form['A1'],
            'A2': request.form['A2'],
            'A3': request.form['A3'],
            'A4': request.form['A4'],
            'A5': request.form['A5'],
            'A6': request.form['A6'],
            'A7': request.form['A7'],
            'A8': request.form['A8'],
            'A9': request.form['A9'],
            'A10_Autism_Spectrum_Quotient': request.form['A10_Autism_Spectrum_Quotient'],
            'Age_Years': request.form['Age_Years'],
            'Jaundice': request.form['Jaundice'],
            'Family_mem_with_ASD': request.form['Family_mem_with_ASD'],
            'Who_completed_the_test_Family_Member': request.form['Who_completed_the_test_Family_Member'],
            'Who_completed_the_test_Health_Care_Professional': request.form['Who_completed_the_test_Health_Care_Professional'],
            'Who_completed_the_test_Relative': request.form['Who_completed_the_test_Relative'],
            'Who_completed_the_test_Self': request.form['Who_completed_the_test_Self']
        }

        adult_input_array = np.array([list(adult_inputs.values())])
        adult_prediction = adult_model.predict(adult_input_array)
        adult_result = 'Yes,Autism has been identified.' if adult_prediction[0] == 1 else 'No,Autism has not been identified.'

        return render_template('result.html', selected_age_group='adult',adult_result=adult_result)
    else:
        return render_template('adult_questions.html')

if __name__ == '__main__':
    app.run(debug=True)