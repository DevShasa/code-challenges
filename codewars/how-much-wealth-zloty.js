/*
testwealth 
https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/train/javascript

I always thought that my old friend John was rather richer than he looked, but I never knew exactly how much money he actually had. One day (as I was plying him with questions) he said:

"Imagine I have between m and n Zloty..." (or did he say Quetzal? I can't remember!)
"If I were to buy 9 cars costing c each, I'd only have 1 Zloty (or was it Meticals?) left."
"And if I were to buy 7 boats at b each, I'd only have 2 Ringglets (or was it Zloty?) left."
Could you tell me in each possible case:

how much money f he could possibly have ?
the cost c of a car?
the cost b of a boat?
So, I will have a better idea about his fortune. Note that if m-n is big enough, you might have a lot of possible answers.

Each answer should be given as ["M: f", "B: b", "C: c"] and all the answers as [ ["M: f", "B: b", "C: c"], ... ]. "M" stands for money, "B" for boats, "C" for cars.

Note: m, n, f, b, c are positive integers, where 0 <= m <= n or m >= n >= 0. m and n are inclusive.
*/


function checknumber(number){
    // Return true if a number is positive and has decimal integers, else return false 
    if(number % 1 === 0 && Math.sign(number) === 1){
        return true;
    } else{
        return false;
    }
}

function howmuch(m, n){
    // An array is created if both car and boat return true from checknumber() above     
    let finalarr = [];
    for (let x = Math.min(m, n); x <= Math.max(m,n); x++){
        let car = (x-1)/9;
        let boat  = (x-2)/7;

        if (checknumber(car) && checknumber(boat)){
            finalarr.push([`M: ${String(x)}`, `B: ${String(boat)}`, `C: ${String(car)}`]);
        } else{
            continue;
        }

    }

    return finalarr;
}
