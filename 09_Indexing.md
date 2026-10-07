# Program 9 – Books and Products Collection

## PART A – BOOKS

## Sample Data
Use the 10 book documents provided in the exercise post.

---

## 1. Find all the books

### Query
```javascript
db.books.find()
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
    bookId: 102,
    title: 'Learning Python',
    author: 'Mark Lutz',
    category: 'Programming',
    isbn: '978100002',
    price: 850,
    stock: 15,
    publisher: "O'Reilly",
    year: 2022
}
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
{
    bookId: 104,
    title: 'Data Science Handbook',
    author: 'Jake VanderPlas',
    category: 'Data Science',
    isbn: '978100004',
    price: 900,
    stock: 12,
    publisher: "O'Reilly",
    year: 2023
}
{
    bookId: 105,
    title: 'Machine Learning Essentials',
    author: 'Andrew Ng',
    category: 'AI',
    isbn: '978100005',
    price: 1200,
    stock: 10,
    publisher: 'AI Publications',
    year: 2024
}
{
    bookId: 106,
    title: 'SQL Complete Guide',
    author: 'Chris Fehily',
    category: 'Database',
    isbn: '978100006',
    price: 550,
    stock: 18,
    publisher: 'McGraw Hill',
    year: 2020
}
{
    bookId: 107,
    title: 'Node.js in Action',
    author: 'Mike Cantelon',
    category: 'Programming',
    isbn: '978100007',
    price: 700,
    stock: 22,
    publisher: 'Manning',
    year: 2023
}
{
    bookId: 108,
    title: 'Deep Learning',
    author: 'Ian Goodfellow',
    category: 'AI',
    isbn: '978100008',
    price: 1500,
    stock: 8,
    publisher: 'MIT Press',
    year: 2024
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
{
    bookId: 110,
    title: 'Python for Data Analysis',
    author: 'Wes McKinney',
    category: 'Data Science',
    isbn: '978100010',
    price: 950,
    stock: 14,
    publisher: "O'Reilly",
    year: 2023
}
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

## 4. Display books published after 2022

### Query
```javascript
db.books.find({year: {$gt: 2022}})
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

## 5. Create index on category

### Query
```javascript
db.books.createIndex({category: 1})
```

### Output
```text
category_1
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
db.books.find({
    $text: {$search: "James Gosling"}
})
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

### Query
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

---

# PART B – PRODUCTS

> The exercise post does not contain product sample data. The following small sample is provided so the product exercises can be executed.

## Sample Product Data

```javascript
db.products.insertMany([
    {
        productid: "P101",
        name: "Laptop",
        category: "Electronics",
        price: 55000
    },
    {
        productid: "P102",
        name: "Mobile Phone",
        category: "Electronics",
        price: 25000
    },
    {
        productid: "P103",
        name: "Office Chair",
        category: "Furniture",
        price: 8500
    },
    {
        productid: "P104",
        name: "Refrigerator",
        category: "Appliances",
        price: 45000
    },
    {
        productid: "P105",
        name: "Study Table",
        category: "Furniture",
        price: 7000
    }
])
```

---

## 9. Create single field index for category

### Query
```javascript
db.products.createIndex({category: 1})
```

### Output
```text
category_1
```

---

## 10. Create a unique index for productid

### Query
```javascript
db.products.createIndex(
    {productid: 1},
    {unique: true}
)
```

### Output
```text
productid_1
```

---

## 11. Find the product above 10000

### Query
```javascript
db.products.find({price: {$gt: 10000}})
```

### Output
```text
{
    productid: 'P101',
    name: 'Laptop',
    category: 'Electronics',
    price: 55000
}
{
    productid: 'P102',
    name: 'Mobile Phone',
    category: 'Electronics',
    price: 25000
}
{
    productid: 'P104',
    name: 'Refrigerator',
    category: 'Appliances',
    price: 45000
}
```

---

## 12. Create a compound index on category ascending and price descending

### Query
```javascript
db.products.createIndex({
    category: 1,
    price: -1
})
```

### Output
```text
category_1_price_-1
```

---

## 13. Create a text index for name

### Query
```javascript
db.products.createIndex({
    name: "text"
})
```

### Output
```text
name_text
```

---

## 14. Find the product above 10000

### Query
```javascript
db.products.find({price: {$gt: 10000}})
```

### Output
```text
{
    productid: 'P101',
    name: 'Laptop',
    category: 'Electronics',
    price: 55000
}
{
    productid: 'P102',
    name: 'Mobile Phone',
    category: 'Electronics',
    price: 25000
}
{
    productid: 'P104',
    name: 'Refrigerator',
    category: 'Appliances',
    price: 45000
}
```
