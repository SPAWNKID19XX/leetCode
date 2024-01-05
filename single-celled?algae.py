'''
В пробирку поместили зелёных и красных одноклеточных водорослей. 
В 1-й, 3-й, 5-й, 7-й и 9-й день каждая зелёная водоросль поглотила ровно по одной красной водоросли. 
А во 2-й, 4-й, 6-й, 8-й и 10-й день каждая красная водоросль поглотила ровно по одной зелёной водоросли. 
Спустя эти 10 дней в пробирке осталась лишь одна водоросль. Сколько красных водорослей было первоначально?

In a test tube, green and red single-celled algae were placed. 
On the 1st, 3rd, 5th, 7th, and 9th days, each green alga absorbed exactly one red alga. 
On the 2nd, 4th, 6th, 8th, and 10th days, each red alga absorbed exactly one green alga. 
After these 10 days, only one alga remained in the test tube. How many red algae were initially present?
'''
red = 1
green = 0
def red_count_tomorow():
    global red 
    red = red + green
    return red


def green_count_tomorow():
    global green
    green = green + red
    return green

for i in range(1, 11):
    if red == 1:
        green =1
    if i % 2 == 0:
        green_res = green_count_tomorow()
    else:
        red_res = red_count_tomorow()
    print("Day {} red:{} green:{}".format(i, red, green))
print(red_res)
