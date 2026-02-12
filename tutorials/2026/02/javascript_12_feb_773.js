// Recursive Backtracking in JavaScript
//======================================

function solveSudoku(board) {
    // function to check if a number is valid on the board
    function isValid(num, row, col) {
        // check row and column for duplicates
        for (let i = 0; i < 9; i++) {
            if (board[row][i] === num || board[i][col] === num) return false;
        }

        // check 3x3 sub-grid for duplicates
        let startRow = row - row % 3;
        let startCol = col - col % 3;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                if (board[i + startRow][j + startCol] === num) return false;
            }
        }

        // number is valid
        return true;
    }

    // function to solve the Sudoku board recursively
    function solveBoard() {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (board[i][j] === 0) { // find an empty cell to fill in
                    for (let num = 1; num <= 9; num++) {
                        if (isValid(num, i, j)) { // check if the number is valid on the board
                            board[i][j] = num; // place the number on the board

                            if (solveBoard()) return true; // solve the rest of the board

                            board[i][j] = 0; // reset the cell to empty if it doesn't lead to a solution
                        }
                    }

                    return false; // no valid numbers, so this path leads to no solution
                }
            }
        }

        return true; // all cells filled in successfully
    }

    return solveBoard();
}

// Test the function
let board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
];

console.log(solveSudoku(board));