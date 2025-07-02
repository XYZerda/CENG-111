def count_rectangles(Pattern):
    
    count=0
    
    cerceveli_pattern = []
    
    cerceveli_pattern.append((len(Pattern[0])+2)*'0')
    
    for a in range(0,len(Pattern)):
        
        cerceveli_pattern.append('0'+Pattern[a]+'0')
        
    cerceveli_pattern.append((len(Pattern[0])+2)*'0')
    
    #cerceveli pattern ile 0'lardan oluşan bir çerçeve yaptık inputa.
    #dikdörtgenin her köşesi kendinden önce veya sonra bir sıfır içerecek böylece.
    
    rectangles = helper(cerceveli_pattern)
    
    for elm in rectangles:
        
        st_row = elm[0]
        st_col = elm[1]
        end_row = elm[2]
        end_col = elm[3]

        aday = birleştirici(cerceveli_pattern, st_row, st_col, end_row, end_col)

        if controller(aday) == "valid":

            count+=1
      
    return count

def helper(cerceveli_pattern):
        
    results = []
    
    for i in range(1,len(cerceveli_pattern)-1):
            
        for j in range(1,len(cerceveli_pattern[0])-1):
                
            if cerceveli_pattern[i][j]=="1":

                for bottom in range(i,len(cerceveli_pattern)):

                    if cerceveli_pattern[bottom][j] == "0": 

                        bottom -= 1

                        break
                    
                    for right in range(j, len(cerceveli_pattern[0])):
                        
                        if cerceveli_pattern[i][right] == "0":

                            right -= 1

                            break

                        if is_rectangle(cerceveli_pattern, i, j, bottom, right):

                            results.append((i, j, bottom, right))
                    
    return results            
                
def is_rectangle(cerceveli_pattern, st_row, st_col, end_row, end_col):
# Dikdörtgenin tüm kenarlarının 1 olması gerekiyor
    for row in range(st_row, end_row + 1):
        
        if cerceveli_pattern[row][st_col] != "1" or cerceveli_pattern[row][end_col] != "1":
        
            return False

    for col in range(st_col, end_col + 1):
        
        if cerceveli_pattern[st_row][col] != "1" or cerceveli_pattern[end_row][col] != "1":
        
            return False

    return True
    
def birleştirici(cerceveli_pattern,st_row,st_col,end_row,end_col):
        
    aday_rectangle=[]
        
    for row in range(st_row, end_row+1):
            
        result= cerceveli_pattern[row][st_col:end_col+1]
                
        aday_rectangle.append(result)

    return aday_rectangle
                        
def controller(aday_rectangle):
        
    has_zero = False

    for row in aday_rectangle[1:-1]:

        for char in row[1:-1]:

            if char == "0":

                has_zero = True

    return "valid" if has_zero else "invalid"
