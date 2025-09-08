/*
012345
..X... 0
.SAMX. 1
.A..A. 2
XMAS.S 3
.X.... 4

row, col
0, 2
left: 0,1; 0,0; 0,null -> break
left-up: -1,0 ->
up: 
right-up:
right:
right-down:
down:
left-down:

helper function takes two arguments (start_row, start_col, vertical_dir, horizontal_dir)
- initialize an empty array
- start for loop (4) i = 0; i < 4; i++
  - push row + vertical_dir(-1, 0, +1) * i, col + horizontal_dir(-1, 0, +1) * i to array
- join the array


0123456789
....XXMAS. 0
.SAMXMS... 1
...S..A... 2
..A.A.MS.X 3
XMASAMX.MM 4
X.....XA.A 5
S.S.S.S.SS 6
.A.A.A.A.A 7
..M.M.M.MM 8
.X.X.XMASX 9


- loop through entire input
- for each char, create 4 letter word in each direction (up, right-up, right, right-down, down, left-down, left, left-up)
- count all words that are XMAS (forward or reverse)

*/

import { readFileSync } from "fs";

function countAllXMAS(filename) {
  const input = formatPuzzleInput(filename)
  let xmasCount = 0;

  for (let row = 0; row < input.length; row++) {
    for (let col = 0; col < input[row].length; col++) {
      words = createWordsInGrid(row, col, input);
      xmasCount += countXMASOccurences(words);
    }
  }

  return xmasCount;
}

function formatPuzzleInput(filename) {
  const rawData = readFileSync(`./${filename}`, "utf-8");
  return rawData.split('\n').map(row => row.split(''));
}

function createWordsInGrid(start_row, start_col, input) {
  const words = [];

  for (let vertical_dir = -1; vertical_dir <= 1; vertical_dir++) {
    for (let horizontal_dir = -1; horizontal_dir <= 1; horizontal_dir++) {
      if (vertical_dir === 0 && horizontal_dir === 0) continue;
      const singleDirectionWord = createWordInDirection(
        start_row,
        start_col,
        vertical_dir,
        horizontal_dir,
        input
      );
      if (singleDirectionWord) words.push(singleDirectionWord);
    }
  }

  return words;
}

function countXMASOccurences(words) {
  return words.reduce((sum, word) => {
      if (word === "XMAS") {
        return (sum += 1);
      } else {
        return sum;
      }
    }, 0);
}

function createWordInDirection(start_row, start_col, vertical_dir, horizontal_dir, input) {
  const word = [];
  
  if (input[start_row][start_col] !== 'X') return;

  for (let i = 0; i < 4; i++) {    
    const row = vertical_dir === 0 ? start_row : start_row + (vertical_dir * i);
    const col = horizontal_dir === 0 ? start_col : start_col + (horizontal_dir * i);

    if (!input[row] || !input[col]) return;

    word.push(input[row][col])
  }

  return word.join('')
}

// console.log(countAllXMAS('example.txt'));
console.log(countAllXMAS('puzzle.txt'))