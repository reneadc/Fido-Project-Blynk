var Blynk = require('blynk-library');
var Gpio = require('onoff').Gpio;

var AUTH = '9zG3ffG9aZzvwDfFUW6F0Ip8ChojH39P';

var blynk = new Blynk.Blynk(AUTH);

var v3 = new blynk.VirtualPin(3);



const { spawn } = require('child_process');
const child = spawn('ls', );
// use child.stdout.setEncoding('utf8'); if you want text chunks
child.stdout.on('data', (chunk) => {
  // data from the standard output is here as buffers
});
// since these are streams, you can pipe them elsewhere
child.stderr.pipe(dest);
child.on('close', (code) => {
  console.log(`child process exited with code ${code}`);
});

const exec = require('child_process').exec, child;

//connectToRaspberryPi
function connectToRaspberryPi{
//On Virtual Pin 3 execute the motorScript
v3.on('write', function(param) {
    if (param[0] == '1') {
	exec('cd servoMotor & sudo python motor.py');
    }

    console.log('V3:', param[0]);
    });
});