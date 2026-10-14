const API_URL = "http://127.0.0.1:5000";
const board = document.getElementById("board");

let puzzle;
let solution;

let mistakes = 0;
const mistakesDisplay = document.getElementById("mistakes");

let seconds = 0;
const timerDisplay = document.getElementById("timer");

let timerId;

let difficulty = "medium";

const startScreen = document.getElementById("start-screen");
const gameScreen = document.getElementById("game-screen");
const playBtn = document.getElementById("play-btn");

document.querySelectorAll(".diff-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
        difficulty = btn.dataset.level;

        document.querySelectorAll(".diff-btn").forEach(function (b) {
            b.classList.remove("selected-diff");
        });
        btn.classList.add("selected-diff");
    });
});

async function loadPuzzle() {
    const response = await fetch(API_URL + "/api/puzzle?difficulty=" + difficulty);
    const data = await response.json();

    puzzle = data.puzzle;
    solution = data.solution;

    buildBoard();
}

function buildBoard() {
    board.innerHTML = "";

    for (let i = 0; i < 81; i++) {
        const row = Math.floor(i / 9);
        const col = i % 9;

        const cell = document.createElement("div");
        cell.classList.add("cell");
        cell.dataset.row = row;
        cell.dataset.col = col;

        const value = puzzle[row][col];

        if (value !== 0) {
            cell.textContent = value;
            cell.classList.add("given");
        }

        if (col === 2 || col === 5) {
            cell.classList.add("border-right");
        }
        if (row === 2 || row === 5) {
            cell.classList.add("border-bottom");
        }

        cell.addEventListener("click", function () {
            const old = document.querySelector(".selected");
            if (old) {
                old.classList.remove("selected");
            }
            cell.classList.add("selected");
        });

        board.appendChild(cell);
    }
}

function startTimer() {
    clearInterval(timerId);

    timerId = setInterval(function () {
        seconds++;

        const mins = Math.floor(seconds / 60);
        const secs = seconds % 60;

        timerDisplay.textContent =
            String(mins).padStart(2, "0") + ":" + String(secs).padStart(2, "0");
    }, 1000);
}

function checkWin() {
    const cells = document.querySelectorAll(".cell");

    for (const cell of cells) {
        const row = Number(cell.dataset.row);
        const col = Number(cell.dataset.col);

        if (Number(cell.textContent) !== solution[row][col]) {
            return;
        }
    }

    clearInterval(timerId);
    document.getElementById("message").textContent = "🎉 Well done! You solved it!";
}

async function resetGame() {
    clearInterval(timerId);

    mistakes = 0;
    seconds = 0;
    mistakesDisplay.textContent = 0;
    timerDisplay.textContent = "00:00";
    document.getElementById("message").textContent = "";

    await loadPuzzle();
    startTimer();
}

document.getElementById("new-game-btn").addEventListener("click", resetGame);

document.addEventListener("keydown", function (event) {
    const selected = document.querySelector(".selected");

    if (!selected) {
        return;
    }

    if (selected.classList.contains("given")) {
        return;
    }

    if (event.key >= "1" && event.key <= "9") {
        selected.textContent = event.key;

        const row = Number(selected.dataset.row);
        const col = Number(selected.dataset.col);

        if (Number(event.key) === solution[row][col]) {
            selected.classList.remove("wrong");
            checkWin();
        } else {
            selected.classList.add("wrong");
            mistakes++;
            mistakesDisplay.textContent = mistakes;
        }
    }

    if (event.key === "Backspace" || event.key === "Delete") {
        selected.textContent = "";
        selected.classList.remove("wrong");
    }
});

playBtn.addEventListener("click", async function () {
    startScreen.classList.add("hidden");
    gameScreen.classList.remove("hidden");
    await loadPuzzle();
    startTimer();
});