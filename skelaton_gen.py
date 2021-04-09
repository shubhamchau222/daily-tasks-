import os 
import time 
import argparse



APP = """
from flask import Flask, render_template

import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
"""

BASE = """ 
<!doctype html>
<html lang="en">
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  {% block custom_css %}
  {% endblock custom_css %}
  <title>
    {% block title %}
    {% endblock title %}
  </title>
</head>
<body>
  {% block body %}
  {% endblock body %}
  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
    integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
    integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
    crossorigin="anonymous"></script>
  <!-- jQuery google CDN-->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  {% block custom_js %}
  {% endblock custom_js %}
</body>
</html>
"""

INDEX = """

{% extends 'base.html' %}

{% block title %}
{% endblock title %}

{% block custom_css %}

<!-- Custom CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
{% endblock custom_css %}

{% block body %}
<h1>Hello Flask</h1>
{% endblock body %}

{% block custom_js %}
<!-- Custom JS -->
<script src="{{ url_for('static', filename='script/index.js') }}"></script>
{% endblock custom_js %}


"""


def make_dir_structure(root):
    path_for_placeholder = os.path.join(root ,"templates","Placeholder")
    os.makedirs(path_for_placeholder , exist_ok=True)

    static_dirs = ["css", "script", "uploads"]
    for static_ in static_dirs:
        static_path  = os.path.join(root ,"static", static_)
        os.makedirs(static_path , exist_ok=True)

def file_maker(path ,content):
    with open (path ,"w") as f:
        f.writelines(content)
        # to write the basic flask code in app.py file 
        # to write the html code in index.html file 
        # to write the base code in base.html           

def create_app_html_files(root):
    # create app file 
    app_file_path  = os.path.join(root,"app.py")
    file_maker(app_file_path ,content=APP )   

    # create base file 
    base_file_path  = os.path.join(root  ,"templates" ,"base.html")
    file_maker(base_file_path , content=BASE)

    # createindex  html file 
    file_maker(os.path.join(root,"templates" ,"index.html") , content= INDEX)
        

def touch_empty_files(root): 
    static_root = os.path.join(root, "static")
    files = {
        "css/main.css": "/* main css comment */", 
        "script/index.js": "// index js file"}
    
    for file_, content in files.items():
        dir_, file_ = file_.split("/")
        # using the os.path.join() to avoid the error while change in system
        path_to_file = os.path.join(static_root, dir_, file_)
        file_maker(path_to_file, content)


def main(ROOT):
    make_dir_structure(root=ROOT)
    create_app_html_files(root=ROOT)
    touch_empty_files(root=ROOT)
    print("you boilerplate is ready")



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    ROOT = time.strftime("FlaskApp_%Y_%m_%d-%H_%M_%S")
    args.add_argument("--root" ,default= ROOT)
    parsed_args = args.parse_args()
    #print(parsed_args)    
    main(parsed_args.root)
     
    
    # skelaton_gen.py