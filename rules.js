document.addEventListener("DOMContentLoaded", () =>{
    createSquares();

    let guessedWords = [[]];
    const availableSpace = 1;


    const keys = document.querySelectorAll('.keyboard-row button')

    for (let i = 0; i <keys.length; i++){
        keys[i].onclick = ({ target }) =>{
            const letter = target.getAttribute("data-key");
            updateGuessedWords();
        };
    }
    function getCurrentWordArr()
    {
        const numberOfGuessedWords = guessedWords.length;
        return guessedWords[numberOfGuessedWords -1];
    }
    function updateGuessedWords(letter){
        const currWordArr = getCurrentWordArr();

        if (currWordArr && getCurrentWordArr.length <5){
            getCurrentWordArr.push(letter);
            const availableSpaceEl = document.getAElementById("board");
            availableSpace = availableSpace + 1;
            availableSpace.textContent = letter;

        }
    };



    function createSquares(){
        const gameBoard = document.getElementById("board");

        for (let index = 0; index < 30; index++)
        {
            let square = document.createElement("div")
            square.classList.add("square");
            square.setAttribute("id",index +1);
            gameBoard.appendChild(square);
        }
    }


});