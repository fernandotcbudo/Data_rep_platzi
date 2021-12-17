def open_or_senior(*data):
    output=[]
    for d in data:
        if d[0] > 54 and d[1] > 7:
            output.append("Senior")
        else:
            output.append("Open") 
    return output

if __name__ == "__main__":
    var= open_or_senior([60,40])
    print(var)


        

