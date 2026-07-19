# Database Operations

## Create / Switch Database

```javascript
use studentDB
```

## Current Database

```javascript
db
```

## List Databases

```javascript
show dbs
```

## Delete Database

```javascript
use studentDB
db.dropDatabase()
```

## Useful Commands

```javascript
show collections
db.students.find()
db.students.findOne()
db.students.countDocuments()
```