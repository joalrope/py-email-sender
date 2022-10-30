name = "Joalrope"
email = "joalrope@gmail.com"

style = """
    <style>
        .btn {
            display: inline-block;
            cursor: pointer;
            font-weight: 400;
            line-height: 1.5;
            color: #212529;
            text-align: center;
            text-decoration: none;
            vertical-align: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
            background-color: transparent;
            border: 1px solid transparent;
            padding: .375rem .75rem;
            font-size: 1rem;
            border-radius: .25rem;
            transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
        }

        .btn-primary {
            color: #fff;
            background-color: #0d6efd;
            border-color: #0d6efd;
        }   
    </style>
"""

template = f"""
<!doctype html>
<head>
    {style}
</head>
<html lang="en">
    <body>
        <h2> Correo enviado al correo: {email} </h2>
        <h4>Hola {name} desde Python</h4>
        <h3>Test email sent from Python</h3>
        <img src="cid:Mailtrapimage" alt="Test Python send email with image">
        <button class="btn btn-primary">Aceptar</button>
    </body>
</html>
"""
