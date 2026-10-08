## mini language compiler

### run (linux)
write in your terminal: python3 miniComp.py -i fibbonacci.mini

You can replace "fibbonacci.mini" with your file name

### example program written in mini with comments

let a = 1; ```Declaration of a variable named 'a' with the value 1```

let b = 1; ```Declaration of a variable named 'b' with the value 1```

let c = 1; ```Declaration of a variable named 'c' with the value 1```


printvar(a); ```printing the value of the variable a```

printvar(b); ```printing the value of the variable b```


for(10) { ```A loop that will iterate through the contents 10 times```

    add(a, b, c); ```Add a and b variables and store the result in the variable c```
    
    a = b; ```Assignment of the variable a to the variable b```
    
    b = c; ```Assignment of the variable b to the variable c```
    
    printvar(b); ```printing the value of the variable b```
    
} ```End of loop```
