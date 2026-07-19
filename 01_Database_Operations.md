# Install & Configure MongoDB

## Open MongoDB Shell

```javascript
mongosh
```

## Create / Switch Database

```javascript
use studentDB
```

## Create Database (Insert First Document)

```javascript
db.students.insertOne({
    name: "John",
    age: 20
})
```

## Current Database

```javascript
db
```

## List Databases

```javascript
show dbs
```

## Show Collections

```javascript
show collections
```

## Delete Database

```javascript
use studentDB
db.dropDatabase()
```