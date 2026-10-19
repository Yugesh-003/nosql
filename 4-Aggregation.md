# Aggregation Pipeline

---

### Step 1 — Create / Switch Database

> Switch to (or create) a database called `studentDB`.

```javascript
use studentDB
```

**Output**
```text
switched to db studentDB
```

---

### Step 2 — Create Collection

> Explicitly create an empty `students` collection inside `studentDB`.

```javascript
db.createCollection("students")
```

**Output**
```javascript
{ ok: 1 }
```

---

### Step 3 — Insert Sample Data

> Insert 8 students across 3 departments with varied marks — this gives the aggregation commands interesting, non-trivial results to work with.

```javascript
db.students.insertMany([
    { name: "Arun",   department: "CSE",  marks: 85 },
    { name: "Priya",  department: "CSE",  marks: 92 },
    { name: "Rahul",  department: "CSE",  marks: 76 },
    { name: "Divya",  department: "ECE",  marks: 88 },
    { name: "Karan",  department: "ECE",  marks: 73 },
    { name: "Sneha",  department: "MECH", marks: 91 },
    { name: "Arjun",  department: "MECH", marks: 69 },
    { name: "Meena",  department: "MECH", marks: 84 }
])
```

**Output**
```javascript
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ab1234567890abcdef12350'),
    '1': ObjectId('6ab1234567890abcdef12351'),
    '2': ObjectId('6ab1234567890abcdef12352'),
    '3': ObjectId('6ab1234567890abcdef12353'),
    '4': ObjectId('6ab1234567890abcdef12354'),
    '5': ObjectId('6ab1234567890abcdef12355'),
    '6': ObjectId('6ab1234567890abcdef12356'),
    '7': ObjectId('6ab1234567890abcdef12357')
  }
}
```

---

### Step 4 — Verify the Data

> Confirm all 8 documents were inserted correctly before running aggregations.

```javascript
db.students.find()
```

**Output**
```javascript
{ _id: ObjectId('...'), name: 'Arun',  department: 'CSE',  marks: 85 }
{ _id: ObjectId('...'), name: 'Priya', department: 'CSE',  marks: 92 }
{ _id: ObjectId('...'), name: 'Rahul', department: 'CSE',  marks: 76 }
{ _id: ObjectId('...'), name: 'Divya', department: 'ECE',  marks: 88 }
{ _id: ObjectId('...'), name: 'Karan', department: 'ECE',  marks: 73 }
{ _id: ObjectId('...'), name: 'Sneha', department: 'MECH', marks: 91 }
{ _id: ObjectId('...'), name: 'Arjun', department: 'MECH', marks: 69 }
{ _id: ObjectId('...'), name: 'Meena', department: 'MECH', marks: 84 }
```

---

## Match

> Filters documents in the pipeline — only students with marks greater than 80 pass through to the next stage.

```javascript
db.students.aggregate([
    {$match:{marks:{$gt:80}}}
])
```

**Output**
```javascript
{ _id: ObjectId('...'), name: 'Arun',  department: 'CSE',  marks: 85 }
{ _id: ObjectId('...'), name: 'Priya', department: 'CSE',  marks: 92 }
{ _id: ObjectId('...'), name: 'Divya', department: 'ECE',  marks: 88 }
{ _id: ObjectId('...'), name: 'Sneha', department: 'MECH', marks: 91 }
{ _id: ObjectId('...'), name: 'Meena', department: 'MECH', marks: 84 }
```

---

## Group

> Groups all students by their `department` field and calculates the average marks for each department using `$avg`.

```javascript
db.students.aggregate([
    {
        $group:{
            _id:"$department",
            averageMarks:{$avg:"$marks"}
        }
    }
])
```

**Output**
```javascript
{ _id: 'CSE',  averageMarks: 84.33333333333333 }
{ _id: 'ECE',  averageMarks: 80.5 }
{ _id: 'MECH', averageMarks: 81.33333333333333 }
```

---

## Project

> Controls which fields appear in the output — `1` means include, `0` means exclude. Here it shows only `name` and `marks`, hiding the `_id`.

```javascript
db.students.aggregate([
    {
        $project:{
            _id:0,
            name:1,
            marks:1
        }
    }
])
```

**Output**
```javascript
{ name: 'Arun',  marks: 85 }
{ name: 'Priya', marks: 92 }
{ name: 'Rahul', marks: 76 }
{ name: 'Divya', marks: 88 }
{ name: 'Karan', marks: 73 }
{ name: 'Sneha', marks: 91 }
{ name: 'Arjun', marks: 69 }
{ name: 'Meena', marks: 84 }
```

---

## Sort

> Sorts all students by marks in descending order (`-1` = highest first, `1` would be lowest first).

```javascript
db.students.aggregate([
    {$sort:{marks:-1}}
])
```

**Output**
```javascript
{ _id: ObjectId('...'), name: 'Priya', department: 'CSE',  marks: 92 }
{ _id: ObjectId('...'), name: 'Sneha', department: 'MECH', marks: 91 }
{ _id: ObjectId('...'), name: 'Divya', department: 'ECE',  marks: 88 }
{ _id: ObjectId('...'), name: 'Arun',  department: 'CSE',  marks: 85 }
{ _id: ObjectId('...'), name: 'Meena', department: 'MECH', marks: 84 }
{ _id: ObjectId('...'), name: 'Rahul', department: 'CSE',  marks: 76 }
{ _id: ObjectId('...'), name: 'Karan', department: 'ECE',  marks: 73 }
{ _id: ObjectId('...'), name: 'Arjun', department: 'MECH', marks: 69 }
```

---

## Limit

> First sorts students by marks descending, then `$limit:3` cuts the result to only the top 3 students.

```javascript
db.students.aggregate([
    {$sort:{marks:-1}},
    {$limit:3}
])
```

**Output**
```javascript
{ _id: ObjectId('...'), name: 'Priya', department: 'CSE',  marks: 92 }
{ _id: ObjectId('...'), name: 'Sneha', department: 'MECH', marks: 91 }
{ _id: ObjectId('...'), name: 'Divya', department: 'ECE',  marks: 88 }
```
