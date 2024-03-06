def  ds(str):
    result  = set()
 
    for i in range(len(str)+1):
        for k in range( i , len(str)+1):
 
            result.add(str[i:k])
        return len(result)

# test 
str = "abcd"

print(ds(str))

#hiii