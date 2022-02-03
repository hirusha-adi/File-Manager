
import os
import sys
from tkinter import E
import urllib.parse

from flask import Flask, redirect, render_template, request, send_file, url_for

WIN = True if os.name == 'nt' else False
UNIX = False if os.name == 'nt' else True

if WIN:
    import shlex
    import winreg

    def get_default_windows_app(suffix):
        try:
            class_root = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, suffix)
            try:
                with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'{}\shell\open\command'.format(class_root)) as key:
                    command = winreg.QueryValueEx(key, '')[0]
                    name = shlex.split(command)[0]
                    if (name is None) or (name == '') or (bool(name) == False):
                        return False
                    else:
                        return name
            except:
                return False
        except:
            return False


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

    return render_template("index.html",
                           cwd_files=cwd_files,
                           cwd_folder=cwd_folder
                           )


@ app.route("/file")
def file():
    path = request.args.get("path")
    if path is None:
        return "Bug lol"
    corrected = '/'.join(str(path).split("s1a5h"))
    if WIN:
        code = get_default_windows_app(corrected[-1])
        if code is False:
            return send_file(corrected)
        else:
            os.system(f'"{code}" "{path}"')
            return "Program should be running"
    else:
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


if __name__ == "__main__":
    app.run("0.0.0.0", port=3335, debug=True)
