from flask import render_template, request
from . import main
import json, epics
import numpy as np
import time


@main.route('/')
def index():
    return render_template('index.html')
