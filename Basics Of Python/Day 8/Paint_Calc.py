import math
test_h = int(input("Enter Height of the wall : "))
test_w = int(input("Enter Width of the Wall : "))
coverage = 5
def paint_calc(height,width, cover):
    number_of_cans = (height*width)/cover
    print(f"You have to buy {math.ceil(number_of_cans)}")
paint_calc(height = test_h,width = test_w, cover = coverage)