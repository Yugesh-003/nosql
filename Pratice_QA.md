Yes. I checked the uploaded MongoDB exercise. It contains **12 database questions**, each with CRUD + aggregation tasks. 

Below are **ready-to-run MongoDB commands** for all of them. You can practice these directly in **MongoDB Compass Shell / mongosh**.

---

# 1. CollegeDB — Students

The question asks you to create `CollegeDB`, insert students, perform CRUD, and find the top 3 departments by average marks. 

### Create database and collection

```javascript
use CollegeDB

db.createCollection("students")
```

### Insert documents

```javascript
db.students.insertMany([
  {
    rollNo: 101,
    name: "Arun",
    department: "Computer Science",
    year: 2,
    marks: 85
  },
  {
    rollNo: 102,
    name: "Bala",
    department: "Commerce",
    year: 2,
    marks: 78
  },
  {
    rollNo: 103,
    name: "Charan",
    department: "Computer Science",
    year: 3,
    marks: 92
  },
  {
    rollNo: 104,
    name: "Divya",
    department: "Mathematics",
    year: 1,
    marks: 88
  },
  {
    rollNo: 105,
    name: "Esha",
    department: "Commerce",
    year: 3,
    marks: 82
  }
])
```

### READ

```javascript
db.students.find()
```

Find one:

```javascript
db.students.findOne({ rollNo: 101 })
```

### UPDATE

```javascript
db.students.updateOne(
  { rollNo: 101 },
  { $set: { marks: 90 } }
)
```

### DELETE

```javascript
db.students.deleteOne({ rollNo: 105 })
```

### Aggregation — Average marks department-wise

```javascript
db.students.aggregate([
  {
    $group: {
      _id: "$department",
      averageMarks: { $avg: "$marks" }
    }
  },
  {
    $project: {
      _id: 0,
      department: "$_id",
      averageMarks: 1
    }
  },
  {
    $sort: { averageMarks: -1 }
  },
  {
    $limit: 3
  }
])
```

**Remember:**

```text
$group → $project → $sort → $limit
```

---

# 2. HospitalDB — Patients

The question requires patient CRUD and an aggregation that matches a disease, groups patients by doctor, counts them, and sorts by count. 

```javascript
use HospitalDB

db.createCollection("patients")
```

### Insert

```javascript
db.patients.insertMany([
  {
    patientId: 1,
    name: "Ravi",
    age: 35,
    gender: "Male",
    disease: "Diabetes",
    doctor: "Dr. Kumar"
  },
  {
    patientId: 2,
    name: "Priya",
    age: 42,
    gender: "Female",
    disease: "Diabetes",
    doctor: "Dr. Kumar"
  },
  {
    patientId: 3,
    name: "Arun",
    age: 28,
    gender: "Male",
    disease: "Fever",
    doctor: "Dr. Raj"
  },
  {
    patientId: 4,
    name: "Meena",
    age: 50,
    gender: "Female",
    disease: "Diabetes",
    doctor: "Dr. Raj"
  }
])
```

### Query

```javascript
db.patients.find({ disease: "Diabetes" })
```

### Update

```javascript
db.patients.updateOne(
  { patientId: 1 },
  { $set: { age: 36 } }
)
```

### Delete

```javascript
db.patients.deleteOne({ patientId: 4 })
```

### Aggregation

```javascript
db.patients.aggregate([
  {
    $match: {
      disease: "Diabetes"
    }
  },
  {
    $group: {
      _id: "$doctor",
      patientCount: { $sum: 1 }
    }
  },
  {
    $sort: {
      patientCount: -1
    }
  }
])
```

---

# 3. LibraryDB — Books

The question asks for CRUD and the **five most expensive available books**, showing only title, author and price. 

```javascript
use LibraryDB

db.createCollection("books")
```

### Insert

```javascript
db.books.insertMany([
  {
    ISBN: "ISBN001",
    title: "MongoDB Basics",
    author: "John",
    category: "Database",
    price: 800,
    availability: true
  },
  {
    ISBN: "ISBN002",
    title: "Python Programming",
    author: "David",
    category: "Programming",
    price: 1200,
    availability: true
  },
  {
    ISBN: "ISBN003",
    title: "Data Science",
    author: "Smith",
    category: "Data Science",
    price: 1500,
    availability: true
  },
  {
    ISBN: "ISBN004",
    title: "Web Development",
    author: "James",
    category: "Web",
    price: 900,
    availability: false
  },
  {
    ISBN: "ISBN005",
    title: "Machine Learning",
    author: "Alex",
    category: "AI",
    price: 1800,
    availability: true
  }
])
```

### CRUD

```javascript
db.books.find()
```

```javascript
db.books.find({ availability: true })
```

```javascript
db.books.updateOne(
  { ISBN: "ISBN001" },
  { $set: { price: 850 } }
)
```

```javascript
db.books.deleteOne({ ISBN: "ISBN004" })
```

### Aggregation

```javascript
db.books.aggregate([
  {
    $match: {
      availability: true
    }
  },
  {
    $project: {
      _id: 0,
      title: 1,
      author: 1,
      price: 1
    }
  },
  {
    $sort: {
      price: -1
    }
  },
  {
    $limit: 5
  }
])
```

**Pattern:**

```text
$match → $project → $sort → $limit
```

---

# 4. BankDB — Accounts

The question asks for account insertion, update/delete, and average balance branch-wise with the top 5 branches. 

```javascript
use BankDB

db.createCollection("accounts")
```

### Insert

```javascript
db.accounts.insertMany([
  {
    accountNo: 1001,
    customerName: "Arun",
    accountType: "Savings",
    balance: 50000,
    branch: "Madurai"
  },
  {
    accountNo: 1002,
    customerName: "Bala",
    accountType: "Current",
    balance: 80000,
    branch: "Chennai"
  },
  {
    accountNo: 1003,
    customerName: "Charan",
    accountType: "Savings",
    balance: 60000,
    branch: "Madurai"
  },
  {
    accountNo: 1004,
    customerName: "Divya",
    accountType: "Savings",
    balance: 90000,
    branch: "Chennai"
  }
])
```

### Update

```javascript
db.accounts.updateOne(
  { accountNo: 1001 },
  { $set: { balance: 55000 } }
)
```

### Delete

```javascript
db.accounts.deleteOne({ accountNo: 1004 })
```

### Aggregation

```javascript
db.accounts.aggregate([
  {
    $group: {
      _id: "$branch",
      averageBalance: { $avg: "$balance" }
    }
  },
  {
    $sort: {
      averageBalance: -1
    }
  },
  {
    $limit: 5
  }
])
```

---

# 5. ShopDB — Products

The question asks for CRUD and an aggregation to filter a category, project fields, sort by price, and display the first 10. 

```javascript
use ShopDB

db.createCollection("products")
```

### Insert

```javascript
db.products.insertMany([
  {
    productId: 1,
    name: "Laptop",
    category: "Electronics",
    brand: "HP",
    price: 55000,
    stock: 10
  },
  {
    productId: 2,
    name: "Mouse",
    category: "Electronics",
    brand: "Logitech",
    price: 800,
    stock: 50
  },
  {
    productId: 3,
    name: "Keyboard",
    category: "Electronics",
    brand: "Dell",
    price: 1500,
    stock: 30
  }
])
```

### CRUD

```javascript
db.products.find()
```

```javascript
db.products.find({ category: "Electronics" })
```

```javascript
db.products.updateOne(
  { productId: 1 },
  { $set: { stock: 15 } }
)
```

```javascript
db.products.deleteOne({ productId: 3 })
```

### Aggregation

```javascript
db.products.aggregate([
  {
    $match: {
      category: "Electronics"
    }
  },
  {
    $project: {
      _id: 0,
      name: 1,
      brand: 1,
      price: 1
    }
  },
  {
    $sort: {
      price: -1
    }
  },
  {
    $limit: 10
  }
])
```

---

# 6. EmployeeDB — Employees

The question asks for CRUD and department-wise average salary and employee count, sorted by average salary. 

```javascript
use EmployeeDB

db.createCollection("employees")
```

### Insert

```javascript
db.employees.insertMany([
  {
    employeeId: 1,
    name: "Arun",
    department: "IT",
    designation: "Developer",
    salary: 50000,
    experience: 2
  },
  {
    employeeId: 2,
    name: "Bala",
    department: "HR",
    designation: "Manager",
    salary: 60000,
    experience: 5
  },
  {
    employeeId: 3,
    name: "Charan",
    department: "IT",
    designation: "Developer",
    salary: 55000,
    experience: 3
  },
  {
    employeeId: 4,
    name: "Divya",
    department: "Sales",
    designation: "Executive",
    salary: 45000,
    experience: 2
  }
])
```

### CRUD

```javascript
db.employees.find()
```

```javascript
db.employees.find({ department: "IT" })
```

```javascript
db.employees.updateOne(
  { employeeId: 1 },
  { $set: { salary: 52000 } }
)
```

```javascript
db.employees.deleteOne({ employeeId: 4 })
```

### Aggregation

```javascript
db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      averageSalary: { $avg: "$salary" },
      totalEmployees: { $sum: 1 }
    }
  },
  {
    $sort: {
      averageSalary: -1
    }
  }
])
```

---

# 7. MovieDB — Movies

The question asks for CRUD and the **top 5 highest-rated movies released after 2020**. 

```javascript
use MovieDB

db.createCollection("movies")
```

### Insert

```javascript
db.movies.insertMany([
  {
    movieName: "Movie A",
    director: "Director A",
    genre: "Action",
    year: 2021,
    rating: 8.5,
    actors: ["Actor A", "Actor B"]
  },
  {
    movieName: "Movie B",
    director: "Director B",
    genre: "Drama",
    year: 2022,
    rating: 9.1,
    actors: ["Actor C", "Actor D"]
  },
  {
    movieName: "Movie C",
    director: "Director C",
    genre: "Comedy",
    year: 2019,
    rating: 9.5,
    actors: ["Actor E", "Actor F"]
  }
])
```

### CRUD

```javascript
db.movies.find()
```

```javascript
db.movies.find({ genre: "Action" })
```

```javascript
db.movies.updateOne(
  { movieName: "Movie A" },
  { $set: { rating: 8.8 } }
)
```

```javascript
db.movies.deleteOne({ movieName: "Movie C" })
```

### Aggregation

```javascript
db.movies.aggregate([
  {
    $match: {
      year: { $gt: 2020 }
    }
  },
  {
    $sort: {
      rating: -1
    }
  },
  {
    $limit: 5
  }
])
```

---

# 8. TravelDB — Tourists

The question asks for CRUD and average package cost for each destination, sorted descending. 

```javascript
use TravelDB

db.createCollection("tourists")
```

### Insert

```javascript
db.tourists.insertMany([
  {
    touristId: 1,
    name: "Arun",
    destination: "Goa",
    age: 25,
    country: "India",
    packageCost: 25000
  },
  {
    touristId: 2,
    name: "Bala",
    destination: "Goa",
    age: 30,
    country: "India",
    packageCost: 30000
  },
  {
    touristId: 3,
    name: "John",
    destination: "Dubai",
    age: 28,
    country: "USA",
    packageCost: 60000
  }
])
```

### CRUD

```javascript
db.tourists.find()
```

```javascript
db.tourists.find({ destination: "Goa" })
```

```javascript
db.tourists.updateOne(
  { touristId: 1 },
  { $set: { packageCost: 27000 } }
)
```

```javascript
db.tourists.deleteOne({ touristId: 3 })
```

### Aggregation

```javascript
db.tourists.aggregate([
  {
    $group: {
      _id: "$destination",
      averageCost: { $avg: "$packageCost" }
    }
  },
  {
    $sort: {
      averageCost: -1
    }
  }
])
```

---

# 9. HotelDB — Bookings

The question asks for CRUD and total booking amount for each hotel, sorted by revenue and limited to 5. 

```javascript
use HotelDB

db.createCollection("bookings")
```

### Insert

```javascript
db.bookings.insertMany([
  {
    bookingId: 1,
    customerName: "Arun",
    hotel: "Hotel A",
    roomType: "Deluxe",
    nights: 3,
    amount: 15000
  },
  {
    bookingId: 2,
    customerName: "Bala",
    hotel: "Hotel A",
    roomType: "Suite",
    nights: 2,
    amount: 20000
  },
  {
    bookingId: 3,
    customerName: "Charan",
    hotel: "Hotel B",
    roomType: "Standard",
    nights: 4,
    amount: 12000
  }
])
```

### CRUD

```javascript
db.bookings.find()
```

```javascript
db.bookings.find({ hotel: "Hotel A" })
```

```javascript
db.bookings.updateOne(
  { bookingId: 1 },
  { $set: { nights: 4 } }
)
```

```javascript
db.bookings.deleteOne({ bookingId: 3 })
```

### Aggregation

```javascript
db.bookings.aggregate([
  {
    $group: {
      _id: "$hotel",
      totalRevenue: { $sum: "$amount" }
    }
  },
  {
    $sort: {
      totalRevenue: -1
    }
  },
  {
    $limit: 5
  }
])
```

---

# 10. EcommerceDB — Orders

The question specifically asks to calculate **order value = quantity × price**, then group by category and find average order value. 

```javascript
use EcommerceDB

db.createCollection("orders")
```

### Insert

```javascript
db.orders.insertMany([
  {
    orderId: 1,
    customer: "Arun",
    product: "Laptop",
    category: "Electronics",
    quantity: 2,
    price: 50000,
    orderDate: "2026-08-01"
  },
  {
    orderId: 2,
    customer: "Bala",
    product: "Mouse",
    category: "Electronics",
    quantity: 3,
    price: 800,
    orderDate: "2026-08-02"
  },
  {
    orderId: 3,
    customer: "Charan",
    product: "Shirt",
    category: "Clothing",
    quantity: 2,
    price: 1200,
    orderDate: "2026-08-03"
  }
])
```

### CRUD

```javascript
db.orders.find()
```

```javascript
db.orders.find({ category: "Electronics" })
```

```javascript
db.orders.updateOne(
  { orderId: 1 },
  { $set: { quantity: 3 } }
)
```

```javascript
db.orders.deleteOne({ orderId: 3 })
```

### Aggregation

```javascript
db.orders.aggregate([
  {
    $project: {
      category: 1,
      orderValue: {
        $multiply: ["$quantity", "$price"]
      }
    }
  },
  {
    $group: {
      _id: "$category",
      averageOrderValue: {
        $avg: "$orderValue"
      }
    }
  }
])
```

### Important

For multiplication:

```javascript
$multiply: ["$quantity", "$price"]
```

---

# 11. SportsDB — Players

The question asks to group players by team, calculate average performance score, sort teams, and show the top 3. 

```javascript
use SportsDB

db.createCollection("players")
```

### Insert

```javascript
db.players.insertMany([
  {
    playerName: "Arun",
    team: "Team A",
    sport: "Cricket",
    age: 25,
    matches: 50,
    runsGoals: 2500,
    country: "India"
  },
  {
    playerName: "Bala",
    team: "Team A",
    sport: "Cricket",
    age: 27,
    matches: 60,
    runsGoals: 3000,
    country: "India"
  },
  {
    playerName: "John",
    team: "Team B",
    sport: "Football",
    age: 24,
    matches: 40,
    runsGoals: 30,
    country: "UK"
  }
])
```

### CRUD

```javascript
db.players.find()
```

```javascript
db.players.find({ team: "Team A" })
```

```javascript
db.players.updateOne(
  { playerName: "Arun" },
  { $set: { runsGoals: 2700 } }
)
```

```javascript
db.players.deleteOne({ playerName: "John" })
```

### Aggregation

Here, since the question calls it a **performance score** but doesn't give a formula, the simplest interpretation is to use `runsGoals` as the performance score.

```javascript
db.players.aggregate([
  {
    $group: {
      _id: "$team",
      averagePerformance: {
        $avg: "$runsGoals"
      }
    }
  },
  {
    $sort: {
      averagePerformance: -1
    }
  },
  {
    $limit: 3
  }
])
```

---

# 12. SchoolDB — Students + Courses

This is the important one because it introduces **arrays and `$unwind`**. The question requires students to have enrolled courses and asks to display each course separately and count students per course. 

```javascript
use SchoolDB

db.createCollection("students")
```

### Insert

```javascript
db.students.insertMany([
  {
    studentId: 1,
    name: "Arun",
    age: 20,
    department: "Computer Science",
    courses: ["MongoDB", "Python", "Data Science"]
  },
  {
    studentId: 2,
    name: "Bala",
    age: 21,
    department: "Computer Science",
    courses: ["MongoDB", "Java"]
  },
  {
    studentId: 3,
    name: "Charan",
    age: 20,
    department: "Commerce",
    courses: ["Python", "Data Science"]
  }
])
```

### Query

```javascript
db.students.find()
```

Find students taking MongoDB:

```javascript
db.students.find({
  courses: "MongoDB"
})
```

### Update

Add a course:

```javascript
db.students.updateOne(
  { studentId: 1 },
  { $push: { courses: "Java" } }
)
```

### Delete

```javascript
db.students.deleteOne({
  studentId: 3
})
```

### `$unwind`

```javascript
db.students.aggregate([
  {
    $unwind: "$courses"
  }
])
```

This changes:

```text
Arun → [MongoDB, Python, Data Science]
```

into:

```text
Arun → MongoDB
Arun → Python
Arun → Data Science
```

### Count students in each course

```javascript
db.students.aggregate([
  {
    $unwind: "$courses"
  },
  {
    $group: {
      _id: "$courses",
      studentCount: { $sum: 1 }
    }
  }
])
```

---

# Most Important MongoDB Patterns to Memorize

For your internal exam, **don't memorize all 12 programs separately**. Memorize these patterns.

### 1. Database

```javascript
use DatabaseName
```

### 2. Collection

```javascript
db.createCollection("collectionName")
```

### 3. Insert one

```javascript
db.collection.insertOne({
  field: "value"
})
```

### 4. Insert many

```javascript
db.collection.insertMany([
  { field: "value1" },
  { field: "value2" }
])
```

### 5. Read

```javascript
db.collection.find()
```

### 6. Find with condition

```javascript
db.collection.find({
  field: "value"
})
```

### 7. Update

```javascript
db.collection.updateOne(
  { field: "oldValue" },
  { $set: { field: "newValue" } }
)
```

### 8. Delete

```javascript
db.collection.deleteOne({
  field: "value"
})
```

---

# Aggregation Cheat Sheet

This is the part I'd memorize most.

### `$match` = WHERE

```javascript
{
  $match: {
    disease: "Diabetes"
  }
}
```

### `$group` = GROUP BY

```javascript
{
  $group: {
    _id: "$department",
    average: { $avg: "$marks" }
  }
}
```

### `$sum` = COUNT / TOTAL

Count:

```javascript
{ $sum: 1 }
```

Total:

```javascript
{ $sum: "$amount" }
```

### `$avg` = Average

```javascript
{ $avg: "$salary" }
```

### `$sort`

Descending:

```javascript
{ $sort: { marks: -1 } }
```

Ascending:

```javascript
{ $sort: { marks: 1 } }
```

**Remember:**

```text
1  = ascending
-1 = descending
```

### `$limit`

```javascript
{
  $limit: 5
}
```

### `$project`

Choose fields:

```javascript
{
  $project: {
    _id: 0,
    name: 1,
    price: 1
  }
}
```

### `$multiply`

```javascript
{
  $multiply: ["$quantity", "$price"]
}
```

### `$unwind`

Used when you have an **array**:

```javascript
{
  $unwind: "$courses"
}
```

---

## The 6 aggregation combinations you really need

| Question type           | Pattern                              |
| ----------------------- | ------------------------------------ |
| Average department-wise | `$group → $avg → $sort`              |
| Count by doctor         | `$match → $group → $sum → $sort`     |
| Top expensive items     | `$match → $project → $sort → $limit` |
| Top-rated movies        | `$match → $sort → $limit`            |
| Total revenue           | `$group → $sum → $sort → $limit`     |
| Array/course counting   | `$unwind → $group → $sum`            |

If you understand these **6 patterns**, you can solve essentially every aggregation question in this paper by changing only the database, collection, and field names.
