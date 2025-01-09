from flask import Flask, render_template_string
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WEB - PYTHON RAFI</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@700&family=Mulish&display=swap" rel="stylesheet">
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: black;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            font-family: 'Mulish', sans-serif;
        }
        .hello-world {
            font-size: 50px;
            font-family: 'Poppins', sans-serif;
            font-weight: bold;
            background: linear-gradient(to right, #5F9EA0, #8FBC8F, #ADD8E6);
            -webkit-background-clip: text;
            color: transparent;
        }
        .quote {
            font-size: 20px;
            font-family: 'Mulish', sans-serif;
            color: white;
            margin-top: 5px; /* Reduced the gap further between the two texts */
        }
    </style>
</head>
<body>
    <div class="hello-world">Hello World</div>
    <div class="quote">Apapun metodenya, yang penting jadi</div>
</body>
</html>
    ''')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
