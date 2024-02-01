let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input[0];
const map = [];

for(let i = 1; i < input.length; i++){
    let temp = input[i].split(' ').map((elem) => +elem);
    map.push(temp);
}

let answer = 0;

function moveTop(board){
    let newBoard = Array.from(new Array(N), (_, i) => new Array(N).fill(0));

    for(let i = 0; i < N; i++){
        let newIdx = 0;
        let addIdxSet = new Set();
        
        for(let j = 0; j < N; j++){
            if(board[j][i] !== 0){
                if(newIdx !== 0 && newBoard[newIdx - 1][i] === board[j][i] && !addIdxSet.has(newIdx - 1)){
                    newBoard[newIdx - 1][i] += board[j][i];
                    addIdxSet.add(newIdx - 1);
                }
                else{
                    newBoard[newIdx][i] = board[j][i];
                    newIdx += 1;
                }
            }
        }
    }

    return newBoard;
}

function moveBottom(board){
    let newBoard = Array.from(new Array(N), (_, i) => new Array(N).fill(0));

    for(let i = N-1; i >= 0; i--){
        let newIdx = N-1;
        let addIdxSet = new Set();
        
        for(let j = N-1; j >= 0; j--){
            if(board[j][i] !== 0){
                if(newIdx !== N-1 && newBoard[newIdx + 1][i] === board[j][i] && !addIdxSet.has(newIdx + 1)){
                    newBoard[newIdx + 1][i] += board[j][i];
                    addIdxSet.add(newIdx + 1);
                }
                else{
                    newBoard[newIdx][i] = board[j][i];
                    newIdx -= 1;
                }
            }
        }
    }

    return newBoard;
}

function moveLeft(board){
    let newBoard = Array.from(new Array(N), (_, i) => new Array(N).fill(0));

    for(let i = 0; i < N; i++){
        let newIdx = 0;
        let addIdxSet = new Set();
        
        for(let j = 0; j < N; j++){
            if(board[i][j] !== 0){
                if(newIdx === 0){
                    newBoard[i][newIdx] = board[i][j];
                    newIdx += 1;
                }
                else{
                    if(newBoard[i][newIdx - 1] === board[i][j]){
                        if(addIdxSet.has(newIdx - 1)){
                            newBoard[i][newIdx] = board[i][j];
                            newIdx += 1;
                        }
                        else{
                            newBoard[i][newIdx - 1] += board[i][j];
                            addIdxSet.add(newIdx - 1);
                        }
                    }
                    else{
                        newBoard[i][newIdx] = board[i][j];
                        newIdx += 1;
                    }
                }
            }
        }
    }

    return newBoard;
}

function moveRight(board){
    let newBoard = Array.from(new Array(N), (_, i) => new Array(N).fill(0));

    for(let i = N-1; i >= 0; i--){
        let newIdx = N-1;
        let addIdxSet = new Set();
        
        for(let j = N-1; j >= 0; j--){
            if(board[i][j] !== 0){
                if(newIdx === N-1){
                    newBoard[i][newIdx] = board[i][j];
                    newIdx -= 1;
                }
                else{
                    if(newBoard[i][newIdx + 1] === board[i][j]){
                        if(addIdxSet.has(newIdx + 1)){
                            newBoard[i][newIdx] = board[i][j];
                            newIdx -= 1;
                        }
                        else{
                            newBoard[i][newIdx + 1] += board[i][j];
                            addIdxSet.add(newIdx + 1);
                        }
                    }
                    else{
                        newBoard[i][newIdx] = board[i][j];
                        newIdx -= 1;
                    }
                }
            }
        }
    }

    return newBoard;
}

function dfs(board, d, depth){
    if(depth > 5){
        let max = 0;
        let maxList = board.forEach((list) => {
            let value = Math.max(...list);
            if(max < value){
                max = value;
            }
        });

        if(answer < max){
            answer = max;
        }
        return;
    }

    let nextBoard = [];
    //상
    if(d === 0) {
        nextBoard = moveTop(board);
    }
    //하
    else if(d === 1) {
        nextBoard = moveBottom(board);
    }
    //좌
    else if(d === 2) { 
        nextBoard = moveLeft(board);
    }
    //우
    else {
        nextBoard = moveRight(board);
    }

    for(let i = 0; i < 4; i++){
        dfs(nextBoard, i, depth+1);
    }
}

for(let i = 0; i < 4; i++){
    dfs(map, i, 1);
}

console.log(answer);
