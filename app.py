from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store forms and responses in memory (replace with a database in a production application)
forms = []
responses = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def registration():
    return render_template('register.html')

@app.route('/choose-role', methods=['GET', 'POST'])
def choose_role():
    if request.method == 'POST':
        role = request.form['role']
        if role == 'teacher':
            return redirect(url_for('create_form'))
        elif role == 'student':
            return redirect(url_for('choose_year'))
    return render_template('beforeyear.html')

@app.route('/create-form', methods=['GET', 'POST'])
def create_form():
    if request.method == 'POST':
        form_title = request.form.get('form_title')
        questions = []
        
        question_texts = request.form.getlist('question')
        question_types = request.form.getlist('question_type')
        num_options_list = request.form.getlist('num_options')
        options_list = request.form.getlist('options')
        min_scales = request.form.getlist('min_scale')
        max_scales = request.form.getlist('max_scale')
        
        for i in range(len(question_texts)):
            question = {'text': question_texts[i], 'type': question_types[i]}
            
            if question_types[i] in ('radio', 'checkbox'):
                num_options = int(num_options_list[i])
                options = options_list[:num_options]
                options_list = options_list[num_options:]
                question['options'] = options
            elif question_types[i] == 'scale':
                min_scale = int(min_scales[i])
                max_scale = int(max_scales[i])
                question['min_scale'] = min_scale
                question['max_scale'] = max_scale
                
            questions.append(question)

        form = {'title': form_title, 'questions': questions}
        forms.append(form)
        return redirect(url_for('index'))
    
    return render_template('create_form.html')

@app.route('/choose-year', methods=['GET', 'POST'])
def choose_year():
    if request.method == 'POST':
        year = request.form['year']
        # You can perform actions based on the selected year if needed
        return redirect(url_for('index'))
    return render_template('year.html')

@app.route('/index')
def index():
    # You can pass data to the index template if needed
    return render_template('index.html', forms=forms)

@app.route('/forms/<int:form_id>', methods=['GET', 'POST'])
def answer_form(form_id):
    form = forms[form_id]
    if request.method == 'POST':
        answers = request.form.getlist('answer')
        response = {'form_title': form['title'], 'answers': answers}
        responses.append(response)
        return redirect(url_for('submit_form', form_id=form_id))
    
    return render_template('answer_form.html', form=form)

@app.route('/forms/<int:form_id>/submit', methods=['GET', 'POST'])
def submit_form(form_id):
    form = forms[form_id]
    if request.method == 'POST':
        answers = request.form.getlist('answer')
        response = {'form_title': form['title'], 'answers': answers}
        responses.append(response)
        return redirect(url_for('show_results', form_id=form_id))
    
    return render_template('submit.html', form=form, form_id=form_id)



@app.route('/results/<int:form_id>')
def show_results(form_id):
    form = forms[form_id]
    response_list = [response['answers'] for response in responses if response['form_title'] == form['title']]
    return render_template('results.html', form=form, responses=response_list)


if __name__ == '__main__':
    app.run(debug=True)