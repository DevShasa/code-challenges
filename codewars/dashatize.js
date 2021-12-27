const dashatize = (n) =>{
    if(typeof n === "number"){
        let num = Math.abs(n)
        let outstr = ''
        let nstring = num.toString()
        for(let x in nstring){
            if(parseInt(nstring[x]) & 2 !== 0){
                outstr += `-${nstring[x]}-`
            }else{
                outstr += nstring[x]
            }
        }

        //clean the output
        if(outstr[0]=== "-"){
            outstr = outstr.slice(1) // position one to the end
        }
        if(outstr[outstr.length-1] === "-"){
            outstr = outstr.slice(0, -1) 
        }

        return outstr.replace(/--/g, "-")
    }
    return "None"
}