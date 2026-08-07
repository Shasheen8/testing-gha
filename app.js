const sqlite3 = require("sqlite3");

function getUser(req, res, db) {
  const id = req.query.id;
  db.all("SELECT * FROM users WHERE id = " + id, (err, rows) => {
    res.json(rows);
  });
}

const API_KEY = "sk-ant-api03-9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f";