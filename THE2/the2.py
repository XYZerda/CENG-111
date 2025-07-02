inp = eval(input())

annual_income = eval(input())

income = inp["INCOME"] #takes values of "low, middle, high"

marital_status = inp["MARITAL_STATUS"] #takes values of "single, married, single parent"

child = inp["CHILD"] # çocuk yaşlarından oluşan bir liste verir

special_needs = inp["SPECIAL_NEEDS"] #takes values of "True, False"

elderly_care = inp["ELDERLY_CARE"] #takes values of "True, False"

taxpayer_duration = inp["TAXPAYER_DURATION"] #takes values of "new, regular, long term"

city_category = inp["CITY_CATEGORY"] #takes values of "urban, suburban, rural"

education = inp["EDUCATION"] #takes values of "True, False"

healthcare = inp["HEALTHCARE"] #takes values of "True, False"

green_initiatives = inp["GREEN_INITIATIVES"] #takes values of "True, False"

property_status = inp["PROPERTY_STATUS"] #takes values of "owns, rents"

if income == "low":
    base_tax_rate = annual_income * 0.1
elif income == "middle":
    base_tax_rate = annual_income * 0.2
elif income == "high":
    base_tax_rate = annual_income * 0.3

child_number = len(child) #çocuk sayısını verdi
below18 = list(filter(lambda x: x < 18, child))
LenBelow18 = len(below18)
if marital_status == "single":
    if elderly_care == True: # v1 stands for version one of tax rate, since we are going to make a lot of operations on base tax rate I defined the variables simply as v1, v2, v3 etc.
        v1 = base_tax_rate-800
    if elderly_care == False:
        v1 = base_tax_rate    
elif marital_status == "married":
    if special_needs and elderly_care == True:
        v1 = base_tax_rate-(500+300*child_number)-(200*LenBelow18)-1000-800
    if special_needs == True:
        if elderly_care == False:
            v1 = base_tax_rate-(500+300*child_number)-(200*LenBelow18)-1000
    elif special_needs == False:
        if elderly_care == True:
            v1 = base_tax_rate-(500+300*child_number)-(200*LenBelow18)-800
        else:
            v1 = base_tax_rate-(500+300*child_number)-(200*LenBelow18)
elif marital_status == "single_parent":
    if special_needs and elderly_care == True:
        v1 = base_tax_rate-(600*child_number)-(200*LenBelow18)-1000-800
    if special_needs == True:
        if elderly_care == False:
            v1 = base_tax_rate-(600*child_number)-(200*LenBelow18)-1000
    elif special_needs == False:
        if elderly_care == True:
            v1 = base_tax_rate-(600*child_number)-(200*LenBelow18)-800
        else:
            v1 = base_tax_rate-(600*child_number)-(200*LenBelow18)

if city_category == "urban":
    if education == True:
        if healthcare == True:
            if green_initiatives == True:
                v2 = v1-500-750-300
            elif green_initiatives == False:
                v2 = v1-500-750
        elif healthcare == False:
            if green_initiatives == True:
                v2 = v1-500-300
            elif green_initiatives == False:
                v2= v1-500
    elif education == False:
        if healthcare == True:
            if green_initiatives == True:
                v2 = v1-750-300
            elif green_initiatives == False:
                v2 = v1-750
        elif healthcare == False:
            if green_initiatives == True:
                v2 = v1-300
            elif green_initiatives == False:
                v2= v1
elif city_category == "suburban":
    if education == True:
        if healthcare == True:
            if green_initiatives == True:
                v2 = v1-200-500-750-300
            elif green_initiatives == False:
                v2 = v1-200-500-750
        elif healthcare == False:
            if green_initiatives == True:
                v2 = v1-200-500-300
            elif green_initiatives == False:
                v2= v1-200-500
    elif education == False:
        if healthcare == True:
            if green_initiatives == True:
                v2 = v1-200-750-300
            elif green_initiatives == False:
                v2 = v1-200-750
        elif healthcare == False:
            if green_initiatives == True:
                v2 = v1-200-300
            elif green_initiatives == False:
                v2= v1-200
elif city_category == "rural":
    if education == True:
        if healthcare == True:
            if green_initiatives == True:
                v2 = v1-400-500-750-300
            elif green_initiatives == False:
                v2 = v1-400-500-750
        elif healthcare == False:
            if green_initiatives == True:
                v2 = v1-400-500-300
            elif green_initiatives == False:
                v2= v1-400-500
    elif education == False:
        if healthcare == True:
            if green_initiatives == True:
                v2 = v1-400-750-300
            elif green_initiatives == False:
                v2 = v1-400-750
        elif healthcare == False:
            if green_initiatives == True:
                v2 = v1-400-300
            elif green_initiatives == False:
                v2= v1-400

if property_status == "owns":
    v3 = v2
elif property_status == "rents":
    v3 = v2-300

if taxpayer_duration == "new":
    v4 = v3
elif taxpayer_duration == "regular":
    v4 = v3*0.95
elif taxpayer_duration == "long_term":
    v4 = v3*0.90

if v4<0:
    final_tax_amount = 0.00
    print("%.2f" % final_tax_amount)
elif v4>=0:
    final_tax_amount = v4
    print("%.2f" % final_tax_amount)
