const express = require('express');
const app = express();
const cookieParser = require('cookie-parser')

app.set('view engine', 'ejs')
app.use(cookieParser());


app.get('/', (req,res) => {

  res.render('home')
})

app.get('/worker_route', (req, res) => {
  
  const choices = ['dogs', 'cats', 'turtles', 'fish', 'birds', 'rabbits']

  const out = {
    'your_number' : Math.floor(Math.random() * 10),
    'your_pet' : choices[ Math.floor(Math.random() * 5) ]
  }

  res.json(out)

});


var listener = app.listen(
  process.env.PORT || 8080,
  process.env.HOST || "0.0.0.0",
  function() {
    console.log("Express server started on http://127.0.0.1:8080");
});