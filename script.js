const cells = document.querySelectorAll(".cell");
const message = document.getElementById("message");
const resetButton = document.getElementById("reset");

let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let gameActive = true;

const winningConditions = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];

function checkWinner() {
    for (let condition of winningConditions) {
        const [a, b, c] = condition;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            gameActive = false;
            message.textContent = `Player ${currentPlayer} wins!`;
            return;
        }
    }
    if (!board.includes("")) {
        gameActive = false;
        message.textContent = "It's a tie!";
    }
}

function handleClick(e) {
    const index = e.target.getAttribute("data-index");
    if (board[index] !== "" || !gameActive) return;

    board[index] = currentPlayer;
    e.target.textContent = currentPlayer;

    checkWinner();

    if (gameActive) {
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        message.textContent = `Player ${currentPlayer}'s turn`;
    }
}

function resetGame() {
    board = ["", "", "", "", "", "", "", "", ""];
    gameActive = true;
    currentPlayer = "X";
    cells.forEach(cell => cell.textContent = "");
    message.textContent = `Player ${currentPlayer}'s turn`;
}

cells.forEach(cell => cell.addEventListener("click", handleClick));
resetButton.addEventListener("click", resetGame);
