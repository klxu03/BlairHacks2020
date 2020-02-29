import os
from store import app
from flask import render_template, url_for, session, request, redirect
from .edamam import product_info
from store.form import ItemForm, ListForm
from flask_session import Session
from werkzeug.utils import secure_filename


items = {
    "apple": {
                "name": "apple",
                "price": 1.99
            },
    "orange": {
                "name": "orange"
            },
    "other":{
                "name": "unknown"
    }
}


# Create a session object and initilize it
sess = Session()
sess.init_app(app)


@app.route('/item/<name>')
def getInfo(name):
    item_info = product_info(name) # get nutritional info based on name
    extra_info = items[name] if name in items else items["other"]

    return render_template("item.html", name=name, item_info=item_info, extra_info=extra_info)

@app.route('/item', methods=['GET', 'POST'])
def item():
    itemForm = ItemForm()
    if itemForm.validate_on_submit():
        itemText = request.form['item']
        print(itemText)
        return redirect(url_for('getInfo', name=itemText))
    else:
        return render_template("itemSearch.html", form=itemForm)

@app.route('/additem/<item>')
def additem(item):
    if item not in session['cartItems']:
        session['cartItems'].append(item)
    if item in session['cartAmounts']:
        session['cartAmounts'][item]+=1
    else:
        session['cartAmounts'][item] = 1
    return redirect(url_for("cart"))

@app.route('/cart')
def cart():
    return render_template("cart.html", items = session['cartItems'], count = session['cartAmounts'])

@app.route('/remItem/<item>')
def remItem(item):
    if item in session['cartItems']:
        session['cartItems'].remove(item)
        del session['cartAmounts'][item]
    return redirect(url_for('cart'))

@app.route('/shoppinglist')
def shoppinglist():
    listForm = ListForm()
    if listForm.validate_on_submit():
        listItem = request.form['item']
        print(listItem)
    return render_template("shoppinglist.html", form=listForm, shoppinglist = session.get('shoppinglist', []))

@app.route('/addlistitem', methods=['POST'])
def addlistitem():
    if session.get('shoppinglist', False):
        session['shoppinglist'].append()
    return render_template("shoppinglist.html", shoppinglist = session.get('shoppinglist', []))

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            photo.save(os.path.join('./store/image-upload', photo.filename))
    return redirect(url_for('item.html'))

@app.route('/')
def home():
    session['cartItems'] = []
    session['cartAmounts'] = {}
    return render_template("index.html")

@app.route('/logout')
def logout():
    session['cartItems'] = []
    session['cartAmounts'] = {}
    session['items'] = []
    return redirect(url_for("item"))
