from flask import Flask
from flask import (Flask, flash, redirect, render_template, request,
                   session, url_for)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/styling/")
def styling():
    return render_template("styling.html")

@app.route("/colouring/")
def colouring():
    return render_template("colouring.html")

@app.route("/other/")
def other():
    return render_template("other.html")