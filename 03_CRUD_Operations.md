# CRUD Operations

## Create

```javascript
db.students.insertOne({
    rollNo:101,
    name:"Arun",
    department:"CSE",
    marks:85
})
```

```javascript
db.students.insertMany([
    {rollNo:102,name:"Priya",marks:90},
    {rollNo:103,name:"Rahul",marks:88}
])
```

## Read

```javascript
db.students.find()
```

```javascript
db.students.findOne({rollNo:101})
```

```javascript
db.students.find({marks:{$gt:85}})
```

## Update

```javascript
db.students.updateOne(
    {rollNo:101},
    {$set:{marks:92}}
)
```

## Delete

```javascript
db.students.deleteOne({rollNo:101})
```