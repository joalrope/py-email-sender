from templates.styles import style


def template(name, email):

    return f"""
    <!doctype html>
    <head>
        {style}
    </head>
    <html lang="en">
        <body>
            <h3> Correo enviado a:  {name} al email: {email} </h3>
            <h3>desde aplicacion en Python</h3>
            <img src="cid:Mailtrapimage" alt="Test Python send email with image">
            <button class="btn btn-primary">Aceptar</button>
        </body>
    </html>
    """
