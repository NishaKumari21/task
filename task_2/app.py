from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract features from the form
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])[0]
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
