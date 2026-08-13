# Advanced Aggregation in MongoDB

## Use Database

```javascript
use studentDB
```

## Students Collection

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

## Courses Collection

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

## 1. Average using `$group` and `$avg`

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

## 2. Join Collections using `$lookup`

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

## 3. Array Unwinding using `$unwind`

```javascript
db.students.aggregate([
    {
        $unwind: "$subjects"
    }
])
```

## 4. Combining `$lookup` and `$unwind`

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