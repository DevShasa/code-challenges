// Given N = 512 and k = 10 
// function should return 972
// result us obtained by increasing first value of N four times and second digit six times 

function solution(N, K){
    // convert n to an array
    const intN = []
    for(const i of N.toString()){
        intN.push(Number(i))
    }

    
    const finalArr = []
    for(const i of intN){
        let arrNum = i
        while( arrNum !== 9 ){
            if(K === 0){
                break
            }else{
                arrNum = arrNum + 1
                K = K - 1
            }
        }
        finalArr.push(arrNum.toString())
    }

    return Number(finalArr.join(''))
}

console.log(solution(512, 10))