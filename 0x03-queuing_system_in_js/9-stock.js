const express = require('express');

const app = express();
const port = 1245;

const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

app.get('/list_products', (request, response) => {
  const array = [];

  for (let i = 1; i <= listProducts.length; i += 1) {
    const product = getItemById(i);
    if (product) {
      array.push(product);
    }
  }
  response.json(array);
});

app.listen(port);
