const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');

app.set('view engine', 'ejs');
app.use(cookieParser());

app.get('/', (req, res) => {
  // DESTRUCTURING ASSIGNMENT TO RETRIEVE COOKIE
  let { expressLoginCookie } = req.cookies;

  // VALIDATE COOKIE (one-line conditional)
  expressLoginCookie = (expressLoginCookie === 'true') ? 'true' : 'false';
    
  // Compute a date 7 days from now (in ms) for cookie expiration
  const expirationDate = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000); 

  const cookieName = 'expressLoginCookie';
  let cookieValue = expressLoginCookie;

  // SET THE COOKIE
  res.cookie(cookieName, cookieValue, {
    expires: expirationDate,
  });

  if (expressLoginCookie === 'true') {
    res.render('logged_in_true');
  } else {
    res.render('logged_in_false');
  }
});

app.get('/login', (req, res) => {
  // Set the login cookie to 'true'
  res.cookie('expressLoginCookie', 'true', {
    expires: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // 7 days expiration
  });
  res.redirect('/');
});

app.get('/logout', (req, res) => {
  // Set the login cookie to 'false'
  res.cookie('expressLoginCookie', 'false', {
    expires: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000), // 7 days expiration
  });
  res.redirect('/');
});

var listener = app.listen(
  process.env.PORT || 8080,
  process.env.HOST || "0.0.0.0",
  function() {
    console.log("Express server started on http://127.0.0.1:8080");
});
