from market import app
from flask import render_template
from market.models import Item

@app.route('/')
@app.route('/home')
def home_page():
    return render_template ('home.html')  # refer route to the HTML file in tempmlates.

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
