# Import flask forms from flask_wtf
from flask_wtf import FlaskForm
# Import the types of fields that we want to have, a string, password, submit and boolean feild
from wtforms import StringField, SubmitField

# Create a new object that inherits the FlaskForm properties, we want to add our additional attributes that this object should have
class ItemForm(FlaskForm):  
#    picture = FileField('Barcode Picture', validators=[FileAllowed(images, 'Only images allowed!')])
    item = StringField('Item', render_kw={"placeholder": "Enter an item"})
    # Add a submit field
    submit = SubmitField('Search!')

class ListForm(FlaskForm):
    item = StringField('Item', render_kw={"placeholder": "Add an item to your shopping list"})
    submit = SubmitField('Add Item')
