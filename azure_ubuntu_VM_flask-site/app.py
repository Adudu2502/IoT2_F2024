import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask, render_template
from get_stue_dht11_data import get_stue_data
import paho.mqtt.publish as publish

app = Flask(__name__)

def stue_temp():
    timestamps, temp, hum = get_stue_data(10)
    
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor("#fff")
    ax.plot(timestamps, temp, linestyle = "dashed", c="#f11", linewidth="1.5", marker="o")
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Temperature celsius")
    fig.patch.set_facecolor("#fff")
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="blue")
    ax.spines['left'].set_color("blue")
    ax.spines['right'].set_color("blue")
    ax.spines['top'].set_color("blue")
    ax.spines['bottom'].set_color("blue")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def stue_hum():
    timestamps, temp, hum = get_stue_data(10)
    
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    fig.subplots_adjust(bottom=0.3)
    ax.tick_params(axis='x', which='both', rotation=30)
    ax.set_facecolor("#fff")
    ax.plot(timestamps, hum, linestyle = "dashed", c="#f11", linewidth="1.5", marker="o")
    ax.set_xlabel("Timestamps")
    ax.set_ylabel("Humidity %")
    fig.patch.set_facecolor("#fff")
    ax.tick_params(axis="x", colors="black")
    ax.tick_params(axis="y", colors="blue")
    ax.spines['left'].set_color("blue")
    ax.spines['right'].set_color("blue")
    ax.spines['top'].set_color("blue")
    ax.spines['bottom'].set_color("blue")
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stue')
def stue():
    stue_temperature = stue_temp()
    stue_humidity = stue_hum()
    return render_template('stue.html', stue_temperature = stue_temperature, stue_humidity = stue_humidity)

@app.route('/koekken')
def koekken():
    return render_template('koekken.html')

@app.route('/taend/', method=['POST'])
def taend():
    publish.single("LED", "taend" hostname="20.234.68.196")
    return render_template('koekken.html')

@app.route('/sluk/', method=['POST'])
def sluk():
    publish.single("LED", "sluk" hostname="20.234.68.196")
    return render_template('koekken.html')

app.run(debug=True)