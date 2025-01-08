from flask import Flask, request , render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/get_random_number', methods=['POST'])
def get_random():
    try:
        first_num = int(request.form['first_num'])
        second_num = int(request.form['second_num'])
        num_result = randint(first_num, second_num)
        return str(num_result)
    except (ValueError, KeyError) as e:
        return f'Ошибка данных {e}', 400 
    except Exception as e:
        return 'Ошибка {}'.format(e), 500

if __name__ == '__main__':
    app.run(debug=True)
