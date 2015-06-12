from flask import Flask
app = Flask(__name__)

import best_study_spots.models

import best_study_spots.views
