
from src.application.UserConverter import UserConverter
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.Event import Event
from src.application.EventService import EventService
from src.data.User import User
from src.application.UserService import UserService
from src.application.EventConverter import EventConverter

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager,login_user, current_user, logout_user, login_required
from src import login_manager,app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user)
  
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        user_service = UserService()
        input_data = dict(request.form)
        user = user_service.login(request.form['email'],request.form['password'])
        if user:
            login_user(user)
            next_page = request.args.get('next')
            print(current_user)
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')


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
    
    




