from flask import render_template
from app import app_1

@app_1.errorhandler(404)
def not_found_error(error):
    return print("not found") #render_template('404.html'), 404

@app_1.errorhandler(500)
def internal_error(error):
    return print("internal_error") #render_template('500.html'), 500