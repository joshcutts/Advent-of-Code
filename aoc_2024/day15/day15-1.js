/*



*/

import { readFileSync } from "fs";

function formatPuzzleInput(filename) {
  const rawData = readFileSync(`./${filename}`, "utf-8");
  const [movementMap, moves] = rawData.split("\n\n")

  const modMovMap = movementMap.split("\n").map((row) => row.split(""));
  

  return [modMovMap, moves.split('').filter(move => move !== '\n')]
}


function findRobotStart(warehouseMap) {
  let start = []

  warehouseMap.forEach((__ ,row) => {
    warehouseMap.forEach((_, col) => {
      if (warehouseMap[row][col] === '@') start = [row, col]
    })
  })
  console.log(start)
  return start
}

function traverse(warehouseMap, moves) {
  let currentLoc = findRobotStart(warehouseMap)
  console.log(currentLoc);

  moves.forEach(moveSym => {
    currentLoc = move(currentLoc, moveSym)
  })
}

const translate = {
  '^': [-1, 0],
  'v': [1, 0],
  '<': [0, -1],
  '>': [0, 1]
}

function reverse(moveSym) {
  if (moveSym === '^') {
    return "v";
  } else if (moveSym === 'v') {
    return "^";
  } else if (moveSym === '<') {
    return ">";
  } else if (moveSym === '>') {
    return "<";
  }
}

function move(currentLoc, moveSym) {
  console.log("current", currentLoc, moveSym);
  const movement = translate[moveSym]
  let nextLoc = [currentLoc[0] + movement[0], currentLoc[1] + movement[1]];
  let nextLocItem = warehouseMap[nextLoc[0]][nextLoc[1]]

  if (nextLocItem === '.') {
    warehouseMap[currentLoc[0]][currentLoc[1]] = ".";
    warehouseMap[nextLoc[0]][nextLoc[1]] = "@";
    // printMap(warehouseMap);
    return nextLoc;
  } else if (nextLocItem === 'O') {
    while (nextLocItem === "O") {
      nextLoc[0] = nextLoc[0] + movement[0]
      nextLoc[1] = nextLoc[1] + movement[1]
      nextLocItem = warehouseMap[nextLoc[0]][nextLoc[1]];
      // console.log(currentLoc, movement, nextLoc, nextLocItem);
    }

    if (nextLocItem === ".") {
      warehouseMap[nextLoc[0]][nextLoc[1]] = "O";
      warehouseMap[currentLoc[0]][currentLoc[1]] = '.';
      warehouseMap[currentLoc[0] + movement[0]][currentLoc[1] + movement[1]] = "@";
      // printMap(warehouseMap)
      return [currentLoc[0] + movement[0], currentLoc[1] + movement[1]];
    }
    // printMap(warehouseMap);
    return currentLoc
  } else {
    return currentLoc
  }
}

function calculateGPSScore(warehouseMap) {
  let result = 0;
  
  for (let row = 0; row < warehouseMap.length; row++) {
    for (let col = 0; col < warehouseMap[row].length; col++) {

      if (warehouseMap[row][col] === 'O') {
        result += ((100 * row) + col)
      }
    }
  }

  return result
}

function printMap(warehouseMap) {
  warehouseMap.forEach(row => console.log(row.join('')))
}

// const [warehouseMap, moves] = formatPuzzleInput("example.txt");
const [warehouseMap, moves] = formatPuzzleInput("puzzle.txt");
traverse(warehouseMap, moves)


console.log(calculateGPSScore(warehouseMap))