//a script that deletes all documents with name="Holberton school" in the collection school
db.school.deleteMany({ name: "Holberton school" })
