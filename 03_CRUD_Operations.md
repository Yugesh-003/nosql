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

> Inserts multiple student documents at once by passing an array of objects.

```javascript
db.students.insertMany([
    {rollNo:102,name:"Priya",marks:90},
    {rollNo:103,name:"Rahul",marks:88}
])
```

## Read

> Retrieves and displays all documents in the `students` collection.

```javascript
db.students.find()
```

> Finds and returns only the first document where `rollNo` equals 101.

```javascript
db.students.findOne({rollNo:101})
```

> Finds all students whose marks are greater than 85 (`$gt` means "greater than").

```javascript
db.students.find({marks:{$gt:85}})
```

## Update

> Finds the student with `rollNo` 101 and updates their marks to 92 using `$set` (only changes that one field).

```javascript
db.students.updateOne(
    {rollNo:101},
    {$set:{marks:92}}
)
```

## Delete

> Finds and deletes the first document where `rollNo` equals 101.

```javascript
db.students.deleteOne({rollNo:101})
```