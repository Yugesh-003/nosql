# Collection Operations

## Create Collection

> Switches to `CollegeDB` and explicitly creates an empty collection called `students`.

```javascript
use CollegeDB

db.createCollection("students")
```

## Auto Create Collection

> MongoDB automatically creates a collection when you insert into one that doesn't exist — this inserts one faculty document into a new `faculty` collection.

```javascript
db.faculty.insertOne({
    name: "Anitha",
    department: "CSE"
})
```

## View Collections

> Lists all collections in the current database — you can use either of these two commands.

```javascript
show collections
```

or

```javascript
db.getCollectionNames()
```

## Delete Collection

> Permanently drops (deletes) the `students` collection and all documents inside it.

```javascript
db.students.drop()
```