const express = require("express");

const app = express();

app.get("/smoke-greet", (req, res) => {
  const name = req.query.name || "guest";
  res.send(`<html><body><h1>Hello ${name}</h1></body></html>`);
});

module.exports = app;
