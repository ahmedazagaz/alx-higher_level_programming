#!/usr/bin/node
const axios = require('axios');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

axios.get(apiUrl + movieId)
  .then((response) => {
    const characters = response.data.characters;

    const characterPromises = characters.map((characterUrl) => {
      return axios.get(characterUrl);
    });

    Promise.all(characterPromises)
      .then((characterResponses) => {
        for (const characterResponse of characterResponses) {
          console.log(characterResponse.data.name);
        }
      })
      .catch((error) => {
        console.error('Error fetching characters:', error.message);
      });
  })
  .catch((error) => {
    console.error('Error fetching movie data:', error.message);
  });
