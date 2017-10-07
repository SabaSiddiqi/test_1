def intersection(x,y,u,v):

    [x1, y1] = x
    [x2, y2] = y
    [w1, z1] = u
    [w2, z2] = v


    diff_y = y2 - y1
    diff_x = x1 - x2
    
    diff_z = z2 - z1
    diff_w = w1 - w2
    
    eq1 = diff_y*x1 + diff_x*y1
    eq2 = diff_z*w1 + diff_w*z1
    

    slope_calc = diff_y*diff_w - diff_z*diff_x
    
    if (slope_calc != 0):
        
        val1 = (diff_w*eq1 - diff_x*eq2)/slope_calc
        val2 = (diff_y*eq2 - diff_z*eq1)/slope_calc
        
        cond1=val1 >= min([x1,x2]) and val1 <= max([x1,x2]) and val1 >= min([w1,w2]) and val1 <= max([w1,w2]) 
        cond2=val2 >= min([y1,y2]) and val2 <= max([y1,y2]) and val2 >= min([z1,z2]) and val2 <= max([z1,z2])
        
        if cond1 and cond2:
            return tuple([round(val1,2),round(val2,2)])
    
    
    else:
        if (x1 == w1 and y1 == z1) or (x1 == w2 and y1 == z2):
            return tuple([x1, y1])
        elif (x2 == w1 and y2 == z1) or (x2 == w2 and y2 == z2):
            return tuple([x2, y2])
            




