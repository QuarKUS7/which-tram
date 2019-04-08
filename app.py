from flask import Flask, render_template
from api import set_chromium, get_times, set_driver
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    message = find_direction()
    return render_template('index.html', message=message)

def find_direction():
    now = datetime.datetime.now()
    now_mas = now + datetime.timedelta(hours=2, minutes = 11)
    now_mas = now_mas.strftime('%H:%M')

    now_bil = now + datetime.timedelta(hours=2, minutes = 9)
    now_bil = now_bil.strftime('%H:%M')

    MASAR = 'Masarykovo nádraží'
    BILA = 'Bílá labuť'
    ARRIVAl = 'Letenské náměstí'

    mas = get_times(now_mas, MASAR, ARRIVAl)
    bil = get_times(now_bil, BILA, ARRIVAl)

    if mas <  bil:
        return "Chod na Masaricku: {:d}:{:02d}".format(mas.time().hour, mas.time().minute)
    else:
        return "Chod na Bielu labut: {:d}:{:02d}".format(bil.time().hour, bil.time().minute)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
