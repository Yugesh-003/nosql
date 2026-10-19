# Advanced Aggregation in MongoDB

## Use Database

> Switches to (or creates) the `studentDB` database.

```javascript
use studentDB
```

**Output**
```text
switched to db studentDB
```

---

## Students Collection

> Inserts two student documents that each have a `courseId` (for joining later) and a `subjects` array (for unwinding later).

```javascript
db.students.insertMany([
    {
        rollNo: 101,
        name: "Arun",
        department: "CSE",
        marks: 85,
        courseId: 201,
        subjects: ["DBMS", "Python"]
    },
    {
        rollNo: 102,
        name: "Priya",
        department: "ECE",
        marks: 90,
        courseId: 202,
        subjects: ["C Programming", "Signals"]
    }
])
```

**Output**
```javascript
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6ab1234567890abcdef12360'),
    '1': ObjectId('6ab1234567890abcdef12361')
  }
}
```

---

## Courses Collection

> Inserts two course documents into a separate `courses` collection — these will be joined with students using `$lookup`.

```javascript
db.courses.insertMany([
    {
        _id: 201,
        courseName: "Computer Science"
    },
    {
        _id: 202,
        courseName: "Electronics"
    }
])
```

**Output**
```javascript
{
  acknowledged: true,
  insertedIds: {
    '0': 201,
    '1': 202
  }
}
```

---

## 1. Average using `$group` and `$avg`

> Groups students by department and calculates the average marks for each department — like "Computer Science avg = 85".

```javascript
db.students.aggregate([
    {
        $group: {
            _id: "$department",
            averageMarks: {
                $avg: "$marks"
            }
        }
    }
])
```

**Output**
```javascript
{ _id: 'CSE', averageMarks: 85 }
{ _id: 'ECE', averageMarks: 90 }
```

---

## 2. Join Collections using `$lookup`

> Joins the `students` collection with the `courses` collection — matches each student's `courseId` to the `_id` in `courses` and attaches the result as `courseDetails`.

```javascript
db.students.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "courseId",
            foreignField: "_id",
            as: "courseDetails"
        }
    }
])
```

**Output**
```javascript
{
  _id: ObjectId('6ab1234567890abcdef12360'),
  rollNo: 101,
  name: 'Arun',
  department: 'CSE',
  marks: 85,
  courseId: 201,
  subjects: [ 'DBMS', 'Python' ],
  courseDetails: [
    { _id: 201, courseName: 'Computer Science' }
  ]
}
{
  _id: ObjectId('6ab1234567890abcdef12361'),
  rollNo: 102,
  name: 'Priya',
  department: 'ECE',
  marks: 90,
  courseId: 202,
  subjects: [ 'C Programming', 'Signals' ],
  courseDetails: [
    { _id: 202, courseName: 'Electronics' }
  ]
}
```

---

## 3. Array Unwinding using `$unwind`

> Flattens the `subjects` array — each subject becomes its own separate document row instead of being grouped in an array.

```javascript
db.students.aggregate([
    {
        $unwind: "$subjects"
    }
])
```

**Output**
```javascript
{
  _id: ObjectId('6ab1234567890abcdef12360'),
  rollNo: 101,
  name: 'Arun',
  department: 'CSE',
  marks: 85,
  courseId: 201,
  subjects: 'DBMS'
}
{
  _id: ObjectId('6ab1234567890abcdef12360'),
  rollNo: 101,
  name: 'Arun',
  department: 'CSE',
  marks: 85,
  courseId: 201,
  subjects: 'Python'
}
{
  _id: ObjectId('6ab1234567890abcdef12361'),
  rollNo: 102,
  name: 'Priya',
  department: 'ECE',
  marks: 90,
  courseId: 202,
  subjects: 'C Programming'
}
{
  _id: ObjectId('6ab1234567890abcdef12361'),
  rollNo: 102,
  name: 'Priya',
  department: 'ECE',
  marks: 90,
  courseId: 202,
  subjects: 'Signals'
}
```

---

## 4. Combining `$lookup` and `$unwind`

> First joins the `courses` collection into each student document, then `$unwind` flattens the resulting `courseDetails` array so each student row has a single course object (not an array).

```javascript
db.students.aggregate([
    {
        $lookup: {
            from: "courses",
            localField: "courseId",
            foreignField: "_id",
            as: "courseDetails"
        }
    },
    {
        $unwind: "$courseDetails"
    }
])
```

**Output**
```javascript
{
  _id: ObjectId('6ab1234567890abcdef12360'),
  rollNo: 101,
  name: 'Arun',
  department: 'CSE',
  marks: 85,
  courseId: 201,
  subjects: [ 'DBMS', 'Python' ],
  courseDetails: { _id: 201, courseName: 'Computer Science' }
}
{
  _id: ObjectId('6ab1234567890abcdef12361'),
  rollNo: 102,
  name: 'Priya',
  department: 'ECE',
  marks: 90,
  courseId: 202,
  subjects: [ 'C Programming', 'Signals' ],
  courseDetails: { _id: 202, courseName: 'Electronics' }
}
```
