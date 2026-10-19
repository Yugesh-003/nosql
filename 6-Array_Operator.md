# MongoDB Array Operators – 15 Exercises

## Initial Data

```javascript
use("studentDB")

db.students.insertMany([
    {
        studentId: "S0501",
        name: "Arun",
        skills: ["Python", "Java", "SQL", "MongoDB"]
    },
    {
        studentId: "S0502",
        name: "Bala",
        skills: ["Python", "SQL"]
    },
    {
        studentId: "S0503",
        name: "Cathy",
        skills: ["Java", "MongoDB"]
    }
])
```

> **Note:** Exercises 6–15 below show the result when each exercise is run independently from the original S0501 data. If you run them continuously, the data will change after each update.

---

## 1. `$in`

### Query

```javascript
db.students.find({
    skills: {$in: ["Python", "Java"]}
})
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB'
    ]
}
{
    _id: ObjectId('6abb51d533bfa556717d1b84'),
    studentId: 'S0502',
    name: 'Bala',
    skills: [
        'Python',
        'SQL'
    ]
}
{
    _id: ObjectId('6abb51d533bfa556717d1b85'),
    studentId: 'S0503',
    name: 'Cathy',
    skills: [
        'Java',
        'MongoDB'
    ]
}
```

---

## 2. `$nin`

### Query

```javascript
db.students.find({
    skills: {$nin: ["Java"]}
})
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b84'),
    studentId: 'S0502',
    name: 'Bala',
    skills: [
        'Python',
        'SQL'
    ]
}
```

---

## 3. `$all`

### Query

```javascript
db.students.find({
    skills: {$all: ["Java", "SQL", "MongoDB"]}
})
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB'
    ]
}
```

---

## 4. `$size`

### Query

```javascript
db.students.find({
    skills: {$size: 2}
})
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b84'),
    studentId: 'S0502',
    name: 'Bala',
    skills: [
        'Python',
        'SQL'
    ]
}
{
    _id: ObjectId('6abb51d533bfa556717d1b85'),
    studentId: 'S0503',
    name: 'Cathy',
    skills: [
        'Java',
        'MongoDB'
    ]
}
```

---

## 5. `$elemMatch`

### Query

```javascript
db.students.find({
    skills: {$elemMatch: {$in: ["Python", "SQL"]}}
})
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB'
    ]
}
{
    _id: ObjectId('6abb51d533bfa556717d1b84'),
    studentId: 'S0502',
    name: 'Bala',
    skills: [
        'Python',
        'SQL'
    ]
}
```

---

# Update Operations

## 6. `$push`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {$push: {skills: "JavaScript"}}
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB',
        'JavaScript'
    ]
}
```

---

## 7. `$addToSet`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {$addToSet: {skills: "Python"}}
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB'
    ]
}
```

---

## 8. `$pop` – Remove Last Element

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {$pop: {skills: 1}}
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL'
    ]
}
```

---

## 9. `$pop` – Remove First Element

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {$pop: {skills: -1}}
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Java',
        'SQL',
        'MongoDB'
    ]
}
```

---

## 10. `$pull`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {$pull: {skills: "SQL"}}
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'MongoDB'
    ]
}
```

---

## 11. `$pullAll`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {$pullAll: {skills: ["Java", "SQL"]}}
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'MongoDB'
    ]
}
```

---

## 12. `$push + $each`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {
        $push: {
            skills: {
                $each: ["Python", "Java", "SQL"]
            }
        }
    }
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB',
        'Python',
        'Java',
        'SQL'
    ]
}
```

---

## 13. `$addToSet + $each`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {
        $addToSet: {
            skills: {
                $each: ["Python", "MongoDB", "SQL"]
            }
        }
    }
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB'
    ]
}
```

---

## 14. `$push + $slice`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {
        $push: {
            skills: {
                $each: ["React", "Node.js"],
                $slice: 5
            }
        }
    }
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Java',
        'SQL',
        'MongoDB',
        'React'
    ]
}
```

---

## 15. `$push + $position`

### Query

```javascript
db.students.updateOne(
    {studentId: "S0501"},
    {
        $push: {
            skills: {
                $each: ["Python"],
                $position: 0
            }
        }
    }
)
```

### Output

```text
{
    _id: ObjectId('6abb51d533bfa556717d1b83'),
    studentId: 'S0501',
    name: 'Arun',
    skills: [
        'Python',
        'Python',
        'Java',
        'SQL',
        'MongoDB'
    ]
}
```
