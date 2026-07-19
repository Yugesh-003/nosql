# Collection Operations

## Create Collection

```javascript
use CollegeDB

db.createCollection("students")
```

## Auto Create Collection

```javascript
db.faculty.insertOne({
    name: "Anitha",
    department: "CSE"
})
```

## View Collections

```javascript
show collections
```

or

```javascript
db.getCollectionNames()
```

## Delete Collection

```javascript
db.students.drop()
```