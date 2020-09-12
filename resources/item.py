import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="this field cannot be left blank!")
    
    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404
    
    def post(self, name):        
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400
        
        data = Item.parser.parse_args()
        
        item = {'name': name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {"message": "An error occured insterting the item."}, 500

        return item, 201

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name, ))

        connection.commit()
        connection.close()

        return {'message': "item deleted"}

    def put(self, name):
        data = Item.parser.parse_args()

        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        
        if item is None:
            try:
                seilf.insert(update_item)
            except:
                return {"message": "An error occured inserting the item."}, 500

        else:
            try:
                self.update(updated_item)
            except:
                return {"message": "An error occured updating the item"}, 500
        return updated_item


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': [row[1]]})

        connection.close()
        return {'items': items}