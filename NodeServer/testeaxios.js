const axios = require('axios');
const http = require('http');
               
var servidor = http.createServer(function (req, res) {
    const options = {
        headers: { 'X-AIO-Key': 'aio_nqoI77kQJQHwz74qcy5vhBwm0zOV' }
    };

    axios.get('https://io.adafruit.com/api/v2/Paces53/feeds/sensorfeed/data/last', options)
        .then((resp) => {
            res.writeHead(200, {
                'Content-type': 'text/html; charset=utf-8'
            })
            
            lastdata = resp.data;

            res.write(`<p>??????'+ ${lastdata.value} + '???????</p>`);

            console.log(lastdata);
            res.end();
        }).catch((err) => {
            console.log('Erro :'+err);
            res.write('<p>Pedido nao suportado: ' + req.method + '</p>');
            res.end();
        });
}).listen(7777)

console.log('Listening on 7777...')