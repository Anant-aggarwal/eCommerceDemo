import express from 'express';
import cors from 'cors';
import sqlite3 from 'sqlite3';
import { open } from 'sqlite';

const app = express();
const PORT = 3000;

// Enable CORS for all origins (adjust if needed)
app.use(cors());
app.use(express.json());

// Open SQLite DB connection
const dbPromise = open({
  filename: './ecommerce.db',
  driver: sqlite3.Database
});

// Routes
app.get('/api/products', async (req, res) => {
  try {
    const db = await dbPromise;
    const products = await db.all('SELECT * FROM products LIMIT 100'); // Add pagination if needed
    res.json({ success: true, data: products });
  } catch (err) {
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

app.get('/api/products/:id', async (req, res) => {
  try {
    const db = await dbPromise;
    const product = await db.get('SELECT * FROM products WHERE id = ?', req.params.id);
    if (product) {
      res.json({ success: true, data: product });
    } else {
      res.status(404).json({ success: false, error: 'Product not found' });
    }
  } catch (err) {
    res.status(500).json({ success: false, error: 'Internal server error' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
app.use(cors());