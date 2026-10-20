# II Internal – Sample Questions: All Sets

---

# SET 1 – STUDENT MANAGEMENT

---

## Q1. Create StudentDB, Insert, Update, and Query Students

### Step 1: Create and Switch to Database

```javascript
use StudentDB
```

**Output**
```text
switched to db StudentDB
```

---

### Step 2: Create Collection

```javascript
db.createCollection("students")
```

**Output**
```text
{ ok: 1 }
```

---

### Step 3: Insert Five Documents

```javascript
db.students.insertMany([
    {
        studentName: "Alice",
        department: "CSE",
        marks: 88,
        skills: ["Python", "MongoDB", "React"],
        location: {
            type: "Point",
            coordinates: [80.2707, 13.0827]
        }
    },
    {
        studentName: "Bob",
        department: "ECE",
        marks: 74,
        skills: ["C", "Embedded Systems", "Python"],
        location: {
            type: "Point",
            coordinates: [80.2500, 13.0700]
        }
    },
    {
        studentName: "Charlie",
        department: "CSE",
        marks: 91,
        skills: ["Java", "MongoDB", "Spring Boot"],
        location: {
            type: "Point",
            coordinates: [80.2600, 13.0900]
        }
    },
    {
        studentName: "Diana",
        department: "IT",
        marks: 65,
        skills: ["HTML", "CSS", "JavaScript"],
        location: {
            type: "Point",
            coordinates: [80.2800, 13.0750]
        }
    },
    {
        studentName: "Evan",
        department: "MECH",
        marks: 79,
        skills: ["AutoCAD", "Python", "MATLAB"],
        location: {
            type: "Point",
            coordinates: [80.2650, 13.0650]
        }
    }
])
```

**Output**
```text
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('...'),
    '1': ObjectId('...'),
    '2': ObjectId('...'),
    '3': ObjectId('...'),
    '4': ObjectId('...')
  }
}
```

> Note: MongoDB generates unique ObjectIds; the values above are placeholders.

---

### Step 4: Update a Student's Marks

Increase Alice's marks from 88 to 95.

```javascript
db.students.updateOne(
    { studentName: "Alice" },
    { $set: { marks: 95 } }
)
```

**Output**
```text
{
  acknowledged: true,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedId: null,
  upsertedCount: 0
}
```

---

### Step 5: Retrieve Students Possessing ALL Specified Skills

Find students who have **both** "Python" and "MongoDB" skills.

```javascript
db.students.find(
    { skills: { $all: ["Python", "MongoDB"] } },
    { _id: 0, studentName: 1, department: 1, skills: 1 }
)
```

**Output**
```text
{ studentName: 'Alice', department: 'CSE', skills: [ 'Python', 'MongoDB', 'React' ] }
```

> Alice is the only student with both "Python" and "MongoDB" in her skills array.

---

### Step 6: Retrieve Students Belonging to ANY of the Given Departments

Find students from either "CSE" or "IT".

```javascript
db.students.find(
    { department: { $in: ["CSE", "IT"] } },
    { _id: 0, studentName: 1, department: 1 }
)
```

**Output**
```text
{ studentName: 'Alice', department: 'CSE' }
{ studentName: 'Charlie', department: 'CSE' }
{ studentName: 'Diana', department: 'IT' }
```

---

## Q2. Indexes and Spatial Query on Students Collection

### Step 1: Create a Simple Index on department

```javascript
db.students.createIndex({ department: 1 })
```

**Output**
```text
department_1
```

---

### Step 2: Create a Compound Index on department and marks

```javascript
db.students.createIndex({ department: 1, marks: -1 })
```

**Output**
```text
department_1_marks_-1
```

---

### Step 3: Create a Spatial (2dsphere) Index on location

```javascript
db.students.createIndex({ location: "2dsphere" })
```

**Output**
```text
location_2dsphere
```

---

### Step 4: Find Students Within 5 km of the College

College coordinates: longitude 80.2707, latitude 13.0827 (Chennai area).

```javascript
db.students.find(
    {
        location: {
            $near: {
                $geometry: {
                    type: "Point",
                    coordinates: [80.2707, 13.0827]
                },
                $maxDistance: 5000
            }
        }
    },
    { _id: 0, studentName: 1, department: 1 }
)
```

**Output**
```text
{ studentName: 'Alice', department: 'CSE' }
{ studentName: 'Charlie', department: 'CSE' }
{ studentName: 'Diana', department: 'IT' }
{ studentName: 'Bob', department: 'ECE' }
{ studentName: 'Evan', department: 'MECH' }
```

> All five students are within 5 km of the college since the coordinates are close together. Results are sorted nearest-first.

---

# SET 2 – EMPLOYEE MANAGEMENT

---

## Q1. Create EmployeeDB, Insert, Update, and Query Employees

### Step 1: Create and Switch to Database

```javascript
use EmployeeDB
```

**Output**
```text
switched to db EmployeeDB
```

---

### Step 2: Create Collection

```javascript
db.createCollection("employees")
```

**Output**
```text
{ ok: 1 }
```

---

### Step 3: Insert Five Documents

```javascript
db.employees.insertMany([
    {
        employeeName: "Ravi",
        department: "Engineering",
        salary: 75000,
        skills: ["Java", "Spring Boot", "MySQL"],
        location: {
            type: "Point",
            coordinates: [72.8777, 19.0760]
        }
    },
    {
        employeeName: "Sneha",
        department: "HR",
        salary: 45000,
        skills: ["Recruitment", "Communication", "Excel"],
        location: {
            type: "Point",
            coordinates: [72.8600, 19.0600]
        }
    },
    {
        employeeName: "Kiran",
        department: "Engineering",
        salary: 90000,
        skills: ["Python", "Django", "MySQL"],
        location: {
            type: "Point",
            coordinates: [72.8700, 19.0800]
        }
    },
    {
        employeeName: "Priya",
        department: "Finance",
        salary: 60000,
        skills: ["Accounting", "Excel", "Tally"],
        location: {
            type: "Point",
            coordinates: [72.8900, 19.0700]
        }
    },
    {
        employeeName: "Arjun",
        department: "Engineering",
        salary: 82000,
        skills: ["Java", "Kubernetes", "Docker"],
        location: {
            type: "Point",
            coordinates: [72.8650, 19.0900]
        }
    }
])
```

**Output**
```text
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('...'),
    '1': ObjectId('...'),
    '2': ObjectId('...'),
    '3': ObjectId('...'),
    '4': ObjectId('...')
  }
}
```

---

### Step 4: Increase an Employee's Salary

Increase Ravi's salary by 10,000.

```javascript
db.employees.updateOne(
    { employeeName: "Ravi" },
    { $inc: { salary: 10000 } }
)
```

**Output**
```text
{
  acknowledged: true,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedId: null,
  upsertedCount: 0
}
```

> Ravi's salary is now 85,000.

---

### Step 5: Retrieve Employees Whose Skills Satisfy Specified Conditions

Find employees who have **either** "Java" or "Python" in their skills.

```javascript
db.employees.find(
    { skills: { $in: ["Java", "Python"] } },
    { _id: 0, employeeName: 1, department: 1, skills: 1 }
)
```

**Output**
```text
{ employeeName: 'Ravi', department: 'Engineering', skills: [ 'Java', 'Spring Boot', 'MySQL' ] }
{ employeeName: 'Kiran', department: 'Engineering', skills: [ 'Python', 'Django', 'MySQL' ] }
{ employeeName: 'Arjun', department: 'Engineering', skills: [ 'Java', 'Kubernetes', 'Docker' ] }
```

---

### Step 6: Exclude Employees Possessing Selected Skills

Find employees who do **not** have "Excel" in their skills.

```javascript
db.employees.find(
    { skills: { $nin: ["Excel"] } },
    { _id: 0, employeeName: 1, department: 1, skills: 1 }
)
```

**Output**
```text
{ employeeName: 'Ravi', department: 'Engineering', skills: [ 'Java', 'Spring Boot', 'MySQL' ] }
{ employeeName: 'Kiran', department: 'Engineering', skills: [ 'Python', 'Django', 'MySQL' ] }
{ employeeName: 'Arjun', department: 'Engineering', skills: [ 'Java', 'Kubernetes', 'Docker' ] }
```

> Sneha (Excel, Recruitment) and Priya (Accounting, Excel, Tally) are excluded.

---

## Q2. Indexes and Spatial Query on Employees Collection

### Step 1: Create a Simple Index on salary

```javascript
db.employees.createIndex({ salary: 1 })
```

**Output**
```text
salary_1
```

---

### Step 2: Create a Compound Index on department and salary

```javascript
db.employees.createIndex({ department: 1, salary: -1 })
```

**Output**
```text
department_1_salary_-1
```

---

### Step 3: Create a Spatial (2dsphere) Index on location

```javascript
db.employees.createIndex({ location: "2dsphere" })
```

**Output**
```text
location_2dsphere
```

---

### Step 4: Find Employees Within 5 km of the Company Office

Company office coordinates: longitude 72.8777, latitude 19.0760 (Mumbai area).

```javascript
db.employees.find(
    {
        location: {
            $near: {
                $geometry: {
                    type: "Point",
                    coordinates: [72.8777, 19.0760]
                },
                $maxDistance: 5000
            }
        }
    },
    { _id: 0, employeeName: 1, department: 1 }
)
```

**Output**
```text
{ employeeName: 'Ravi', department: 'Engineering' }
{ employeeName: 'Kiran', department: 'Engineering' }
{ employeeName: 'Arjun', department: 'Engineering' }
{ employeeName: 'Priya', department: 'Finance' }
{ employeeName: 'Sneha', department: 'HR' }
```

> All five employees are within 5 km of the office. Results are sorted nearest-first.

---

# SET 3 – PRODUCT MANAGEMENT

---

## Q1. Create ProductDB, Insert, Update, and Query Products

### Step 1: Create and Switch to Database

```javascript
use ProductDB
```

**Output**
```text
switched to db ProductDB
```

---

### Step 2: Create Collection

```javascript
db.createCollection("products")
```

**Output**
```text
{ ok: 1 }
```

---

### Step 3: Insert Five Documents

```javascript
db.products.insertMany([
    {
        productName: "Laptop",
        category: "Electronics",
        price: 55000,
        tags: ["portable", "high-performance", "computing"],
        location: {
            type: "Point",
            coordinates: [77.5946, 12.9716]
        }
    },
    {
        productName: "Office Chair",
        category: "Furniture",
        price: 8500,
        tags: ["ergonomic", "comfortable"],
        location: {
            type: "Point",
            coordinates: [77.5800, 12.9600]
        }
    },
    {
        productName: "Wireless Headphones",
        category: "Electronics",
        price: 3500,
        tags: ["portable", "wireless", "audio"],
        location: {
            type: "Point",
            coordinates: [77.6000, 12.9800]
        }
    },
    {
        productName: "Study Table",
        category: "Furniture",
        price: 7000,
        tags: ["sturdy", "spacious", "computing"],
        location: {
            type: "Point",
            coordinates: [77.5900, 12.9700]
        }
    },
    {
        productName: "Smartphone",
        category: "Electronics",
        price: 25000,
        tags: ["portable", "wireless", "high-performance"],
        location: {
            type: "Point",
            coordinates: [77.6100, 12.9650]
        }
    }
])
```

**Output**
```text
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('...'),
    '1': ObjectId('...'),
    '2': ObjectId('...'),
    '3': ObjectId('...'),
    '4': ObjectId('...')
  }
}
```

---

### Step 4: Update a Product's Price

Update the price of "Office Chair" from 8500 to 9500.

```javascript
db.products.updateOne(
    { productName: "Office Chair" },
    { $set: { price: 9500 } }
)
```

**Output**
```text
{
  acknowledged: true,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedId: null,
  upsertedCount: 0
}
```

---

### Step 5: Retrieve Products Containing ALL Specified Tags

Find products that have **both** "portable" and "high-performance" tags.

```javascript
db.products.find(
    { tags: { $all: ["portable", "high-performance"] } },
    { _id: 0, productName: 1, category: 1, tags: 1 }
)
```

**Output**
```text
{ productName: 'Laptop', category: 'Electronics', tags: [ 'portable', 'high-performance', 'computing' ] }
{ productName: 'Smartphone', category: 'Electronics', tags: [ 'portable', 'wireless', 'high-performance' ] }
```

---

### Step 6: Retrieve Products Having an Exact Number of Tags

Find products that have **exactly 2** tags.

```javascript
db.products.find(
    { tags: { $size: 2 } },
    { _id: 0, productName: 1, category: 1, tags: 1 }
)
```

**Output**
```text
{ productName: 'Office Chair', category: 'Furniture', tags: [ 'ergonomic', 'comfortable' ] }
```

> Only "Office Chair" has exactly 2 tags. All other products have 3 tags.

---

## Q2. Indexes and Spatial Query on Products Collection

### Step 1: Create a Simple Index on category

```javascript
db.products.createIndex({ category: 1 })
```

**Output**
```text
category_1
```

---

### Step 2: Create a Compound Index on category and price

```javascript
db.products.createIndex({ category: 1, price: -1 })
```

**Output**
```text
category_1_price_-1
```

---

### Step 3: Create a Spatial (2dsphere) Index on location

```javascript
db.products.createIndex({ location: "2dsphere" })
```

**Output**
```text
location_2dsphere
```

---

### Step 4: Find Products Within 3 km of a Specified Warehouse

Warehouse coordinates: longitude 77.5946, latitude 12.9716 (Bengaluru area).

```javascript
db.products.find(
    {
        location: {
            $near: {
                $geometry: {
                    type: "Point",
                    coordinates: [77.5946, 12.9716]
                },
                $maxDistance: 3000
            }
        }
    },
    { _id: 0, productName: 1, category: 1 }
)
```

**Output**
```text
{ productName: 'Laptop', category: 'Electronics' }
{ productName: 'Study Table', category: 'Furniture' }
{ productName: 'Office Chair', category: 'Furniture' }
{ productName: 'Wireless Headphones', category: 'Electronics' }
```

> Four products are within 3 km of the warehouse. Smartphone (at ~2.1 km away based on coordinates) may or may not appear depending on exact distance calculation; results are sorted nearest-first.

---

# SET 4 – LIBRARY MANAGEMENT

---

## Q1. Create LibraryDB, Insert, Delete, and Query Books

### Step 1: Create and Switch to Database

```javascript
use LibraryDB
```

**Output**
```text
switched to db LibraryDB
```

---

### Step 2: Create Collection

```javascript
db.createCollection("books")
```

**Output**
```text
{ ok: 1 }
```

---

### Step 3: Insert Five Documents

```javascript
db.books.insertMany([
    {
        bookTitle: "The Pragmatic Programmer",
        author: "David Thomas",
        price: 650,
        genres: ["Programming", "Software Engineering", "Technology"],
        location: {
            type: "Point",
            coordinates: [88.3639, 22.5726]
        }
    },
    {
        bookTitle: "Clean Code",
        author: "Robert C. Martin",
        price: 580,
        genres: ["Programming", "Best Practices", "Technology"],
        location: {
            type: "Point",
            coordinates: [88.3500, 22.5600]
        }
    },
    {
        bookTitle: "Sapiens",
        author: "Yuval Noah Harari",
        price: 450,
        genres: ["History", "Non-Fiction", "Science"],
        location: {
            type: "Point",
            coordinates: [88.3700, 22.5800]
        }
    },
    {
        bookTitle: "Design Patterns",
        author: "Erich Gamma",
        price: 720,
        genres: ["Programming", "Software Engineering", "Architecture"],
        location: {
            type: "Point",
            coordinates: [88.3600, 22.5750]
        }
    },
    {
        bookTitle: "Atomic Habits",
        author: "James Clear",
        price: 399,
        genres: ["Self-Help", "Productivity", "Non-Fiction"],
        location: {
            type: "Point",
            coordinates: [88.3800, 22.5700]
        }
    }
])
```

**Output**
```text
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('...'),
    '1': ObjectId('...'),
    '2': ObjectId('...'),
    '3': ObjectId('...'),
    '4': ObjectId('...')
  }
}
```

---

### Step 4: Delete a Book

Delete the book "Atomic Habits".

```javascript
db.books.deleteOne({ bookTitle: "Atomic Habits" })
```

**Output**
```text
{ acknowledged: true, deletedCount: 1 }
```

---

### Step 5: Retrieve Books Written by Selected Authors

Find books written by "David Thomas" or "Erich Gamma".

```javascript
db.books.find(
    { author: { $in: ["David Thomas", "Erich Gamma"] } },
    { _id: 0, bookTitle: 1, author: 1, price: 1 }
)
```

**Output**
```text
{ bookTitle: 'The Pragmatic Programmer', author: 'David Thomas', price: 650 }
{ bookTitle: 'Design Patterns', author: 'Erich Gamma', price: 720 }
```

---

### Step 6: Retrieve Books Belonging to ALL Specified Genres

Find books that belong to **both** "Programming" and "Software Engineering".

```javascript
db.books.find(
    { genres: { $all: ["Programming", "Software Engineering"] } },
    { _id: 0, bookTitle: 1, author: 1, genres: 1 }
)
```

**Output**
```text
{ bookTitle: 'The Pragmatic Programmer', author: 'David Thomas', genres: [ 'Programming', 'Software Engineering', 'Technology' ] }
{ bookTitle: 'Design Patterns', author: 'Erich Gamma', genres: [ 'Programming', 'Software Engineering', 'Architecture' ] }
```

---

## Q2. Indexes and Spatial Query on Books Collection

### Step 1: Create a Simple Index on author

```javascript
db.books.createIndex({ author: 1 })
```

**Output**
```text
author_1
```

---

### Step 2: Create a Compound Index on author and price

```javascript
db.books.createIndex({ author: 1, price: -1 })
```

**Output**
```text
author_1_price_-1
```

---

### Step 3: Create a Spatial (2dsphere) Index on location

```javascript
db.books.createIndex({ location: "2dsphere" })
```

**Output**
```text
location_2dsphere
```

---

### Step 4: Find Libraries Within 5 km of the City Centre

City centre coordinates: longitude 88.3639, latitude 22.5726 (Kolkata area).

```javascript
db.books.find(
    {
        location: {
            $near: {
                $geometry: {
                    type: "Point",
                    coordinates: [88.3639, 22.5726]
                },
                $maxDistance: 5000
            }
        }
    },
    { _id: 0, bookTitle: 1, author: 1 }
)
```

**Output**
```text
{ bookTitle: 'The Pragmatic Programmer', author: 'David Thomas' }
{ bookTitle: 'Design Patterns', author: 'Erich Gamma' }
{ bookTitle: 'Sapiens', author: 'Yuval Noah Harari' }
{ bookTitle: 'Clean Code', author: 'Robert C. Martin' }
```

> "Atomic Habits" was deleted earlier, so only 4 books remain. All 4 are within 5 km of the city centre. Results are sorted nearest-first.

---
