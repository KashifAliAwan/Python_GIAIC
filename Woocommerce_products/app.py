from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from woocommerce import API

app = Flask(__name__)

# WooCommerce API credentials
WC_API_URL = "https://your-woocommerce-store.com"  # Replace with your store URL
WC_CONSUMER_KEY = "ck_your_consumer_key"           # Replace with your consumer key
WC_CONSUMER_SECRET = "cs_your_consumer_secret"    # Replace with your consumer secret

# Initialize WooCommerce API
wcapi = API(
    url=WC_API_URL,
    consumer_key=WC_CONSUMER_KEY,
    consumer_secret=WC_CONSUMER_SECRET,
    version="wc/v3"
)

# In-memory cart (for demonstration purposes)
cart = {}

@app.route('/')
def home():
    # Fetch products from the "Electronics" category
    response = wcapi.get("products", params={"category": "electronics"})  # Replace "electronics" with your category slug
    products = response.json()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))

    # Fetch product details
    product = wcapi.get(f"products/{product_id}").json()

    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity,
            'image': product['images'][0]['src'] if product['images'] else None
        }

    return redirect(url_for('view_cart'))

@app.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    action = request.form.get('action')

    if product_id in cart:
        if action == 'plus':
            cart[product_id]['quantity'] += 1
        elif action == 'minus':
            cart[product_id]['quantity'] -= 1
            if cart[product_id]['quantity'] <= 0:
                del cart[product_id]

    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    total_amount = sum(item['price'] * item['quantity'] for item in cart.values())
    return render_template('cart.html', cart=cart, total_amount=total_amount)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = wcapi.get(f"products/{product_id}").json()
    return render_template('product_detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)