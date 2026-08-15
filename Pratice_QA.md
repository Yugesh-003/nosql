Yes. I checked the uploaded MongoDB exercise. It contains **12 database questions**, each with CRUD + aggregation tasks. 

Below are **ready-to-run MongoDB commands** for all of them. You can practice these directly in **MongoDB Compass Shell / mongosh**.

---

# 1. CollegeDB — Students

The question asks you to create `CollegeDB`, insert students, perform CRUD, and find the top 3 departments by average marks. 

### Create database and collection

> Switches to (or creates) `CollegeDB`, then explicitly creates an empty `students` collection.

```javascript
use CollegeDB

db.createCollection("students")
```

### Insert documents

> Inserts 5 student documents at once with fields like rollNo, name, department, year, and marks.

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

> Retrieves and displays every document in the `students` collection.

```javascript
db.students.find()
```

> Returns only the first document where `rollNo` equals 101.

```javascript
db.students.findOne({ rollNo: 101 })
```

### UPDATE

> Finds student with `rollNo` 101 and changes only their `marks` field to 90 — all other fields remain untouched.

```javascript
db.students.updateOne(
  { rollNo: 101 },
  { $set: { marks: 90 } }
)
```

### DELETE

> Permanently removes the first document where `rollNo` equals 105 from the collection.

```javascript
db.students.deleteOne({ rollNo: 105 })
```

### Aggregation — Average marks department-wise

> Groups students by department, calculates average marks, hides the `_id` field, renames it to `department`, sorts by highest average first, and returns only the top 3 departments.

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

> Switches to `HospitalDB` and creates an empty `patients` collection.

```javascript
use HospitalDB

db.createCollection("patients")
```

### Insert

> Inserts 4 patient documents, each with details like disease and assigned doctor.

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

> Finds all patients whose `disease` field is exactly "Diabetes".

```javascript
db.patients.find({ disease: "Diabetes" })
```

### Update

> Updates only the `age` field of patient 1 to 36, leaving all other fields unchanged.

```javascript
db.patients.updateOne(
  { patientId: 1 },
  { $set: { age: 36 } }
)
```

### Delete

> Removes the document for patient 4 from the collection.

```javascript
db.patients.deleteOne({ patientId: 4 })
```

### Aggregation

> Filters to only Diabetes patients (`$match`), then groups them by doctor and counts how many each doctor has (`$sum: 1`), then sorts by highest count first.

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

> Switches to `LibraryDB` and creates an empty `books` collection.

```javascript
use LibraryDB

db.createCollection("books")
```

### Insert

> Inserts 5 book documents with fields including ISBN, title, author, category, price, and availability status.

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

> Returns all books in the collection.

```javascript
db.books.find()
```

> Returns only books where `availability` is `true`.

```javascript
db.books.find({ availability: true })
```

> Updates the price of the book with ISBN001 to 850.

```javascript
db.books.updateOne(
  { ISBN: "ISBN001" },
  { $set: { price: 850 } }
)
```

> Deletes the book with ISBN004 from the collection.

```javascript
db.books.deleteOne({ ISBN: "ISBN004" })
```

### Aggregation

> Filters to only available books, shows only title/author/price (hides `_id`), sorts by highest price first, and returns the top 5.

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

> Switches to `BankDB` and creates an empty `accounts` collection.

```javascript
use BankDB

db.createCollection("accounts")
```

### Insert

> Inserts 4 bank account documents, each with account number, customer name, account type, balance, and branch.

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

> Updates the balance of account 1001 to 55000.

```javascript
db.accounts.updateOne(
  { accountNo: 1001 },
  { $set: { balance: 55000 } }
)
```

### Delete

> Removes account 1004 from the collection.

```javascript
db.accounts.deleteOne({ accountNo: 1004 })
```

### Aggregation

> Groups accounts by branch, calculates the average balance per branch using `$avg`, sorts branches by highest average balance first, and limits results to the top 5.

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

> Switches to `ShopDB` and creates an empty `products` collection.

```javascript
use ShopDB

db.createCollection("products")
```

### Insert

> Inserts 3 product documents with productId, name, category, brand, price, and stock quantity.

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

> Returns all products in the collection.

```javascript
db.products.find()
```

> Returns only products that belong to the "Electronics" category.

```javascript
db.products.find({ category: "Electronics" })
```

> Updates the stock of product 1 to 15 units.

```javascript
db.products.updateOne(
  { productId: 1 },
  { $set: { stock: 15 } }
)
```

> Deletes product 3 from the collection.

```javascript
db.products.deleteOne({ productId: 3 })
```

### Aggregation

> Filters to "Electronics" category, shows only name/brand/price (no `_id`), sorts by highest price first, and returns the top 10 products.

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

> Switches to `EmployeeDB` and creates an empty `employees` collection.

```javascript
use EmployeeDB

db.createCollection("employees")
```

### Insert

> Inserts 4 employee documents with employeeId, name, department, designation, salary, and years of experience.

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

> Returns all employee documents.

```javascript
db.employees.find()
```

> Returns only employees who work in the "IT" department.

```javascript
db.employees.find({ department: "IT" })
```

> Updates employee 1's salary to 52000.

```javascript
db.employees.updateOne(
  { employeeId: 1 },
  { $set: { salary: 52000 } }
)
```

> Removes employee 4 from the collection.

```javascript
db.employees.deleteOne({ employeeId: 4 })
```

### Aggregation

> Groups employees by department, calculates average salary (`$avg`) and total headcount (`$sum: 1`) per department, then sorts by highest average salary first.

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

> Switches to `MovieDB` and creates an empty `movies` collection.

```javascript
use MovieDB

db.createCollection("movies")
```

### Insert

> Inserts 3 movie documents, each with movieName, director, genre, release year, rating, and an actors array.

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

> Returns all movies in the collection.

```javascript
db.movies.find()
```

> Returns only movies where the `genre` is "Action".

```javascript
db.movies.find({ genre: "Action" })
```

> Updates the rating of "Movie A" to 8.8.

```javascript
db.movies.updateOne(
  { movieName: "Movie A" },
  { $set: { rating: 8.8 } }
)
```

> Deletes "Movie C" from the collection.

```javascript
db.movies.deleteOne({ movieName: "Movie C" })
```

### Aggregation

> Filters to only movies released after 2020 (`$gt: 2020`), sorts by highest rating first, and returns the top 5.

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

> Switches to `TravelDB` and creates an empty `tourists` collection.

```javascript
use TravelDB

db.createCollection("tourists")
```

### Insert

> Inserts 3 tourist documents with touristId, name, destination, age, country, and package cost.

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

> Returns all tourist documents.

```javascript
db.tourists.find()
```

> Returns only tourists whose destination is "Goa".

```javascript
db.tourists.find({ destination: "Goa" })
```

> Updates tourist 1's package cost to 27000.

```javascript
db.tourists.updateOne(
  { touristId: 1 },
  { $set: { packageCost: 27000 } }
)
```

> Removes tourist 3 from the collection.

```javascript
db.tourists.deleteOne({ touristId: 3 })
```

### Aggregation

> Groups tourists by destination, calculates the average package cost per destination using `$avg`, and sorts by highest average cost first.

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

> Switches to `HotelDB` and creates an empty `bookings` collection.

```javascript
use HotelDB

db.createCollection("bookings")
```

### Insert

> Inserts 3 booking documents with bookingId, customer name, hotel name, room type, number of nights, and total amount paid.

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

> Returns all bookings in the collection.

```javascript
db.bookings.find()
```

> Returns only bookings made at "Hotel A".

```javascript
db.bookings.find({ hotel: "Hotel A" })
```

> Updates the number of nights for booking 1 to 4.

```javascript
db.bookings.updateOne(
  { bookingId: 1 },
  { $set: { nights: 4 } }
)
```

> Deletes booking 3 from the collection.

```javascript
db.bookings.deleteOne({ bookingId: 3 })
```

### Aggregation

> Groups bookings by hotel and sums up all the `amount` values to get each hotel's total revenue (`$sum: "$amount"`), then sorts by highest revenue first and shows only the top 5 hotels.

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

> Switches to `EcommerceDB` and creates an empty `orders` collection.

```javascript
use EcommerceDB

db.createCollection("orders")
```

### Insert

> Inserts 3 order documents with orderId, customer name, product, category, quantity, price, and order date.

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

> Returns all orders in the collection.

```javascript
db.orders.find()
```

> Returns only orders in the "Electronics" category.

```javascript
db.orders.find({ category: "Electronics" })
```

> Updates the quantity of order 1 to 3.

```javascript
db.orders.updateOne(
  { orderId: 1 },
  { $set: { quantity: 3 } }
)
```

> Deletes order 3 from the collection.

```javascript
db.orders.deleteOne({ orderId: 3 })
```

### Aggregation

> First uses `$project` with `$multiply` to compute a new `orderValue` field (quantity × price) for each order, then groups by category and calculates the average `orderValue` per category.

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

> `$multiply` takes an array of two field references and returns their product — used inside `$project` to create a computed field.

```javascript
$multiply: ["$quantity", "$price"]
```

---

# 11. SportsDB — Players

The question asks to group players by team, calculate average performance score, sort teams, and show the top 3. 

> Switches to `SportsDB` and creates an empty `players` collection.

```javascript
use SportsDB

db.createCollection("players")
```

### Insert

> Inserts 3 player documents with playerName, team, sport, age, matches played, runs/goals scored, and country.

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

> Returns all players in the collection.

```javascript
db.players.find()
```

> Returns only players who belong to "Team A".

```javascript
db.players.find({ team: "Team A" })
```

> Updates Arun's runsGoals to 2700.

```javascript
db.players.updateOne(
  { playerName: "Arun" },
  { $set: { runsGoals: 2700 } }
)
```

> Removes John's document from the collection.

```javascript
db.players.deleteOne({ playerName: "John" })
```

### Aggregation

Here, since the question calls it a **performance score** but doesn't give a formula, the simplest interpretation is to use `runsGoals` as the performance score.

> Groups players by team, calculates the average `runsGoals` as performance score, sorts teams by highest average first, and returns only the top 3 teams.

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

> Switches to `SchoolDB` and creates an empty `students` collection.

```javascript
use SchoolDB

db.createCollection("students")
```

### Insert

> Inserts 3 student documents where the `courses` field is an **array** — each student is enrolled in multiple courses.

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

> Returns all student documents.

```javascript
db.students.find()
```

> Finds all students whose `courses` array contains "MongoDB" — MongoDB automatically searches inside arrays for a match.

```javascript
db.students.find({
  courses: "MongoDB"
})
```

### Update

> Uses `$push` to add "Java" to the end of student 1's `courses` array without removing existing entries.

```javascript
db.students.updateOne(
  { studentId: 1 },
  { $push: { courses: "Java" } }
)
```

### Delete

> Removes the document for student 3 from the collection.

```javascript
db.students.deleteOne({
  studentId: 3
})
```

### `$unwind`

> Flattens the `courses` array — each course in the array becomes a separate document row, so one student with 3 courses becomes 3 rows.

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

> First `$unwind` flattens the courses array into individual rows, then `$group` groups by course name and counts how many students are in each course using `$sum: 1`.

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

> Switch to (or create) a database by name.

```javascript
use DatabaseName
```

### 2. Collection

> Explicitly create an empty collection inside the current database.

```javascript
db.createCollection("collectionName")
```

### 3. Insert one

> Insert a single document (object) into a collection.

```javascript
db.collection.insertOne({
  field: "value"
})
```

### 4. Insert many

> Insert multiple documents at once by passing an array.

```javascript
db.collection.insertMany([
  { field: "value1" },
  { field: "value2" }
])
```

### 5. Read

> Retrieve all documents from a collection.

```javascript
db.collection.find()
```

### 6. Find with condition

> Retrieve only documents that match a specific field-value filter.

```javascript
db.collection.find({
  field: "value"
})
```

### 7. Update

> Find the first matching document and update a specific field using `$set` — only the listed field changes.

```javascript
db.collection.updateOne(
  { field: "oldValue" },
  { $set: { field: "newValue" } }
)
```

### 8. Delete

> Find and permanently remove the first document that matches the condition.

```javascript
db.collection.deleteOne({
  field: "value"
})
```

---

# Aggregation Cheat Sheet

This is the part I'd memorize most.

### `$match` = WHERE

> Filters documents — only those matching the condition move to the next pipeline stage (like SQL's WHERE clause).

```javascript
{
  $match: {
    disease: "Diabetes"
  }
}
```

### `$group` = GROUP BY

> Groups documents by a field and computes aggregated values (like average, count, sum) for each group.

```javascript
{
  $group: {
    _id: "$department",
    average: { $avg: "$marks" }
  }
}
```

### `$sum` = COUNT / TOTAL

> `$sum: 1` counts the number of documents in a group; `$sum: "$field"` adds up the values of a numeric field.

Count:

```javascript
{ $sum: 1 }
```

Total:

```javascript
{ $sum: "$amount" }
```

### `$avg` = Average

> Calculates the arithmetic mean of a numeric field across all documents in a group.

```javascript
{ $avg: "$salary" }
```

### `$sort`

> Orders the result documents — `-1` means descending (highest first), `1` means ascending (lowest first).

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

> Cuts the output to only the first N documents — use after `$sort` to get "top N" results.

```javascript
{
  $limit: 5
}
```

### `$project`

> Controls which fields appear in the output — `1` means include the field, `0` means exclude it.

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

> Multiplies two or more field values together — used inside `$project` to compute a new calculated field.

```javascript
{
  $multiply: ["$quantity", "$price"]
}
```

### `$unwind`

> Deconstructs an array field so each element becomes its own separate document row — used when you need to process array items individually.

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
