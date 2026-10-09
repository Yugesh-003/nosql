# Program 9 – Books and Products Collection

## PART A – BOOKS

## Use DataBase
```
use bookDB
```

## Sample Data
```
db.books.insertMany([
{
  bookId: 101,
  title: "MongoDB Basics",
  author: "John Smith",
  category: "Database",
  isbn: "978100001",
  price: 450,
  stock: 25,
  publisher: "Tech Press",
  year: 2023
},
{
  bookId: 102,
  title: "Learning Python",
  author: "Mark Lutz",
  category: "Programming",
  isbn: "978100002",
  price: 850,
  stock: 15,
  publisher: "O'Reilly",
  year: 2022
},
{
  bookId: 103,
  title: "Java Fundamentals",
  author: "James Gosling",
  category: "Programming",
  isbn: "978100003",
  price: 650,
  stock: 30,
  publisher: "Oracle Press",
  year: 2021
},
{
  bookId: 104,
  title: "Data Science Handbook",
  author: "Jake VanderPlas",
  category: "Data Science",
  isbn: "978100004",
  price: 900,
  stock: 12,
  publisher: "O'Reilly",
  year: 2023
},
{
  bookId: 105,
  title: "Machine Learning Essentials",
  author: "Andrew Ng",
  category: "AI",
  isbn: "978100005",
  price: 1200,
  stock: 10,
  publisher: "AI Publications",
  year: 2024
},
{
  bookId: 106,
  title: "SQL Complete Guide",
  author: "Chris Fehily",
  category: "Database",
  isbn: "978100006",
  price: 550,
  stock: 18,
  publisher: "McGraw Hill",
  year: 2020
},
{
  bookId: 107,
  title: "Node.js in Action",
  author: "Mike Cantelon",
  category: "Programming",
  isbn: "978100007",
  price: 700,
  stock: 22,
  publisher: "Manning",
  year: 2023
},
{
  bookId: 108,
  title: "Deep Learning",
  author: "Ian Goodfellow",
  category: "AI",
  isbn: "978100008",
  price: 1500,
  stock: 8,
  publisher: "MIT Press",
  year: 2024
},
{
  bookId: 109,
  title: "MongoDB Advanced",
  author: "John Smith",
  category: "Database",
  isbn: "978100009",
  price: 750,
  stock: 20,
  publisher: "Tech Press",
  year: 2024
},
{
  bookId: 110,
  title: "Python for Data Analysis",
  author: "Wes McKinney",
  category: "Data Science",
  isbn: "978100010",
  price: 950,
  stock: 14,
  publisher: "O'Reilly",
  year: 2023
}
])
```
---

## 1. Find all the books

### Query
```javascript
db.books.find({},{title:1,_id:0})
```

### Output
```text
[
  { title: 'MongoDB Basics' },
  { title: 'Learning Python' },
  { title: 'Java Fundamentals' },
  { title: 'Data Science Handbook' },
  { title: 'Machine Learning Essentials' },
  { title: 'SQL Complete Guide' },
  { title: 'Node.js in Action' },
  { title: 'Deep Learning' },
  { title: 'MongoDB Advanced' },
  { title: 'Python for Data Analysis' }
]
```

---

## 2. Find books written by John Smith

### Query
```javascript
db.books.find({author: "John Smith"})
```

### Output
```text
{
    bookId: 101,
    title: 'MongoDB Basics',
    author: 'John Smith',
    category: 'Database',
    isbn: '978100001',
    price: 450,
    stock: 25,
    publisher: 'Tech Press',
    year: 2023
}
{
    bookId: 109,
    title: 'MongoDB Advanced',
    author: 'John Smith',
    category: 'Database',
    isbn: '978100009',
    price: 750,
    stock: 20,
    publisher: 'Tech Press',
    year: 2024
}
```

---

## 3. Find books published by Tech Press

### Query
```javascript
db.books.find({publisher: "Tech Press"})
```

### Output
```text
{
  _id: ObjectId('6ac8bfedcede986bf82e6e74'),
  bookId: 101,
  title: 'MongoDB Basics',
  author: 'John Smith',
  category: 'Database',
  isbn: '978100001',
  price: 450,
  stock: 25,
  publisher: 'Tech Press',
  year: 2023
}
{
  _id: ObjectId('6ac8bfedcede986bf82e6e74'),
  bookId: 101,
  title: 'MongoDB Basics',
  author: 'John Smith',
  category: 'Database',
  isbn: '978100001',
  price: 450,
  stock: 25,
  publisher: 'Tech Press',
  year: 2023
}
```

---

## 4. Display books published after 2022

### Query
```javascript
db.books.find({year: {$gt: 2022}}, {title: 1, year: 1, _id: 0})
```

### Output
```text
{
    bookId: 101,
    title: 'MongoDB Basics',
    year: 2023
}
{
    bookId: 104,
    title: 'Data Science Handbook',
    year: 2023
}
{
    bookId: 105,
    title: 'Machine Learning Essentials',
    year: 2024
}
{
    bookId: 107,
    title: 'Node.js in Action',
    year: 2023
}
{
    bookId: 108,
    title: 'Deep Learning',
    year: 2024
}
{
    bookId: 109,
    title: 'MongoDB Advanced',
    year: 2024
}
{
    bookId: 110,
    title: 'Python for Data Analysis',
    year: 2023
}
```

---

## 5. Compare document retrieval before and after creating an index

### Before creating the index

```javascript
db.books.find({category: "Database"}).explain("executionStats")
```

### Output (document count only)

```text
.
.
.
totalDocsExamined: 10
.
.
.
```

### Create an index on category

```javascript
db.books.createIndex({category: 1})
```

### Output

```text
category_1
```

### After creating the index

```javascript
db.books.find({category: "Database"}).explain("executionStats")
```

### Output (document count only)

```text
.
.
.
totalDocsExamined: 3
.
.
.
```

---

## 6. Drop the title index

### Query
```javascript
db.books.createIndex({title: 1})
```

### Output
```text
title_1
```

Then:

```javascript
db.books.dropIndex("title_1")
```

### Output
```text
{ nIndexesWas: 3, ok: 1 }
```


> The `nIndexesWas` value may differ depending on existing indexes.

---

## 7. Create a text index on author and search for "James Gosling"

### Query
```javascript
db.books.createIndex({author: "text"})
```

### Output
```text
author_text
```

### Search Query
```javascript
db.books.find(
    {$text: {$search: "James Gosling"}},
    {_id: 0, title: 1, author: 1}
)
```

### Output
```text
{
    bookId: 103,
    title: 'Java Fundamentals',
    author: 'James Gosling',
    category: 'Programming',
    isbn: '978100003',
    price: 650,
    stock: 30,
    publisher: 'Oracle Press',
    year: 2021
}
```

---

## 8. Create a Compound index on author and year

### Before creating the index

```javascript
db.books.find({author: "John Smith"}).explain("executionStats")
```

### Output (document count only)

```text
.
.
.
totalDocsExamined: 10
.
.
```

### Create an index on category

```javascript
db.books.createIndex({
    author: 1,
    year: 1
})
```

### Output

```text
author_1_year_1
```

### After creating the index

```javascript
db.books.find({author: "John Smith"}).explain("executionStats")
```

### Output (document count only)

```text
.
.
.
totalDocsExamined: 2
.
.
```

---
