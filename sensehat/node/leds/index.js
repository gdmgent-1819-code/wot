'use strict';
const sense = require('sense-hat-led');

/*sense.setPixel(0, 7, [244, 0, 0], err => {
    sense.getPixel(0, 7, (err, color) => {
        console.log(color);
    });
});*/

const X = [0, 255, 255];
const O = [0, 0, 0];

/*const M = [
    O, O, O, X, X, O, O, O,
    O, O, X, O, O, X, O, O,
    O, O, O, O, O, X, O, O,
    O, O, O, O, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, O, O, O, O
]

sense.setPixels(M);*/

const COLOR = [255, 0, 0];

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
for(let x=0;x<=7;x+=2) {
    for(let y=0;y<=7;y+=2) {
        flashLED(x, y, 400+Math.round(Math.random()*2600));
    }
}

