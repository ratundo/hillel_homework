import random
import string

import pandas as pd

from flask import Flask, Request, Response

app = Flask(__name__)

@app.route("/password")
def generate_password():
    length = random.randint(10, 20)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return f'Password of this day: {password}'

@app.route("/students")
def calculate_average():
    df = pd.read_csv('hw.csv')
    av_height = df[' Height(Inches)'].mean(),
    av_weight = df[' Weight(Pounds)'].mean()
    return f'Average height: {av_height} inches,\n Average weight: {av_weight} pounds'

if __name__ == '__main__': app.run(port=5000, debug=True)