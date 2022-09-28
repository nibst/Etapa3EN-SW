
import os
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.Event import Event
from src.application.EventService import EventService
from src.data.User import User
from src.application.UserService import UserService
from src.application.EventConverter import EventConverter

from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(import_name=__name__,
            static_folder=os.getcwd() + r"\images")
            
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form.keys())
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html') 

@app.route('/event/new_event', methods=['GET', 'POST'])
def new_event(sub_events=[]):
    
    if request.method == 'POST':
        user = User('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(166) #for testing purposes  
        converter = EventConverter()    
        event_service = EventService()
        print(request.headers['Referer'])
        if request.headers['Referer'].find('new_subevent') != -1:
            #copy input data dict, because we will add a key in it
            input_data = dict(request.form)
            input_data['host'] = user
            sub_event = converter.dict_to_object(input_data)
            sub_events.append(sub_event)
            request.form = ''

        else:
            print('post criar evento')
            event = None
            input_data = dict(request.form)
            input_data['host'] = user
            try:
                event = converter.dict_to_object(input_data)
                #return event if save successfully
                event = event_service.save(event)
                for sub_event in sub_events:
                    sub_event.set_event_parent(event)
                    event_service.save(sub_event)
            except Exception as e:
                return render_template('create_event.html', error=e)
            else:
                
                flash('Evento criado com sucesso')
                return redirect(url_for('events'))
    print('oi')
    return render_template('create_event.html',sub_events = sub_events,)

@app.route('/events', methods=['GET'])
def events():
    event_service = EventService()
    events = event_service.get_events()
    
    return render_template('events.html',events=events)

@app.route('/event/new_event/new_subevent', methods=['GET'])
def new_subevent(sub_events=[]):
    
    return render_template('create_subevent.html',sub_events = sub_events,)
    
    
if __name__ == '__main__':
    app.run(debug=True)
    DBConnectionSingleton.get_instance() #in case there isnt an instance of DBconnection to destroy
    DBConnectionSingleton.destroyer()




