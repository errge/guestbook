from bson.objectid import ObjectId

class dao(object):
  # We use the "entries" collection inside the database
  def __init__(self, database):
    self.db = database
    self.entries = database.entries

  def find_entries(self):
    l = []
    for entry in self.entries.find():
      l.append(entry)
  
    return l

  def insert_entry(self, name, email):
    newentry = { 'name': name, 'email': email }
    self.entries.insert(newentry)

  def delete_entry(self, id):
    self.entries.remove({ '_id': ObjectId(id) })

  def find_entry(self, id):
    return self.entries.find_one({ '_id': ObjectId(id) })

  def update_entry(self, id, name, email):
    newentry = { 'name': name, 'email': email }
    self.entries.update({ '_id': ObjectId(id) }, newentry)
