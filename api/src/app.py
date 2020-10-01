from flask import Flask, render_template
import requests

from .config import app_config
from .models.__init import db, bcrypt
from .views.UserView import user_api as user_blueprint
from .views.SectionView import blogpost_api as blogpost_blueprint
import json
import os

def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    bcrypt.init_app(app)

    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is workin'

    @app.route('/', methods=['PUT'])
    def create_record(filename):
        dict1 = {}
        with open(filename) as f:
            for line in f:
                command, description = line.strip().split(None, 1)
                dict1[command] = description.strip()
        return json.loads(json.dumps(dict1, indent=4, sort_keys=False))

    def add_record_to_db(filename):
        record = create_record(filename)
        response = requests.post('http://localhost:5000/api/v1/blogposts/', json=record)

    def get_record_from_db():
        response = requests.get('http://localhost:5000/api/v1/blogposts/')
        return response

    def load_information():
        data_directory = os.path.abspath('../resources')
        response = requests.get('http://localhost:5000/api/v1/blogposts/')
        if response.status_code == 200:
            record = json.loads(response.text)
            for r in record:
                requests.delete('http://localhost:5000/api/v1/blogposts/{}'.format(r['id']))
        for file in os.listdir(data_directory):
            add_record_to_db(data_directory+'/'+file)

    @app.route('/home', methods=['GET'])
    def home():
        load_information()
        response = get_record_from_db()
        records = json.loads(response.text)
        content = {}
        content['page'] = 'home'
        for record in records:
            content[record['title']] = record['contents'].split('/n')
        return render_template('base.html', content=content)

    @app.route('/motivation', methods=['GET'])
    def motivation():
        load_information()
        response = get_record_from_db()
        records = json.loads(response.text)
        content = {}
        content['page'] = 'motivation'
        for record in records:
            content[record['title']] = record['contents'].split('/n')
        return render_template('base.html', content=content)

    @app.route('/skills', methods=['GET'])
    def skills():
        load_information()
        response = get_record_from_db()
        records = json.loads(response.text)
        content = {}
        content['page'] = 'skills'
        for record in records:
            content[record['title']] = record['contents'].split('/n')
        return render_template('base.html', content=content)


    return app
