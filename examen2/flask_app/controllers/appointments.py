from flask import render_template, session,flash,redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.user import User
from flask_app.models.appointment import Appointment
from flask_app.controllers import users





@app.route('/post_appointment', methods=['POST'])
def post_appointment():
    if request.method == 'POST':
        # Procesar los datos del formulario aquí
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        # Realizar acciones necesarias con los datos
        
        # Puedes redirigir a una página de confirmación o hacer lo que necesites hacer con los datos.

        return "Datos del formulario procesados con éxito"  # Puedes personalizar el mensaje de confirmación.

