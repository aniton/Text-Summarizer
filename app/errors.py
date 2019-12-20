from flask import render_template
from app import app

@app.errorhandler(404)
def not_found_error(error):
    return print("not found") #render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return print("internal_error") #render_template('500.html'), 500