const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.get('/run', (req, res) => {
  const cmd = req.query.cmd;
  exec(cmd, (error, stdout, stderr) => {
    if (error) {
      res.send(`Error: ${error.message}`);
      return;
    }
    if (stderr) {
      res.send(`stderr: ${stderr}`);
      return;
    }
    res.send(`stdout: ${stdout}`);
  });
});

app.get('/greet', (req, res) => {
  const name = req.query.name;
  res.send(`<h1>Hello, ${name}!</h1>`);
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});