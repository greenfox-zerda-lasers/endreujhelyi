'use strict';

// write a function called each that takes an array and a function as a parameter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

function each(inputList, func) {
  for (var i = 0; i < inputList.length; i++) {
    func(inputList[i]);
  }
};

function rocker(inputBand) {
  console.log(inputBand);
}

var bands = ['Jimmy Eat World', 'The Ghost Inside', 'Touche Amore', 'Violent Soho'];
each(bands, rocker);
