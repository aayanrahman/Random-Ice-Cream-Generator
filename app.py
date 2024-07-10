from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Define lists of possible ingredients
flavors = ["vanilla", "chocolate", "strawberry", "mint", "coffee", "caramel", "matcha", "banana", "coconut", "peach"]
mix_ins = ["chocolate chips", "cookie dough", "brownie bits", "caramel swirl", "marshmallows", "nuts", "fruit pieces", "candy bits"]
toppings = ["sprinkles", "hot fudge", "whipped cream", "cherries", "crushed cookies", "gummy bears"]
swirls = ["caramel", "chocolate", "raspberry", "peanut butter"]
sauces = ["chocolate syrup", "caramel sauce", "strawberry sauce", "butterscotch"]

def generate_random_ice_cream():
    flavor = random.choice(flavors)
    mix_in = random.choice(mix_ins)
    topping = random.choice(toppings)
    swirl = random.choice(swirls)
    sauce = random.choice(sauces)

    if random.choice([True, False]):
        mix_in += " and " + random.choice(mix_ins)
    if random.choice([True, False]):
        topping += " and " + random.choice(toppings)

    return {
        "flavor": flavor,
        "mix_in": mix_in,
        "topping": topping,
        "swirl": swirl,
        "sauce": sauce
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    return jsonify(generate_random_ice_cream())

if __name__ == '__main__':
    app.run(debug=True, port=8000, use_reloader=False)

