const express = require('express');
const https = require('https');
const app = express();
app.set('view engine', 'ejs');

const baseUrl = 'https://api.weather.gov/points/';
const options = {
  headers: {
    'User-Agent': '(weather app) (me@bob.com)',
  },
};

app.use(express.static('public'));

app.get('/', (req, res) => {
  res.render('homePage');
});

app.get('/inputted', (req, res) => {
  const x = req.query.x;
  const y = req.query.y;

  if (!x || !y) {
    return res.render('homePage');
  }

  const url = baseUrl + x + ',' + y;

  fetchData(url, (error, jsonData) => {
    if (error) {
      console.error(error);
      return res.render('homePage');
    }

    const forecastUrl = jsonData.properties?.forecast;
    if (!forecastUrl) {
      return res.render('homePage');
    }

    fetchData(forecastUrl, (error, forecastData) => {
      if (error) {
        console.error(error);
        return res.render('homePage');
      }

      const periods = forecastData.properties?.periods;
      if (!periods || !Array.isArray(periods) || periods.length === 0) {
        return res.render('homePage');
      }

      const organizedData = {};
      periods.forEach((period) => {
        const dayNumber = period.number;
        organizedData[dayNumber] = {
          day: period.name,
          isDaytime: period.isDaytime,
          temperature: period.temperature,
          temperatureUnit: period.temperatureUnit,
          precipitationProbability: period.probabilityOfPrecipitation?.value || 'N/A',
          detailedForecast: period.detailedForecast,
        };
      });

      res.render('forecastPage', { data: organizedData });
    });
  });
});

function fetchData(url, callback) {
  https.get(url, options, (response) => {
    let rawData = '';
    response.on('data', (chunk) => {
      rawData += chunk;
    });

    response.on('end', () => {
      try {
        const jsonData = JSON.parse(rawData);
        callback(null, jsonData);
      } catch (error) {
        callback(error, null);
      }
    });
  }).on('error', (error) => {
    callback(error, null);
  });
}

const listener = app.listen(process.env.PORT || 8080, process.env.HOST || '0.0.0.0', () => {
  console.log('Express server started');
});
