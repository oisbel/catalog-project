from flask import Flask

app = Flask(__name__)

# Show the categories and latest items
@app.route('/')
@app.route('/catalog')
def showCategories():
	return "main page"

# Show the items available for a category
@app.route('/catalog/<string:category_name>/items')
def showItems(category_name):
	return "Items in {}".format(category_name)

# Show the especify information of an item
@app.route('/catalog/<string:category_name>/<string:item_title>')
def showItem(category_name, item_title):
	return "{} in {}".format(item_title,category_name)

# Add an item
@app.route('/catalog/add')
def addItem():
	return "Add Item"

# Edit item
@app.route('/catalog/<string:item_title>/edit')
def showCategory(item_title):
	return "Edit {}".format(item_title)

# Delete item
@app.route('/catalog/<string:item_title>/delete')
def deleteCategory(item_title):
	return "Delete {}".format(item_title)

@app.route('/catalog.json')
def categoriesJSON():
	return "JSON"

if __name__ == '__main__':
  app.secret_key = '88040422507vryyo'
  app.debug = True
  app.run(host = '0.0.0.0', port = 8000)