
const http = require('http');

const handle_request = function (req, res) {

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('recvd request for: ');
    res.write(req.url);
    res.write('\n');
    res.end();
}

const ws = http.createServer(handle_request);
ws.listen(7081);