'use strict';
const sense = require('sense-hat-led');

function randomColor() {
    return [
        Math.round(Math.random()*255),
        Math.round(Math.random()*255),
        Math.round(Math.random()*255)
    ]
}

function flashLED(x, y, delay) {
    setTimeout(() => {
        sense.setPixel(x, y, randomColor());
        flashLED(x, y, delay)
    }, delay);
}

sense.clear();
for(let x=0;x<=7;x+=1) {
    for(let y=0;y<=7;y+=1) {
        flashLED(x, y, 400+Math.round(Math.random()*2600));
    }
}

