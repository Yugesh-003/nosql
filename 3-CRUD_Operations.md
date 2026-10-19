# CRUD Operations

## Create

> Inserts a single student document with rollNo, name, department, and marks into the `students` collection.

```javascript
db.students.insertOne({
    rollNo:101,
    name:"Arun",
    department:"CSE",
    marks:85
})
```

**Output**
```javascript
{
  acknowledged: true,
  insertedId: ObjectId('6ab1234567890abcdef12347')
}
```

> Inserts multiple student documents at once by passing an array of objects.

```javascript
db.students.insertMany([
    {rollNo:102,name:"Priya",marks:90},
    {rollNo:103,name:"Rahul",marks:88}
])
```

**Output**
```javascript
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ab1234567890abcdef12348'),
    '1': ObjectId('6ab1234567890abcdef12349')
  }
}
```

---

## Read

> Retrieves and displays all documents in the `students` collection.

```javascript
db.students.find()
```

**Output**
```javascript
{
  _id: ObjectId('6ab1234567890abcdef12347'),
  rollNo: 101,
  name: 'Arun',
  department: 'CSE',
  marks: 85
}
{
  _id: ObjectId('6ab1234567890abcdef12348'),
  rollNo: 102,
  name: 'Priya',
  marks: 90
}
{
  _id: ObjectId('6ab1234567890abcdef12349'),
  rollNo: 103,
  name: 'Rahul',
  marks: 88
}
```

> Finds and returns only the first document where `rollNo` equals 101.

```javascript
db.students.findOne({rollNo:101})
```

**Output**
```javascript
{
  _id: ObjectId('6ab1234567890abcdef12347'),
  rollNo: 101,
  name: 'Arun',
  department: 'CSE',
  marks: 85
}
```

> Finds all students whose marks are greater than 85 (`$gt` means "greater than").

```javascript
db.students.find({marks:{$gt:85}})
```

**Output**
```javascript
{
  _id: ObjectId('6ab1234567890abcdef12348'),
  rollNo: 102,
  name: 'Priya',
  marks: 90
}
{
  _id: ObjectId('6ab1234567890abcdef12349'),
  rollNo: 103,
  name: 'Rahul',
  marks: 88
}
```

---

## Update

> Finds the student with `rollNo` 101 and updates their marks to 92 using `$set` (only changes that one field).

```javascript
db.students.updateOne(
    {rollNo:101},
    {$set:{marks:92}}
)
```

**Output**
```javascript
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

---

## Delete

> Finds and deletes the first document where `rollNo` equals 101.

```javascript
db.students.deleteOne({rollNo:101})
```

**Output**
```javascript
{ acknowledged: true, deletedCount: 1 }
```
