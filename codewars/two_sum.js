// Write a function that takes an array of numbers and a target number
// It should find two different items in the array that when added together 
// give the target value 

// First attempt it works using nested for loops 
function twoSum1(numbers, target){
    for(let x = 0; x < numbers.length; x++){
        for(let y = x+1; y< numbers.length; y++){
            if(numbers[x] + numbers[y] === target){
                return [x, y];
            }
        }
    }
}

// Second attempt, eliminates one nested for loop
function twoSum(numbers, target){
    for(let x = 0; x< numbers.length; x++){
        if(numbers.includes(target - numbers[x])){
            return [x, numbers.lastIndexOf(target - numbers[x])]
        }
    }
}
