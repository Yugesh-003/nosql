# Aggregation Pipeline

---

### Step 1 — Create / Switch Database

> Switch to (or create) a database called `studentDB`.

```javascript
use studentDB
```

### Step 2 — Create Collection

> Explicitly create an empty `students` collection inside `studentDB`.

```javascript
db.createCollection("students")
```

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

### Step 4 — Verify the Data

> Confirm all 8 documents were inserted correctly before running aggregations.

```javascript
db.students.find()
```

---



## Match

> Filters documents in the pipeline — only students with marks greater than 80 pass through to the next stage.

```javascript
db.students.aggregate([
    {$match:{marks:{$gt:80}}}
])
```

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

## Sort

> Sorts all students by marks in descending order (`-1` = highest first, `1` would be lowest first).

```javascript
db.students.aggregate([
    {$sort:{marks:-1}}
])
```

## Limit

> First sorts students by marks descending, then `$limit:3` cuts the result to only the top 3 students.

```javascript
db.students.aggregate([
    {$sort:{marks:-1}},
    {$limit:3}
])
```