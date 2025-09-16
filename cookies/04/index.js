const express = require('express');
const cookieParser = require('cookie-parser');
const path = require('path');

const app = express();

// Use cookie-parser middleware
app.use(cookieParser());

// Set the view engine to ejs
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
  const cookieName = 'page_visits';
  let visits = 0;

  if (req.cookies[cookieName]) {
    visits = parseInt(req.cookies[cookieName]);
  }
  visits += 1;

  res.cookie(cookieName, visits, { httpOnly: true });
  res.render('cookie_02', { cookie_value: visits });
});

const listener = app.listen(process.env.PORT || 8080, process.env.HOST || '0.0.0.0', () => {
    console.log('Express server started');
  });