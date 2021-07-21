/*
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
*/


function endsWithNumber(str){
    // Check if the string ends with a number
    let lastIndex = parseInt(str[str.length -1])
    if(isNaN(lastIndex)){
        return false;
    } else {
        return true;
    }
}

function extractNumber(str){
    // extracts the number from the end of the string and adds one to it

    // Extract the number
    let nums =  str.match(/(\d+)/)[0]
    
    //convert to int and add one
    let num = parseInt(nums) + 1;

    // convert to string
    let numStr = num.toString();
    
    // Add any leading zeroes in the original number
    let diff = nums.length - numStr.length
    for(let x = 0; x < diff ; x++){
        numStr = "0" + numStr
    }
    return numStr
}
function extractString(str){
    // extract the letters from a string
    return str.replace(str.match(/(\d+)/)[0], "")
}

function incrementString(string){
    if(endsWithNumber(string)){
        return extractString(string) + extractNumber(string)
    }else{
        return string + "1"
    }
}   
