def addtochart(chart, index, state):
    
    if state in chart[index]:
        
        return False
        
    else:
        
        chart[index] = chart[index]+[state]
        
        return True
