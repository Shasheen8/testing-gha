const sqlite3 = require("sqlite3");

function getUser(req, res, db) {
  const id = req.query.id;
  db.all("SELECT * FROM users WHERE id = " + id, (err, rows) => {
    res.json(rows);
  });
}

const { exec } = require("child_process");

function ping(req, res) {
  const host = req.query.host;
  exec("ping -c 1 " + host, (err, stdout) => {
    res.send(stdout);
  });
}