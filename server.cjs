const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = __dirname;
const files = {'/':'index.html', '/index.html':'index.html', '/styles.css':'styles.css', '/app.js':'app.js'};
const types = {'.html':'text/html; charset=utf-8', '.css':'text/css; charset=utf-8', '.js':'text/javascript; charset=utf-8'};
http.createServer((request, response) => {
  const route = new URL(request.url, 'http://localhost').pathname;
  const name = files[route];
  if (!name) { response.writeHead(404); response.end('Not found'); return; }
  fs.readFile(path.join(root, name), (error, content) => {
    if (error) { response.writeHead(500); response.end('Unable to load page'); return; }
    response.writeHead(200, {'Content-Type': types[path.extname(name)], 'Cache-Control':'no-store'});
    response.end(content);
  });
}).listen(4173, '127.0.0.1', () => console.log('Keymaker ready at http://127.0.0.1:4173'));
