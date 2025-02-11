from app import mongo 

class Users:
    collection = mongo.db.users

    @staticmethod
    def find_all():
        Users = Users.collection.find()
        return list(Users)
    

    @staticmethod
    def find_by_id():
        User = Users.collection.find_one({
            "_id": User_id
        })
        return User 
    
    @staticmethod
    def create():
        User = Users.collection.insert_one(data)
        return User.inserted_id
    
    @staticmethod
    def update(User_id, data):
        User = Users.collectio.update_one({
            "id":User_id
        },{
            "$set": data
        })
        return User
    
    @staticmethod
    def delete (User_id):
        return Users.collection.delete_one({"_id": User_id})