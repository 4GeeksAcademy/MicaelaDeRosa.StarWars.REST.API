

Getting Data
Assuming you have a Person object in your models.py file.
# get all the people
# SELECT * FROM Person;
people_query = Person.query.all()

# get only the ones named "Joe"
people_query = Person.query.filter_by(name='Joe')
#SELECT * FROM Person WHERE name = "Joe"

# map the results and your list of people  inside of the all_people variable
all_people = list(map(lambda x: x.serialize(), people_query))

# get just one person basado en su llave primaria
user1 = Person.query.get(person_id)

#Inserting data
Assuming you have a Person object in your models.py file.
user1 = Person()
user1.username = "my_super_username"
user1.email = "my_super@email.com"
db.session.add(user1)
db.session.commit()

#Updating data

user1 = Person.query.get(person_id)
if user1 is None:
    return jsonify({'msg':'User not found'},404

if "username" in body:
    user1.username = body["username"]
if "email" in body:
    user1.email = body["email"]
db.session.commit()

#Delete data

user1 = Person.query.get(person_id)
if user1 is None:
   return jsonify({'msg':'User not found'},404
db.session.delete(user1)
db.session.commit()

<------------------------------------------------------------------------->

One to many relationship 
class Parent(Base):
    __tablename__ = "parent_table"
    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")


class Child(Base):
    __tablename__ = "child_table"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent_table.id"))
    parent = relationship("Parent", back_populates="children")