from flask import Flask, render_template, request
import langchain_helper as lc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pet')
def petGen():    
    return render_template('pet_gen.html')


@app.route('/docAssist')
def docAssist():
    return render_template('docAssist.html')

@app.route('/process', methods=['POST'])
def process():
    pet = request.form['pet']
    color = request.form['color']
    pattern = request.form['pattern']
    print(f"THE INPUT (pet, color, pattern): {pet}, {color}, {pattern}")
    if pet != None: 
        response = lc.generate_pet_name(pet, color, pattern)['pet_name']
        # response = lc.generate_pet_name(pet, color, pattern)
        print(response)
        # return response['pet_name']
        # return response
        return render_template('pet_gen_result.html', pet=pet, color=color, pattern=pattern, response=response)
    # return f"THE INPUT: {user_input}, {user_input2}"
    # return render_template('result.html', pet=pet, color=color)


if __name__ == "__main__":
    app.run(debug=True)