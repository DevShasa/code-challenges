/*
> create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:
1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
*/
multiplicationTable = function(size){
    let outer_arr = [];
    for(let x = 1; x <size + 1; x++){
        // The outer loop builds each individual subarray
        let inner_arr = [];
        let num = x
        for(let y = 0; y < size; y++){
            // This builds the inner loop 
            inner_arr.push(num);
            num += x
        } 
        outer_arr.push(inner_arr)
    }

    return outer_arr;
}