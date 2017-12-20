from flask import Flask, request
from caesar import rotate_string
import cgi

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
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            </style>
        </head>
        <body>
            <form action="/" method="post">
                <p class="error">{rot_error}</p>
                <label>Rotate by:<input name="rot" type="text" value=0 /></label>
                <textarea name="text">{text}</textarea>
                <button>Submit</button>
            </form>
        </body>
    </html>
"""

def is_integer(rot):
    try:
        int(rot)
        return True
    except ValueError:
        return False

def is_alpha(text):
    try:
        str(text)
        return True
    except ValueError:
        return False

@app.route("/")
def index():
    return form.format(rot_error="", text="")

@app.route("/", methods=["post", "get"])

def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]

    rot_error = ""
    text_error = ""

    if not is_integer(rot):
        rot_error = "Numbers only please"
        rot = ""
        return form.format(rot_error=rot_error, text="")
    else:
        rot = int(rot)
        text = cgi.escape(text)
        rotated = rotate_string(text, rot)
        return form.format(rot_error="", text_error="")
    
    if not is_alpha(text):    
        text_error = "Letters only please"
        text = ""
        return form.format(text_error=text_error, rot="")
    else:
        text = str(text)
        text = cgi.escape(text)
        rotated = rotate_string(text, rot)
        return form.format(rot_error="", text_error="")   

app.run()