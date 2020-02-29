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
            }
}


# Create a session object and initilize it
sess = Session()
sess.init_app(app)


@app.route('/item/<name>')
def getInfo(name, file_name=None):
	if file_name == None: #name based evaluation
		item_info = product_info(name) # get nutritional info based on name
		print(item_info)
		extra_info = items[name] if name in items else items["other"]
		if name in items:
		    return render_template("item.html", info=items[name])
		else:
			return render_template("item.html", info={"name":"Unknown item"})

@app.route('/item', methods=['GET', 'POST'])
def item():
    itemForm = ItemForm()
    if itemForm.validate_on_submit():
        itemText = request.form['item']
        itemImage = request.form['picture']
        if itemText != "": # there's something in the text form
            print(itemText)
            # go to the page of the given item
            return redirect(url_for('getInfo', name=itemText))
        else: # no text - is there a picture? (TODO)
            print("No text!")
            print(itemImage)
            return redirect(url_for('getInfo', name='apple')) #temporarily just redirect to /items/apple
    else:
    	return render_template("itemSearch.html", form=itemForm)

@app.route('/additem/<item>')
def additem(item):
    if session.get('items', False): #If there is no item here
        print("1: " + session.get('items'))
        if session.get('counts', False): #If there is not count inside
            print("2: " + session.get('items'))
            if item in session['counts']: #If there is already a count (maybe 2)
                session['counts'][item] += 1
                session['item'].append(item)
            else:
                session['counts'][item] = 1
                session['item'].append(item)
        else:
            session['counts'] = {item:1}
            session['item'].append(item)

    else:
        session['items'] = [item]
        session['counts'] = {item:1}
        session['item'].append(item)
    
    print("3: " + session.get('items'))
    print(session.get('counts'))
    print(session.get('counts')[item])
    # print("Apple: " + str(item))

    numberOfItems = session['counts'][item]
    print("Apple: " + str(item) + " counts " + str(numberOfItems))

    return redirect(url_for("cart", name = item, count = session.get('counts')[item], items = session['item']))

@app.route('/cart')
def cart():
    return render_template("cart.html", items = session.get('items', []))

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
        photo_url = None # defined here for scoping purposes
        if photo.filename != '': # if the photo exists (?)           
            photo_url = os.path.join('./store/image-upload/', photo.filename)
            photo.save(photo_url)
    return redirect(url_for('item', json=json_from_barcode_photo(photo_url)))

def json_from_barcode_photo(file_name):    
    return product_info(barcodereader(file_name))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session['items'] = []
    return redirect(url_for("item"))
