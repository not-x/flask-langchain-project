from flask import Flask, render_template, request
import langchain_helper as lch

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

@app.route('/agents')
def agents():
    return render_template('langchain_agents.html')


@app.route('/process', methods=['POST'])
def process():
    # user_input = request.form['user_input']

    # if user_input != None:
    #     print(f"THE INPUT: {user_input}")
    #     output = lch.generate_output(user_input)['output']
    #     return render_template('index_result.html', output=output)
    # print( (request.form.get('pet') == None))

    if request.form.get('pet') != None:
        pet = request.form['pet']
        color = request.form['color']
        pattern = request.form['pattern']


        print(f"THE INPUT (pet, color, pattern): {pet}, {color}, {pattern}")
        response = lch.generate_pet_name(pet, color, pattern)['pet_name']
        print(response)
        return render_template('pet_gen_result.html', pet=pet, color=color, pattern=pattern, response=response)
         

    # if pet != None:
    #     response = lch.generate_pet_name(pet, color, pattern)['pet_name']
    #     # response = lch.generate_pet_name(pet, color, pattern)
    #     print(response)
    #     # return response['pet_name']
    #     # return response
    #     return render_template('pet_gen_result.html', pet=pet, color=color, pattern=pattern, response=response)
    # # return f"THE INPUT: {user_input}, {user_input2}"
    # return render_template('result.html', pet=pet, color=color)

    question = request.form['question']
    if question != None:
        response = lch.langchain_agent(question)['output']
        print(response)
        # print(response['output'])
        return render_template('langchain_agents_result.html', question=question, response=response)


if __name__ == "__main__":
    app.run(debug=True)
