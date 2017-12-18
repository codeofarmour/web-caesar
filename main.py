from flask import Flask, request
from caesar import rotate_string

app =  Flask(__name__)
app.config['DEBUG'] = True

form = """

    <!DOCTYPE html>
    <html>
        <head>
            <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}            
            textarea {{
                margin: 10px;
                width: 540px;
                height: 120px;
            }}
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <label>Rotate by:<input name="rot" type="text" value=0 /></label>
                <textarea name="text">{0}</textarea>
                <button>Submit</button>
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=["post", "get"])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]

    rotated = rotate_string(text, rot)
    return form.format(rotated)

app.run()