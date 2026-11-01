# MongoDB Exercise - Internal 1

## Exercise Questions

### 1. Database and Collection Creation
- Create a database called `company`
- Create a collection called `employees`

### 2. Insert Employee Documents
Insert the following employee documents into the `employees` collection:

```javascript
db.employees.insertMany([
  {
    name: "John Doe",
    age: 30,
    department: "IT",
    salary: 50000,
    skills: ["JavaScript", "Python", "MongoDB"]
  },
  {
    name: "Jane Smith",
    age: 28,
    department: "HR",
    salary: 45000,
    skills: ["Communication", "Management"]
  },
  {
    name: "Bob Johnson",
    age: 35,
    department: "IT",
    salary: 60000,
    skills: ["Java", "SQL", "MongoDB"]
  },
  {
    name: "Alice Williams",
    age: 32,
    department: "Finance",
    salary: 55000,
    skills: ["Accounting", "Excel"]
  },
  {
    name: "Charlie Brown",
    age: 29,
    department: "IT",
    salary: 52000,
    skills: ["Python", "Django", "PostgreSQL"]
  }
])
```

### 3. Find Operations

**a) Find all employees**
```javascript
db.employees.find()
```

**b) Find employees in the IT department**
```javascript
db.employees.find({ department: "IT" })
```

**c) Find employees with salary greater than 50000**
```javascript
db.employees.find({ salary: { $gt: 50000 } })
```

**d) Find employees with age between 28 and 32**
```javascript
db.employees.find({ age: { $gte: 28, $lte: 32 } })
```

### 4. Update Operations

**a) Update John Doe's salary to 55000**
```javascript
db.employees.updateOne(
  { name: "John Doe" },
  { $set: { salary: 55000 } }
)
```

**b) Add a new skill "React" to all IT department employees**
```javascript
db.employees.updateMany(
  { department: "IT" },
  { $push: { skills: "React" } }
)
```

**c) Increment the salary of all employees by 5000**
```javascript
db.employees.updateMany(
  {},
  { $inc: { salary: 5000 } }
)
```

### 5. Delete Operations

**a) Delete the employee named "Charlie Brown"**
```javascript
db.employees.deleteOne({ name: "Charlie Brown" })
```

**b) Delete all employees from the HR department**
```javascript
db.employees.deleteMany({ department: "HR" })
```

### 6. Aggregation Operations

**a) Calculate the average salary by department**
```javascript
db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      avgSalary: { $avg: "$salary" }
    }
  }
])
```

**b) Count the number of employees in each department**
```javascript
db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      count: { $sum: 1 }
    }
  }
])
```

**c) Find the highest salary in each department**
```javascript
db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      maxSalary: { $max: "$salary" }
    }
  }
])
```

### 7. Advanced Queries

**a) Find employees who have "MongoDB" skill**
```javascript
db.employees.find({ skills: "MongoDB" })
```

**b) Find employees in IT department with salary greater than 50000**
```javascript
db.employees.find({
  department: "IT",
  salary: { $gt: 50000 }
})
```

**c) Sort employees by salary in descending order**
```javascript
db.employees.find().sort({ salary: -1 })
```

**d) Limit the results to top 3 highest paid employees**
```javascript
db.employees.find().sort({ salary: -1 }).limit(3)
```

### 8. Projection

**a) Display only name and salary fields**
```javascript
db.employees.find({}, { name: 1, salary: 1, _id: 0 })
```

**b) Display all fields except skills**
```javascript
db.employees.find({}, { skills: 0 })
```

### 9. Index Creation

**a) Create an index on the department field**
```javascript
db.employees.createIndex({ department: 1 })
```

**b) Create a compound index on department and salary**
```javascript
db.employees.createIndex({ department: 1, salary: -1 })
```

### 10. Complex Aggregation

**a) Find employees with more than 2 skills**
```javascript
db.employees.aggregate([
  {
    $project: {
      name: 1,
      department: 1,
      skillCount: { $size: "$skills" }
    }
  },
  {
    $match: {
      skillCount: { $gt: 2 }
    }
  }
])
```

**b) Group employees by department and calculate total salary**
```javascript
db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      totalSalary: { $sum: "$salary" },
      avgAge: { $avg: "$age" },
      employeeCount: { $sum: 1 }
    }
  }
])
```

### 11. Array Operations

**a) Find employees who know both "JavaScript" and "MongoDB"**
```javascript
db.employees.find({
  skills: { $all: ["JavaScript", "MongoDB"] }
})
```

**b) Add multiple skills to an employee**
```javascript
db.employees.updateOne(
  { name: "Alice Williams" },
  { $push: { skills: { $each: ["Finance", "Budgeting"] } } }
)
```

**c) Remove a skill from an employee**
```javascript
db.employees.updateOne(
  { name: "Bob Johnson" },
  { $pull: { skills: "SQL" } }
)
```

### 12. Logical Operators

**a) Find employees in IT or Finance department**
```javascript
db.employees.find({
  $or: [
    { department: "IT" },
    { department: "Finance" }
  ]
})
```

**b) Find employees NOT in HR department**
```javascript
db.employees.find({
  department: { $ne: "HR" }
})
```

### 13. Text Search

**a) Create a text index on name field**
```javascript
db.employees.createIndex({ name: "text" })
```

**b) Search for employees with "John" in their name**
```javascript
db.employees.find({ $text: { $search: "John" } })
```

### 14. Data Validation

**a) Add validation rules to the collection**
```javascript
db.createCollection("employees", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "age", "department", "salary"],
      properties: {
        name: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        age: {
          bsonType: "int",
          minimum: 18,
          maximum: 65,
          description: "must be an integer between 18 and 65"
        },
        department: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        salary: {
          bsonType: "number",
          minimum: 0,
          description: "must be a positive number"
        }
      }
    }
  }
})
```

### 15. Backup and Export

**a) Export employees collection to JSON**
```bash
mongoexport --db=company --collection=employees --out=employees.json
```

**b) Import employees collection from JSON**
```bash
mongoimport --db=company --collection=employees --file=employees.json
```

---

## Additional Practice Questions

### 16. Counting and Distinct

**a) Count total number of employees**
```javascript
db.employees.countDocuments()
```

**b) Get distinct departments**
```javascript
db.employees.distinct("department")
```

### 17. Update with Upsert

**a) Update or insert a document if it doesn't exist**
```javascript
db.employees.updateOne(
  { name: "David Lee" },
  {
    $set: {
      age: 27,
      department: "Marketing",
      salary: 48000,
      skills: ["SEO", "Content Writing"]
    }
  },
  { upsert: true }
)
```

### 18. Bulk Operations

**a) Perform multiple operations in bulk**
```javascript
db.employees.bulkWrite([
  {
    insertOne: {
      document: {
        name: "Emma Davis",
        age: 26,
        department: "Marketing",
        salary: 47000,
        skills: ["Digital Marketing", "Analytics"]
      }
    }
  },
  {
    updateMany: {
      filter: { department: "IT" },
      update: { $inc: { salary: 2000 } }
    }
  },
  {
    deleteOne: {
      filter: { age: { $lt: 25 } }
    }
  }
])
```

---

## Notes

- Always use appropriate error handling in production code
- Create indexes on frequently queried fields for better performance
- Use projection to retrieve only necessary fields
- Consider using aggregation pipeline for complex data analysis
- Regular backups are essential for data safety
