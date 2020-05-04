from flask import Flask, render_template
import data
import itertools

app = Flask(__name__)


@app.route('/')
def hello():
    print(departures)
    return render_template('index.html',
                            title=data.title,
                            subtitle=data.subtitle,
                            description=data.description,
                            departures=data.departures,
                            tours=dict(itertools.islice(
                                data.tours.items(), 6)))


@app.route('/departures/<departure>')
def departures(departure):
    city_tours = {
        k: v for (k, v) in data.tours.items() if v['departure'] == departure}
    return render_template('departure.html',
                            city_tours=city_tours,
                            min_price=min(
                                [a['price'] for a in city_tours.values()]),
                            max_price=max(
                                [a['price'] for a in city_tours.values()]),
                            departure=departure,
                            title=data.title,
                            subtitle=data.subtitle,
                            description=data.description,
                            departures=data.departures)


@app.route('/tours/<int:id>')
def tours(id):
    tour = data.tours[id]
    return render_template('tour.html',
                            title=data.title,
                            subtitle=data.subtitle,
                            description=data.description,
                            departures=data.departures,
                            tour=tour)


app.run(debug=True)
