const axios = require('axios');
const http = require('http');
               
function getLastSoundValue() {
    value = '';
    const options = {
        headers: { 'X-AIO-Key': 'aio_KgtP88Z5IAEdT78vSQOfTQ6Zj7xK' }
    };
    
    axios.get('https://io.adafruit.com/api/v2/Barca88/feeds/workshop-somanalog/data/last', options)
        .then((resp) => {
            lastdata = resp.data;
            soundLevel = parseInt(lastdata.value);

            console.log(soundLevel);
            value += soundLevel;
        }).catch((err) => {
            console.log('Erro :'+err);
            value += 'Erro' + err;
        });

        return value;
}

var servidor = http.createServer(function (req, res) {
            res.writeHead(200, {
                'Content-type': 'text/html; charset=utf-8'
            })

            value = '';
            getLastSoundValue((value) => {
                console.log('aaa'+value)
                res.write(`<p>Last Value: ${value} dB</p>`);
                res.end();
            })
}).listen(7777)

console.log('Listening on 7777...')



