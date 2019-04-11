from flask import Flask, render_template
from api import set_chromium, get_times, set_driver
import datetime
import os

app = Flask(__name__)

@app.route("/")
def hello():
    message = find_direction()
    return render_template('index.html', message=message)

def find_direction():
    options = set_chromium()

    now = datetime.datetime.now()
    # give 9 minutes for walking to Masarykovo nard.
    now_mas = now + datetime.timedelta(hours=2, minutes = 9)
    now_mas = now_mas.strftime('%H:%M')
    # give 7 minutes for walking to Masarykovo nard.
    now_bil = now + datetime.timedelta(hours=2, minutes = 7)
    now_bil = now_bil.strftime('%H:%M')

    MASAR = 'Masarykovo nádraží'
    BILA = 'Bílá labuť'
    ARRIVAl = 'Letenské náměstí'

    mas = get_times(now_mas, MASAR, ARRIVAl, options)
    bil = get_times(now_bil, BILA, ARRIVAl, options)

    if type(mas) == str:
        return mas
    if type(bil) == str:
        return bil

    if mas <  bil:
        return "Chod na Masaricku: {:d}:{:02d}".format(mas.time().hour, mas.time().minute)
    else:
        return "Chod na Bielu labut: {:d}:{:02d}".format(bil.time().hour, bil.time().minute)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
