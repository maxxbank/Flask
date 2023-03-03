# framework for web libraries
import flask # framework for web
from flask import render_template

# Load damps and loads libraries
import pickle # damps and loads data

# Load the Sklearn libraries
import sklearn
from sklearn.linear_model import LinearRegression

#print('Hello flask')

app = flask.Flask(__name__, template_folder = 'templates') #хранение HTML шаблоном в директории

@app.route('/', methods = ['POST', 'GET']) #декораторы на странице

@app.route('/index', methods = ['POST', 'GET']) #декораторы на странице
def main():
   if flask.request.method == 'GET':
         return render_template('main.html') # возвращаем шаблом HTML
   
   if flask.request.method == 'POST':
        with open('lr_model.pkl', 'rb') as f: #открытие модели в режиме чтение
             loaded_model = pickle.load(f)
        
        exp = float(flask.request.form['experience']) #передаем данные с HTML форм
        y_pred = loaded_model.predict([[exp]])

        return render_template('main.html', result = y_pred)

if __name__ == '__main__':
   app.run()

