/*

0123456789
MMMSXXMASM 0
MSAMXMSMSA 1
AMXSXMAAMM 2
MSAMASMSMX 3
XMASAMXAMM 4
XXAMMXXAMA 5
SMSMSASXSS 6
SAXAMASAAA 7
MAMMMXMMMM 8
MXMXAXMASX 9

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



*/

import { readFileSync } from "fs" 

const rawExampleData = readFileSync(`./example.txt`, 'utf-8');
const example = rawExampleData.split('\n').map(row => row.split(''));

/*
constant that holds corner coordinates from a center and corresponding diag inststructions

[start_row_dir, start_col_dir, vertical_dir, horizonal_dir, input]
[-1, -1, 1, -1] start top left, go right-down
[1, -1, -1, 1] start top right, go left-down
[-1, 1, 1, -1] start bottom left, go up-right
[1, 1, -1, -1] start bottom right, go left-up

row = start_row
col = start_col

row = row + vertical_dir
col = col + horizontal_dir
*/

const CORNER_START_AND_DIRECTION = [
  [-1, -1, 1, 1],
  [1, -1, -1, 1],
  [-1, 1, 1, -1],
  [1, 1, -1, -1],
];

function countAllXMASGrid(filename) {
  let XMASgridCount = 0;
  const input = formatPuzzleInput(filename)
  
  for (let row = 0; row < input.length; row++) {
    for (let col = 0; col < input[row].length; col++) {
      if (isXMASGrid(input, row, col)) XMASgridCount++;
    }
  }

  return XMASgridCount;
}

function formatPuzzleInput(filename) {
  const rawData = readFileSync(`./${filename}`, "utf-8");
  return rawData.split("\n").map((row) => row.split(""));
}

function isXMASGrid(input, start_row, start_col) {
  const cornerWords = generateCornerWords(input, start_row, start_col);
  return cornerWords.filter(word => word.join('') === 'MAS').length === 2;
}

// console.log(isXMASGrid(example, 1, 2));


function generateCornerWords(input, start_row, start_col) {
  const words = [];

  for (let corner of CORNER_START_AND_DIRECTION) {
    const [start_row_dir, start_col_dir, vertical_dir, horizonal_dir] = corner
    let row = start_row + start_row_dir;
    let col = start_col + start_col_dir;
    const word = [];

    for (let i = 0; i < 3; i++) {
      if (!input[row] || !input[row][col]) continue;
      word.push(input[row][col])
      row += vertical_dir
      col += horizonal_dir
    }
    words.push(word)
  }
  
  return words;
}

// console.log(generateCornerWords(example, 1, 2));

console.log(countAllXMASGrid('./example.txt'));
console.log(countAllXMASGrid('./puzzle.txt'));