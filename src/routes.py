
import copy
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
        try:
            user = user_service.login(request.form['email'],request.form['password'])
        except:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        else:
            login_user(user)
            next_page = request.args.get('next')
            print(current_user)
            return redirect(next_page) if next_page else redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        #hashed_password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user_service = UserService()
        user_converter = UserConverter()
        input_data = dict(request.form)
        confirm_password = input_data.pop('confirm_password',None)
        if confirm_password == input_data['password']:
            user = user_converter.dict_to_object(input_data)
        else:
            flash('Passwords are not the same')
            user = None
        try:
            user = user_service.create_user(user)
        except:
            flash('Error creating user')
        else:
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
    return render_template('register.html') 

@app.route('/new_event', methods=['GET', 'POST'])
@login_required
def new_event(sub_events=[]):
    if request.method == 'POST':
        print(request.form)
        print('oi')
        converter = EventConverter()    
        event_service = EventService()

        print('post criar evento')
        event = None
        input_data = dict(request.form)
        input_data['host'] = copy.deepcopy(current_user)
        
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
            return redirect(url_for('home'))

    return render_template('create_event.html',sub_events = sub_events,)

@app.route('/new_event/new_subevent', methods=['GET','POST'],)
@login_required
def new_subevent(sub_events=[]):
    converter = EventConverter()    
    input_data = dict(request.form)
    input_data['host'] = copy.deepcopy(current_user)
    sub_event = converter.dict_to_object(input_data)
    sub_events.append(sub_event)
    request.form = ''
    return redirect(url_for('new_event',sub_events = sub_events,))
    
@app.route('/search')    
def search():
    return render_template('home.html')



