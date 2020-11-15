var http = require('http')

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});


    const https = require('https');

    https.get('https://io.adafruit.com/api/v2/Paces53/feeds/sensordata/data/last', (resp) => {
      let data = '';

      // A chunk of data has been recieved.
      resp.on('data', (chunk) => {
        data += chunk;
      });

      // The whole response has been received. Print out the result.
      resp.on('end', () => {
        res.end(JSON.parse(data).explanation);
        console.log(JSON.parse(data).explanation)
      });

    }).on("error", (err) => {
      console.log("Error: " + err.message);
    });
}).listen(8888);




console.log('Servidor à escuta na porta 7777...')
