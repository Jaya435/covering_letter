import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to New Project</h1> <p>A prototype API for distant reading of Music Albums and 
    Playlists.</p> '''

app.run()