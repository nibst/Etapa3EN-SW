from src.data.Event import Event
from src.application.create_event import EventService
from src.data.User import User
from src.application.create_user import create_user

from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

    
@app.route('/new_event', methods=['GET', 'POST'])
def new_event():
    if request.method == 'POST':
        user = create_user('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(166) #for testing purposes       
        event = None
        event_service = EventService()
        try:
            event = event_service.create_event(user,request.form)
        except Exception as e:
            return render_template('create_event.html', error=e)
        else:
            flash('Evento criado com sucesso')
            return redirect(url_for('events'))
    return render_template('create_event.html')

@app.route('/events', methods=['GET'])
def events():
    event_service = EventService()
    events = event_service.get_events()
    for event in events:
        print(event.visibility)
    return render_template('events.html',events=events)
    
if __name__ == '__main__':
    app.run(debug=True)