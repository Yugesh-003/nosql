# Spatial Indexing in MongoDB

## Aim

To implement geospatial data storage and perform location-based queries using MongoDB.

## 1. Database Creation

```javascript
use GeoDB
```

**Output**
```text
switched to db GeoDB
```

## 2. Collection Creation

```javascript
db.createCollection("places")
```

**Output**
```javascript
{ ok: 1 }
```

## 3. Insert 5 Records

```javascript
db.places.insertMany([
  {
    name: "Central Park",
    category: "Park",
    location: {
      type: "Point",
      coordinates: [-73.9654, 40.7829]
    }
  },
  {
    name: "Times Square",
    category: "Landmark",
    location: {
      type: "Point",
      coordinates: [-73.9855, 40.7580]
    }
  },
  {
    name: "Brooklyn Bridge",
    category: "Bridge",
    location: {
      type: "Point",
      coordinates: [-73.9969, 40.7061]
    }
  },
  {
    name: "Empire State Building",
    category: "Building",
    location: {
      type: "Point",
      coordinates: [-73.9857, 40.7484]
    }
  },
  {
    name: "Statue of Liberty",
    category: "Monument",
    location: {
      type: "Point",
      coordinates: [-74.0445, 40.6892]
    }
  }
])
```

**Output**
```text
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('6acc593d44cc774a3656e31c'),
    '1': ObjectId('6acc593d44cc774a3656e31d'),
    '2': ObjectId('6acc593d44cc774a3656e31e'),
    '3': ObjectId('6acc593d44cc774a3656e31f'),
    '4': ObjectId('6acc593d44cc774a3656e320')
  }
}
```

*Note: ObjectIds shown above are transcribed from the source document; MongoDB will generate different IDs when the records are inserted again.*

## 4. Create a Geospatial Index

```javascript
db.places.createIndex({ location: "2dsphere" })
```

**Output**
```text
location_2dsphere
```

## 5. Location-Based Queries

### Query 1: Display All Records

```javascript
db.places.find()
```

**Output**

The query returns all five documents in the `places` collection:

```javascript
{
  name: "Central Park",
  category: "Park",
  location: {
    type: "Point",
    coordinates: [-73.9654, 40.7829]
  }
}
{
  name: "Times Square",
  category: "Landmark",
  location: {
    type: "Point",
    coordinates: [-73.9855, 40.7580]
  }
}
{
  name: "Brooklyn Bridge",
  category: "Bridge",
  location: {
    type: "Point",
    coordinates: [-73.9969, 40.7061]
  }
}
{
  name: "Empire State Building",
  category: "Building",
  location: {
    type: "Point",
    coordinates: [-73.9857, 40.7484]
  }
}
{
  name: "Statue of Liberty",
  category: "Monument",
  location: {
    type: "Point",
    coordinates: [-74.0445, 40.6892]
  }
}
```

### Query 2: Find Places Near Times Square

```javascript
db.places.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [-73.9855, 40.7580]
      }
    }
  }
})
```

**Output**

The query returns places ordered by distance from Times Square, nearest first. The source output visibly includes:

```javascript
{
  name: "Times Square",
  category: "Landmark",
  location: {
    type: "Point",
    coordinates: [-73.9855, 40.758]
  }
}
{
  name: "Empire State Building",
  category: "Building",
  location: {
    type: "Point",
    coordinates: [-73.9857, 40.7484]
  }
}
{
  name: "Central Park",
  category: "Park",
  location: {
    type: "Point",
    coordinates: [-73.9654, 40.7829]
  }
}
```

### Query 3: Find Places Within 5 km of Times Square

```javascript
db.places.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [-73.9855, 40.7580]
      },
      $maxDistance: 5000
    }
  }
})
```

**Output**

The query returns places within 5,000 metres of Times Square, ordered by distance. The source output shows these matching documents:

```javascript
{
  name: "Times Square",
  category: "Landmark",
  location: {
    type: "Point",
    coordinates: [-73.9855, 40.758]
  }
}
{
  name: "Empire State Building",
  category: "Building",
  location: {
    type: "Point",
    coordinates: [-73.9857, 40.7484]
  }
}
{
  name: "Central Park",
  category: "Park",
  location: {
    type: "Point",
    coordinates: [-73.9654, 40.7829]
  }
}
```

### Query 4: Find Places Within 3 km of Central Park

```javascript
db.places.find({
  location: {
    $geoWithin: {
      $centerSphere: [
        [-73.9654, 40.7829],
        3 / 6378.1
      ]
    }
  }
})
```

**Output**
```javascript
{
  name: "Central Park",
  category: "Park",
  location: {
    type: "Point",
    coordinates: [-73.9654, 40.7829]
  }
}
```

### Query 5: Find the Nearest Place to Brooklyn Bridge Within 10 km

```javascript
db.places.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [-73.9969, 40.7061]
      },
      $maxDistance: 10000
    }
  }
}).limit(1)
```

**Output**
```javascript
{
  name: "Brooklyn Bridge",
  category: "Bridge",
  location: {
    type: "Point",
    coordinates: [-73.9969, 40.7061]
  }
}
```

### Query 6: Find Places Within a Geographical Polygon

```javascript
db.places.find({
  location: {
    $geoWithin: {
      $geometry: {
        type: "Polygon",
        coordinates: [[
          [-74.05, 40.68],
          [-73.95, 40.68],
          [-73.95, 40.80],
          [-74.05, 40.80],
          [-74.05, 40.68]
        ]]
      }
    }
  }
})
```

**Output**

The source output shows the five inserted places within the specified polygon:

```javascript
{
  name: "Statue of Liberty",
  category: "Monument",
  location: {
    type: "Point",
    coordinates: [-74.0445, 40.6892]
  }
}
{
  name: "Times Square",
  category: "Landmark",
  location: {
    type: "Point",
    coordinates: [-73.9855, 40.758]
  }
}
{
  name: "Central Park",
  category: "Park",
  location: {
    type: "Point",
    coordinates: [-73.9654, 40.7829]
  }
}
{
  name: "Empire State Building",
  category: "Building",
  location: {
    type: "Point",
    coordinates: [-73.9857, 40.7484]
  }
}
{
  name: "Brooklyn Bridge",
  category: "Bridge",
  location: {
    type: "Point",
    coordinates: [-73.9969, 40.7061]
  }
}
```

## Result

Thus, a MongoDB database and collection were created, five geospatial records were inserted, and location-based queries were performed using geospatial operators.
