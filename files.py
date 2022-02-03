
import os
import sys
import urllib.parse

from flask import Flask, redirect, render_template, request, send_file, url_for

WIN = True if os.name == 'nt' else False
UNIX = False if os.name == 'nt' else True


app = Flask(__name__)


@app.route("/")
def index():
    all_stuff = os.listdir(os.getcwd())

    cwd_folder = {}
    for folder in all_stuff:
        if os.path.isdir(folder):
            if WIN:
                cwd_folder[folder] = urllib.parse.quote_plus(r's1a5h'.join(
                    os.path.join(os.getcwd(), folder).split("\\")))
            else:
                cwd_folder[folder] = urllib.parse.quote_plus(r's1a5h'.join(
                    os.path.join(os.getcwd(), folder).split("/")))

    cwd_files = {}
    for file in all_stuff:
        if os.path.isfile(file):
            if WIN:
                cwd_files[file] = urllib.parse.quote_plus(r's1a5h'.join(
                    os.path.join(os.getcwd(), file).split("\\")))
            else:
                cwd_files[file] = urllib.parse.quote_plus(r's1a5h'.join(
                    os.path.join(os.getcwd(), file).split("/")))

    current_folder_name = os.path.split(os.getcwd())[-1]

    return render_template("index.html",
                           cwd_files=cwd_files,
                           cwd_folder=cwd_folder,
                           current_folder_name=current_folder_name
                           )


@ app.route("/file")
def file():
    path = request.args.get("path")
    if path is None:
        return "Bug lol"
    corrected = '/'.join(str(path).split("s1a5h"))
    return send_file(corrected)


@app.route("/changedir")
def changedir():
    path = request.args.get("destination")
    if path is None:
        return "Bug lol"
    if path == "backbackback":
        if WIN:
            os.chdir("..\..")
        else:
            os.chdir("../..")
    elif path == "backback":
        os.chdir("..")
    else:
        os.chdir('/'.join(str(path).split("s1a5h")))
    return redirect(url_for('index'))


@app.route("/mkdir")
def mkdir():
    fname = request.args.get("name")
    os.makedirs(fname)
    return redirect(url_for('index'))


@app.route("/mkfile")
def mkdir():
    fname = request.args.get("name")
    with open(fname, "w") as ft:
        ft.write()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run("0.0.0.0", port=3335, debug=True)
