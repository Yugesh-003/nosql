# Aggregation Pipeline

## Match

```javascript
db.students.aggregate([
    {$match:{marks:{$gt:80}}}
])
```

## Group

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

```javascript
db.students.aggregate([
    {$sort:{marks:-1}}
])
```

## Limit

```javascript
db.students.aggregate([
    {$sort:{marks:-1}},
    {$limit:3}
])
```