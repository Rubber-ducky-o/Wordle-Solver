document.addEventListener("DOMContentLoaded", async () =>{
    createSquares();

    let guessedWords = [[]];
    let availableSpace = 1;
    let word = "";
    let guessedWordCount = 0;
    let gameOver = false;
    let isAnimating = false;
    let validWords = new Set();

    const keys = document.querySelectorAll('.keyboard-row button')

    async function loadTextFile(path){
        try{
            const response = await fetch(path);
            if (!response.ok) throw new Error("Network error");

            const text = await response.text();

            const lines = text.split(/\r?\n/).map(line => line.trim().toLowerCase()).filter(line => line.length === 5);
            if (lines.length === 0){
                console.log("File is empty please download 5-letter-words.txt");
                return;
            }

            validWords = new Set(lines);
            const randomIndex = Math.floor(Math.random() * lines.length);

            word = lines[randomIndex];


        }catch (error){
            console.error("Error loading file");
        }


    }
    await loadTextFile("./5-letter-words.txt");

    function getCurrentWordArr()
    {
        const numberOfGuessedWords = guessedWords.length;
        return guessedWords[numberOfGuessedWords -1];
    }
    function updateGuessedWords(letter){
        if (gameOver || isAnimating) return;

        const currWordArr = getCurrentWordArr();

        if (currWordArr && currWordArr.length <5){
            currWordArr.push(letter);

            const availableSpaceEl = document.getElementById(availableSpace);

            availableSpace++;

            availableSpaceEl.textContent = letter;

        }
    };
    function getTileColor(letter,index){
        const isCorrectLetter = word.includes(letter)

        if(!isCorrectLetter){
            return "rgb(58,58,60)";
        }

        const letterInThatPosition = word.charAt(index);
        const isCorrectPosition = (letter === letterInThatPosition);

        if (isCorrectPosition){
            return "rgb(83,141,78)";
        }

        return "rgb(181,159,59)";
    }

    function updateSubColor(letter,tileColor){
        const keyboardKey = document.querySelector(`button[data-key="${letter.toLowerCase()}"]`);
        if (!keyboardKey) return;

        const colorPriority = {
            gray: 1,
            yellow: 2,
            green: 3
        };
        let newState;

        if (tileColor === "rgb(83,141,78)"){
            newState = "green";

        }else if (tileColor === "rgb(181,159,59)"){
            newState = "yellow";
        } else {
            newState = "gray";
        }
        const currentState = keyboardKey.dataset.colorState;

        if (currentState && colorPriority[currentState] >= colorPriority[newState]){
            return;
        }

        keyboardKey.dataset.colorState = newState;
        keyboardKey.style.backgroundColor = tileColor;
        keyboardKey.style.borderColor = tileColor;

    }
    function handleSubmitWord(){

        if(gameOver || isAnimating) return;

        const currWordArr = getCurrentWordArr();

        if (currWordArr.length !==5){
            window.alert("word must be 5 letters!");
            return;
        }

        const currentWord = currWordArr.join('').toLowerCase();
        if (!validWords.has(currentWord)){
            window.alert("Not a valid word!");
            return;
        }

        isAnimating = true;
        const firstLetterId = guessedWordCount * 5 +1;
        const interval = 200;

        currWordArr.forEach((letter,index)=> {
            setTimeout (()=>{
                const tileColor = getTileColor(letter,index);
                const letterId = firstLetterId + index;
                const letterEl = document.getElementById(letterId);

                letterEl.classList.add("animate__flipInX");
                letterEl.style.backgroundColor = tileColor;
                letterEl.style.borderColor = tileColor;

                updateSubColor(letter,tileColor);
            },interval * index);
        });
        guessedWordCount ++;

        const isCorrect = currentWord === word;
        const lastguess = guessedWordCount === 6;
        setTimeout(() => {
            isAnimating = false;

            if (isCorrect){
                gameOver = true;
                window.alert("Congratulations!");
                return;
            }

            if (lastguess){
                gameOver = true;
                window.alert(`No more guesses! The word was ${word}.`);
                return;
            }

            guessedWords.push([]);
        }, interval * 5);

    }

    function createSquares(){
        const gameBoard = document.getElementById("board");

        for (let index = 0; index < 30; index++)
        {
            let square = document.createElement("div")
            square.classList.add("square");
            square.classList.add("animate__animated");
            square.setAttribute("id",index +1);
            gameBoard.appendChild(square);
        }
    }

    for (let i = 0; i <keys.length; i++){
        keys[i].onclick = ({ target }) =>{
            const letter = target.getAttribute("data-key").toLowerCase();
            if (letter === 'enter'){
                handleSubmitWord();
            }else if(letter === "del"){
                handleDeleting();
            }
            else {
            updateGuessedWords(letter);
            }
        };
    }
    document.addEventListener("keydown", (event)=>{
        const key = event.key.toLowerCase();

        if(key === "enter"){
            handleSubmitWord();
        } else if(key === "delete" || key === "backspace"){
            handleDeleting();
        }else if (/^[a-z]$/.test(key)){
            updateGuessedWords(key);
        }
    })
    function handleDeleting(){
        if (gameOver || isAnimating) return;

        const currWordArr = getCurrentWordArr();

        if(currWordArr.length ===0){
            return;
        }

        currWordArr.pop();

        availableSpace--;

        const lastLetterEl = document.getElementById(availableSpace);
        lastLetterEl.textContent = "";
    }


});