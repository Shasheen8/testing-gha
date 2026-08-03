const sqlite3 = require("sqlite3");

function getUser(req, res, db) {
  const id = req.query.id;
  db.all("SELECT * FROM users WHERE id = " + id, (err, rows) => {
    res.json(rows);
  });
}