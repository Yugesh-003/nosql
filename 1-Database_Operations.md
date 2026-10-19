# Create, switch, list, and delete databases in MongoDB  

## Create / Switch Database

> Creates a new database named `studentDB` if it doesn't exist, or switches to it if it already does.

```javascript
use studentDB
```

**Output**
```text
switched to db studentDB
```

---

## Create Database (Insert First Document)

> MongoDB only creates a database on disk when you insert the first document — this inserts one student record to make the database real.

```javascript
db.students.insertOne({
    name: "John",
    age: 20
})
```

**Output**
```javascript
{
  acknowledged: true,
  insertedId: ObjectId('6ab1234567890abcdef12345')
}
```

---

## Current Database

> Shows the name of the database you are currently working in.

```javascript
db
```

**Output**
```text
studentDB
```

---

## List Databases

> Lists all databases that exist on your MongoDB server.

```javascript
show dbs
```

**Output**
```text
admin      40.00 KiB
config     60.00 KiB
local      40.00 KiB
studentDB   8.00 KiB
```

---

## Show Collections

> Lists all collections (like tables) inside the current database.

```javascript
show collections
```

**Output**
```text
students
```

---

## Delete Database

> Switches to `studentDB` and permanently deletes it along with all its collections and documents.

```javascript
use studentDB
db.dropDatabase()
```

**Output**
```javascript
{ ok: 1, dropped: 'studentDB' }
```
