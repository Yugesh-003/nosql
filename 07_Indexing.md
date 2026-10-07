# Indexing and Query Performance

## Create Sample Database and Collection

> Creates the `companyDB` database and inserts six employee documents into the `employees` collection.

```javascript
use companyDB

db.employees.insertMany([
    {
        empId: 101,
        name: "Anu",
        department: "HR",
        salary: 45000,
        age: 28,
        city: "Madurai"
    },
    {
        empId: 102,
        name: "Ravi",
        department: "IT",
        salary: 65000,
        age: 30,
        city: "Chennai"
    },
    {
        empId: 103,
        name: "Meena",
        department: "Finance",
        salary: 55000,
        age: 32,
        city: "Madurai"
    },
    {
        empId: 104,
        name: "Kumar",
        department: "IT",
        salary: 75000,
        age: 35,
        city: "Bangalore"
    },
    {
        empId: 105,
        name: "Priya",
        department: "HR",
        salary: 48000,
        age: 29,
        city: "Chennai"
    },
    {
        empId: 106,
        name: "Suresh",
        department: "IT",
        salary: 70000,
        age: 31,
        city: "Madurai"
    }
])
```

## Query Without Index

> Finds all employees who belong to the IT department.

```javascript
db.employees.find({
    department: "IT"
})
```

> Analyzes the query using `explain("executionStats")` to view execution statistics.

```javascript
db.employees.find({
    department: "IT"
}).explain("executionStats")
```

## Create an Index

> Creates an ascending index on the `department` field.

```javascript
db.employees.createIndex({
    department: 1
})
```

**Output:**

```text
department_1
```

## Run the Same Query Again

> Runs the same query after creating the index and analyzes its execution statistics.

```javascript
db.employees.find({
    department: "IT"
}).explain("executionStats")
```

## Another Example – Salary

> Finds employees earning more than ₹60,000. `$gt` means "greater than".

```javascript
db.employees.find({
    salary: {$gt: 60000}
})
```

> Analyzes the salary query using execution statistics.

```javascript
db.employees.find({
    salary: {$gt: 60000}
}).explain("executionStats")
```

### Create a Salary Index

> Creates an ascending index on the `salary` field.

```javascript
db.employees.createIndex({
    salary: 1
})
```

### Run the Query Again

```javascript
db.employees.find({
    salary: {$gt: 60000}
}).explain("executionStats")
```

## Compound Index Example

> Finds employees in the IT department and sorts them by salary in descending order.

```javascript
db.employees.find({
    department: "IT"
}).sort({
    salary: -1
})
```

> Creates a compound index using `department` in ascending order and `salary` in descending order.

```javascript
db.employees.createIndex({
    department: 1,
    salary: -1
})
```

- `department` → ascending
- `salary` → descending

### Analyze the Query

```javascript
db.employees.find({
    department: "IT"
}).sort({
    salary: -1
}).explain("executionStats")
```

## View All Indexes

> Displays all indexes currently created on the `employees` collection.

```javascript
db.employees.getIndexes()
```

## Remove an Index

> Removes the `salary_1` index from the collection.

```javascript
db.employees.dropIndex("salary_1")
```

### Check the Indexes Again

```javascript
db.employees.getIndexes()
```

## Query Performance Analysis

### Query 1

```javascript
db.employees.find({
    department: "IT"
}).explain("executionStats")
```

### Query 2

> Create an index on the `department` field.

```javascript
db.employees.createIndex({
    department: 1
})
```

### Query 3

```javascript
db.employees.find({
    department: "IT"
}).explain("executionStats")
```

### Query 4

> Create a compound index on `department` and `salary`.

```javascript
db.employees.createIndex({
    department: 1,
    salary: -1
})
```

### Query 5

```javascript
db.employees.find({
    department: "IT"
}).sort({
    salary: -1
}).explain("executionStats")
```

## Remove an Index

```javascript
db.employees.dropIndex("salary_1")
```
