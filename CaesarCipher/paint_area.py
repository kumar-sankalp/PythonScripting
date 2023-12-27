import math
def paint_calc(height,width,cover):
    number_can=(height*width)/cover
    number_can=math.ceil(number_can)
    print(f"You'll need {number_can} can of paint")


test_h = int(input("enter height")) 
test_w = int(input("enter width")) 
coverage = int(input("enter coverage"))
paint_calc(height=test_h, width=test_w, cover=coverage)
