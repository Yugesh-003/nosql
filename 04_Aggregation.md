# Aggregation Pipeline

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