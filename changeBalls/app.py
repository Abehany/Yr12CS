from flask import Flask, render_template, request
from main import changeBalls

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    changes = None
    if request.method == 'POST':
        userInput = request.form.get('userText')
        if userInput:
            changes = changeBalls(userInput)
    
    return render_template('index.html', changes=changes)
  
if __name__ == '__main__':
    app.run(debug=True)
