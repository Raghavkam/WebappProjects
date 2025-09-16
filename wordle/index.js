const express = require("express");
const app = express();

const fs = require('fs');		// fs is built-in. no npm install
const path = require('path');	// path is built-in. no npm install

const bodyParser = require('body-parser');
app.use(bodyParser.json());

// Generate a file path (as a string) for the words file
const wordsFilePath = path.join(__dirname, 'enable1.txt');

// Use fs to read the file; convert bytes to string split on newlines
const words = fs.readFileSync(wordsFilePath).toString().split('\n');

// Filter words based on conditions
function filterWords(conditions) {
  return words.filter(word => {
    if (word.length !== 5) return false; // Ensure word length is 5
    for (let i = 0; i < 5; i++) {
      if (conditions.known[i] && conditions.known[i] !== word[i]) return false;
    }
    return true;
  });
}

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// (words is now an array of the entire enable1.txt file)
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/wordfinder', (req, res) => {
  const conditions = req.body;
  const newDictionary = filterWords(conditions);
  res.json(newDictionary);
});

const listener = app.listen(
  process.env.PORT || 8080,
  process.env.HOST || "0.0.0.0",
  function() {
    console.log("Express server started");
  }
);
