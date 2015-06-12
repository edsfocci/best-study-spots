from best_study_spots import app
from flask import render_template

@app.route('/')
def index():
  return "Hello!"

