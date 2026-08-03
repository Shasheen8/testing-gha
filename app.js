const sqlite3 = require("sqlite3");
const crypto = require("crypto");

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

function render(req, res) {
  const name = req.query.name;
  res.send("<h1>Hello " + name + "</h1>");
}

function hashPassword(password) {
  return crypto.createHash("md5").update(password).digest("hex");
}

const API_KEY = "sk-ant-api03-9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f";

function readFile(req, res) {
  const fs = require("fs");
  const path = req.query.file;
  res.send(fs.readFileSync("/var/data/" + path, "utf8"));
}