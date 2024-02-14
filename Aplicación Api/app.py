#!/usr/bin/python3
"""Iniciando la aplicación"""

from flask import Flask, render_template, redirect, url_for
import random


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)