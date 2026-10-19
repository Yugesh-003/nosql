# PART B – PRODUCTS

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

## 1. Create single field index for category

### Before creating the index

```javascript
db.products.find({ category: "Electronics" }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'COLLSCAN'
nReturned: 2
totalDocsExamined: 5
totalKeysExamined: 0
```

### Query

```javascript
db.products.createIndex({ category: 1 })
```

### Output

```text
category_1
```

### After creating the index

```javascript
db.products.find({ category: "Electronics" }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'IXSCAN'
nReturned: 2
totalDocsExamined: 2
totalKeysExamined: 2
```

> Before indexing, MongoDB scans all 5 documents (COLLSCAN). After creating the index on `category`, it scans only the 2 matching documents (IXSCAN), making the query more efficient.

---

## 2. Create a unique index for productid

### Before creating the index

```javascript
db.products.find({ productid: "P101" }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'COLLSCAN'
nReturned: 1
totalDocsExamined: 5
totalKeysExamined: 0
```

### Query

```javascript
db.products.createIndex(
    { productid: 1 },
    { unique: true }
)
```

### Output

```text
productid_1
```

### After creating the index

```javascript
db.products.find({ productid: "P101" }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'IXSCAN'
nReturned: 1
totalDocsExamined: 1
totalKeysExamined: 1
```

> The unique index ensures no two documents share the same `productid`. It also speeds up lookups — MongoDB scans all 5 documents before indexing, but only 1 after.

---

## 3. Find the product above 10000

### Query

```javascript
db.products.find({ price: { $gt: 10000 } }, { _id: 0 })
```

### Output

```text
{ productid: 'P101', name: 'Laptop', category: 'Electronics', price: 55000 }
{ productid: 'P102', name: 'Mobile Phone', category: 'Electronics', price: 25000 }
{ productid: 'P104', name: 'Refrigerator', category: 'Appliances', price: 45000 }
```

---

## 4. Create a compound index for category (ascending) and price (descending)

### Before creating the index

```javascript
db.products.find({ category: "Furniture", price: { $lt: 10000 } }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'COLLSCAN'
nReturned: 2
totalDocsExamined: 5
totalKeysExamined: 0
```

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

### After creating the index

```javascript
db.products.find({ category: "Furniture", price: { $lt: 10000 } }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'IXSCAN'
nReturned: 2
totalDocsExamined: 2
totalKeysExamined: 2
```

> The compound index covers queries that filter on both `category` and `price`. MongoDB goes from scanning all 5 documents to scanning only the 2 matching ones.

---

## 5. Create a text index for name

### Before creating the index

```javascript
db.products.find({ name: "Laptop" }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'COLLSCAN'
nReturned: 1
totalDocsExamined: 5
totalKeysExamined: 0
```

### Query

```javascript
db.products.createIndex({ name: "text" })
```

### Output

```text
name_text
```

### After creating the index

```javascript
db.products.find({ $text: { $search: "Laptop" } }).explain("executionStats")
```

### Output (important fields)

```text
stage: 'TEXT'
nReturned: 1
totalDocsExamined: 1
totalKeysExamined: 1
```

> Before the text index, MongoDB does a full collection scan to match names. After creating the text index, it uses the `TEXT` stage to locate the document directly, examining only 1 document instead of 5.

---

## 6. Find the product above 10000

### Query

```javascript
db.products.find({ price: { $gt: 10000 } }, { _id: 0 })
```

### Output

```text
{ productid: 'P101', name: 'Laptop', category: 'Electronics', price: 55000 }
{ productid: 'P102', name: 'Mobile Phone', category: 'Electronics', price: 25000 }
{ productid: 'P104', name: 'Refrigerator', category: 'Appliances', price: 45000 }
```
