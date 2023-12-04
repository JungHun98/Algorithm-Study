function solution(n, words) {
    let answer = [0, 0];
    let wordSet = new Set();
    let prevChar = words[0][0];
    
    for(let i = 0; i < words.length; i++){
        if(prevChar !== words[i][0] || words[i].length === 1 || wordSet.has(words[i])){
            let temp = (i+1)%n === 0 ? n : (i+1)%n;
            answer = [temp, Math.ceil((i+1)/n)];
            break;
        }
        wordSet.add(words[i]);
        prevChar = words[i][words[i].length - 1];
    }
    
    return answer;
}