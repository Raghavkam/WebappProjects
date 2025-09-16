const sqlite3 = require('sqlite3').verbose();
const express = require('express');
const bodyParser = require('body-parser')
const path = require('path');


const app = express();



app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const db = new sqlite3.Database('database.db');
const db2 = new sqlite3.Database('responses.db');

app.set('view engine','ejs')

app.get('/', (req, res) => {
  res.render("login");
});

app.get('/failed', (req, res) => {
    res.render("failed");
});

app.get('/home', (req, res) => {
	const username = req.query.username;
	console.log(username)
    res.render("home", { username });
});

app.get('/submit', (req, res) => {
	const username = req.query.username;
	console.log(username)
    res.render("submit", { username });
});

app.post('/submit', (req, res) => {
	const { username, name, email,message} = req.body;

	const sql = "INSERT INTO resp (c_user, c_email,c_messageg) VALUES (?, ?, ?)";
	db2.run(sql, [username, email, message], function(err) {
	  if (err) {
		console.error(err.message);
		res.status(500).json({ error: "Internal Server Error" });
		return;
	  }
	  res.json({ id: this.lastID, username, email, message });
	});
  });
  

  app.get('/responses', (req, res) => {
	const username = req.query.username;
	console.log(username)
	const sql = "SELECT * FROM resp";
	db2.all(sql, [], (err, rows) => {
	  if (err) {
		console.error(err.message);
		res.status(500).json({ error: "Internal Server Error" });
		return;
	  }
	  res.render('responses', { responses: rows, username: username });
	});
  });
  

app.post('/login', (req, res) => {
	const { username, password } = req.body;
  
	const sql = 'SELECT * FROM logins WHERE c_id = ? AND c_pass = ?';
  
	db.get(sql, [username, password], (err, row) => {
	  if (err) {
		console.error(err.message);
		res.status(500).send("Internal Server Error");
		return;
	  }  
	  if (row) {
		res.render("home", { username })
	  } else {
		res.render("failed");
	  }
	});
  });

app.listen(8080,"0.0.0.0", () => {console.log('server started')})