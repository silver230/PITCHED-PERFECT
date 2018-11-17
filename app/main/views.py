from flask import Flask
from . import main
from flask import render_template,redirect, request, url_for
from .forms import PitchForm
from ..models import User

app = Flask(__name__)


# views
@main.route("/")
def index():
    '''
    title = "Get Started with a pitch"
    '''
    title = 'Get started with a pitch'
    pitches = Pitch.query.all()

    return render_template('index.html', title= title, pitches = pitches)
