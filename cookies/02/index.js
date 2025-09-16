const express = require('express');
const app = express();
const cookieParser = require('cookie-parser')

app.set('view engine', 'ejs')
app.use(cookieParser());


// Route to set a cookie
app.get('/', (req, res) => {

  // DESTRUCTURING ASSIGNMENT TO RETRIEVE COOKIE
  let {myExpressCookie} = req.cookies

  // VALIDATE COOKIE IS NUMERIC (one-line conditional)
  myExpressCookie = isNaN(Number(myExpressCookie)) ? 0 : Number(myExpressCookie)

  // compute a date 7 days from now (in ms) for cookie expiration
  const expirationDate = new Date(Date.now() + 7 * 24 * 60 * 60 * 1000); 

  const cookieName = 'myExpressCookie'
  let cookieValue = myExpressCookie
  
  // SET THE COOKIE
  res.cookie(cookieName, cookieValue, {
      expires: expirationDate,
  });

  const render_dictionary = {
    cookie_value : cookieValue 
  }

  res.render('display_number', render_dictionary)
});

var listener = app.listen(
  process.env.PORT || 8080,
  process.env.HOST || "0.0.0.0",
  function() {
    console.log("Express server started on http://127.0.0.1:8080");
});