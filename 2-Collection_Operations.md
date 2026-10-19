# Collection Operations

## Create Collection

> Switches to `CollegeDB` and explicitly creates an empty collection called `students`.

```javascript
use CollegeDB

db.createCollection("students")
```

**Output**
```text
switched to db CollegeDB
```
```javascript
{ ok: 1 }
```

---

## Auto Create Collection

> MongoDB automatically creates a collection when you insert into one that doesn't exist — this inserts one faculty document into a new `faculty` collection.

```javascript
db.faculty.insertOne({
    name: "Anitha",
    department: "CSE"
})
```

**Output**
```javascript
{
  acknowledged: true,
  insertedId: ObjectId('6ab1234567890abcdef12346')
}
```

---

## View Collections

> Lists all collections in the current database — you can use either of these two commands.

```javascript
show collections
```

**Output**
```text
faculty
students
```

or

```javascript
db.getCollectionNames()
```

**Output**
```javascript
[ 'faculty', 'students' ]
```

---

## Delete Collection

> Permanently drops (deletes) the `students` collection and all documents inside it.

```javascript
db.students.drop()
```

**Output**
```javascript
true
```
