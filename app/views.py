from flask import request, redirect, render_template, url_for
from app import app

@app.route('/')
def index():
	return render_template(
		'authentication/index.html',
		animales=['perro', 'gato', 'caballo', 'tigre', 'aguila']
	    )
