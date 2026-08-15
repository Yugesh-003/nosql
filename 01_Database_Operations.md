# Install & Configure MongoDB

## Open MongoDB Shell

> Opens the MongoDB interactive shell where you can type and run database commands.

```javascript
mongosh
```

## Create / Switch Database

> Creates a new database named `studentDB` if it doesn't exist, or switches to it if it already does.

```javascript
use studentDB
```

## Create Database (Insert First Document)

> MongoDB only creates a database on disk when you insert the first document — this inserts one student record to make the database real.

```javascript
db.students.insertOne({
    name: "John",
    age: 20
})
```

## Current Database

> Shows the name of the database you are currently working in.

```javascript
db
```

## List Databases

> Lists all databases that exist on your MongoDB server.

```javascript
show dbs
```

## Show Collections

> Lists all collections (like tables) inside the current database.

```javascript
show collections
```

## Delete Database

> Switches to `studentDB` and permanently deletes it along with all its collections and documents.

```javascript
use studentDB
db.dropDatabase()
```