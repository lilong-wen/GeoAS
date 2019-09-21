# generate data using euklides
import os
import random
from random import shuffle

vocabulary_Captal_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"]

vocabulary_No_Captal_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"]

triangle_type_list = ["triangle", "right", "isosceles", "equilateral"]
quadrilateral_type_list = ["parallelogram", "rectangle", "square"]

num = 0

def triangle_gen():
    global num
    num += 1
    triangle_type = random.choices(triangle_type_list, k=1)
    triangle_type = triangle_type[0].__str__()
    
    #point_name_choice = random.choices(vocabulary_Captal_list, k=3)
    
    shuffle(vocabulary_Captal_list)
    point_name_choice = vocabulary_Captal_list[:3]
    
    point_name_1 = point_name_choice[0].__str__()
    point_name_2 = point_name_choice[1].__str__()
    point_name_3 = point_name_choice[2].__str__()
    
    line_length_1 = 5
    line_length_1 = line_length_1.__str__()
    line_length_2 = 6
    line_length_2 = line_length_2.__str__()
    line_length_3 = 6
    line_length_3 = line_length_3.__str__()
    
    degree_less_than_90_list = ["30", "45", "60"]
    degree_list = ["30", "45", "60", "90", "120", "150", "180"]
    
    first_line_degree = random.choices(degree_list)[0]
    first_line_degree = first_line_degree.__str__()
    
    
    first_angle_degree = random.choices(degree_less_than_90_list)[0]
    first_angle_degree = first_angle_degree.__str__()
    
    second_angle_degree = random.choices(degree_less_than_90_list)[0]
    second_angle_degree = first_angle_degree.__str__()
    

    #num = num.__str__()
    image_name = "img_" + str(num)
    
    print(triangle_type)
    print(type(triangle_type))
    with open('./data/img/' + image_name + '.euk', 'w') as tp:
        tp.write("box -10, -10, 10, 10" + "\n")
        tp.write(point_name_1 + " = point(0, 0)" + "\n")
        if triangle_type == 'triangle':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " " 
                + triangle_type + " " 
                + line_length_1 + ", " 
                + first_angle_degree + "deg" + ", "
                + second_angle_degree + "deg" + ", "
                + first_line_degree + "deg" + "\n")
        
        elif triangle_type == 'right':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " "
                + triangle_type + " "
                + line_length_1 + ", "
                + first_angle_degree + "deg" + ", "
                + first_line_degree + "deg" + "\n")
    
        elif triangle_type == 'isosceles':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " "
                + triangle_type + " "
                + line_length_1 + ", "
                + first_angle_degree + "deg" + ", "
                + first_line_degree + "deg" + "\n")
    
        elif triangle_type == 'equilateral':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " "
                + triangle_type + " "
                + line_length_1 + " "
                + "\n")
    
        tp.write("draw" + "\n")
        tp.write("  " + "(" 
            + point_name_1 + ". " 
            + point_name_2 + ". " 
            + point_name_3 + ")" + "\n")
        tp.write("end" + "\n")
    
        tp.write("label" + "\n")
        tp.write('  ' + point_name_1 + ' ' + '180deg font("Consolas-Bold-12")' + "\n")
        tp.write('  ' + point_name_2 + ' ' + '0deg font("Consolas-Bold-12")' + "\n")
        tp.write('  ' + point_name_3 + ' ' + '90deg font("Consolas-Bold-12")' + "\n")
        tp.write('end' + "\n")
    
    
    with open('./data/' + "lable.txt", 'a') as lb:
        if triangle_type == "triangle":
            if int(first_angle_degree) != 90:
               lb.write(image_name + ".png" + "| " + "1|" +"a " 
               + "right" + " triangle"
               + " with points " 
               + point_name_1 + " "
               + point_name_2 + " "
               + point_name_3 + " " + "and angle "
               + point_name_3 + point_name_1 + point_name_2 + " equals " + "90deg "
               + "\n")
            elif int(second_angle_degree) != 90:
               lb.write(image_name + ".png" + "| " + "1|" + "a " 
               + "right" + " triangle"
               + " with points " 
               + point_name_1 + " "
               + point_name_2 + " "
               + point_name_3 + " " + "and angle "
               + point_name_1 + point_name_2 + point_name_3 + " equals " + "90deg "
               + "\n")            
            else :
                lb.write(image_name + ".png" + "| " + "1|" + "a " + "normal "
                    + triangle_type 
                    + " with points " 
                    + point_name_1 + " "
                    + point_name_2 + " "
                    + point_name_3 + " " + "and angle "
                    + point_name_3 + point_name_1 + point_name_2 + " equals " + first_angle_degree + "deg "
                    + "and angle"
                    + point_name_1 + point_name_2 + point_name_3 + " equals " + second_angle_degree + "deg "
                    + "\n")
        if triangle_type == "right" or int(first_angle_degree) == 90 or int(second_angle_degree) == 90:
            lb.write(image_name + ".png" + "| " + "1|"  + "a " 
                + triangle_type + " triangle"
                + " with points " 
                + point_name_1 + " "
                + point_name_2 + " "
                + point_name_3 + " " + "angle "
                + point_name_3 + point_name_1 + point_name_2 + " equals " + "90deg "
                + "\n")
    
        if triangle_type == "isosceles":
            lb.write(image_name + ".png" + "| " + "1|" + "a " 
                + triangle_type + " triangle"
                + " with points " 
                + point_name_1 + " "
                + point_name_2 + " "
                + point_name_3 + " " 
                + "and"
                + "line " + point_name_3 + point_name_1 + " equals " 
                + "line " + point_name_3 + point_name_2 + " and " + "angle "
                + point_name_3 + point_name_1 + point_name_2 + " equals " + "angle "
                + point_name_3 + point_name_2 + point_name_1 + " equals " + first_angle_degree
                + "\n")
        if triangle_type == "equilateral":
            lb.write(image_name + ".png" + "| " + "1|" + "a " 
                + triangle_type + " triangle"
                + " with points " 
                + point_name_1 + " "
                + point_name_2 + " "
                + point_name_3 + " " 
                + "and "
                + "line " + point_name_3 + point_name_1 + " equals " 
                + "line " + point_name_3 + point_name_2 + " equals "
                + "line " + point_name_1 + point_name_2 + " and " + "angle "
                + point_name_3 + point_name_1 + point_name_2 + " equals " + "angle "
                + point_name_3 + point_name_2 + point_name_1 + " equals " + "angle "
                + point_name_1 + point_name_3 + point_name_2 + " equals " + "60deg"
                + "\n")        
    
    cmd1 = "./convert.sh " + "./data/img/" + image_name + ".euk"
    os.system(cmd1)

    cmd2 = "rm " + "./data/img/" + "*.euk"
    os.system(cmd2)

    cmd2 = "rm " + "./data/img/" + "*.eps"
    os.system(cmd2)

def quadrilateral_gen():
    global num
    num += 1
    quadrilateral_type = random.choices(quadrilateral_type_list, k=1)
    quadrilateral_type = quadrilateral_type[0].__str__()
    
    #point_name_choice = random.choices(vocabulary_Captal_list, k=3)
    
    shuffle(vocabulary_Captal_list)
    point_name_choice = vocabulary_Captal_list[:4]
    
    point_name_1 = point_name_choice[0].__str__()
    point_name_2 = point_name_choice[1].__str__()
    point_name_3 = point_name_choice[2].__str__()
    point_name_4 = point_name_choice[3].__str__()
    
    line_length_list = [4, 5, 6, 7, 8, 9]

    line_length_1 = random.choices(line_length_list)
    line_length_1 = line_length_1.__str__()
    line_length_2 = random.choices(line_length_list)
    line_length_2 = line_length_2.__str__()
    line_length_3 = 6
    line_length_3 = line_length_3.__str__()
    
    degree_less_than_90_list = ["30", "45", "60"]
    degree_list = ["30", "45", "60", "90", "120", "150", "180"]
    
    first_line_degree = random.choices(degree_list)[0]
    first_line_degree = first_line_degree.__str__()
    
    
    first_angle_degree = random.choices(degree_less_than_90_list)[0]
    first_angle_degree = first_angle_degree.__str__()
    
    second_angle_degree = random.choices(degree_less_than_90_list)[0]
    second_angle_degree = first_angle_degree.__str__()

    image_name = "img_" + str(num)
    
    print(quadrilateral_type)
    print(type(quadrilateral_type))
    with open('./data/img/' + image_name + '.euk', 'w') as tp:
        tp.write("box -10, -10, 10, 10" + "\n")
        tp.write(point_name_1 + " = point(0, 0)" + "\n")
        if quadrilateral_type == 'parallelogram':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " " 
                + point_name_4 + " "
                + quadrilateral_type + " " 
                + line_length_1 + ", " 
                + line_length_2 + ", "
                + first_angle_degree + "deg" + ", "                
                + first_line_degree + "deg" + "\n")
        
        elif quadrilateral_type == 'rectangle':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " "
                + quadrilateral_type + " "
                + line_length_1 + ", "
                + line_length_2 + ", "
                + first_line_degree + "deg" + "\n")
    
        elif quadrilateral_type == 'square':
            tp.write(point_name_1 + " " 
                + point_name_2 + " " 
                + point_name_3 + " "
                + quadrilateral_type + " "
                + line_length_1 + ", "
                + first_line_degree + "deg" + "\n")
    
        tp.write("draw" + "\n")
        tp.write("  " + "(" 
            + point_name_1 + ". " 
            + point_name_2 + ". " 
            + point_name_3 + ")" + "\n")
        tp.write("end" + "\n")
    
        tp.write("label" + "\n")
        tp.write('  ' + point_name_1 + ' ' + '180deg font("Consolas-Bold-12")' + "\n")
        tp.write('  ' + point_name_2 + ' ' + '0deg font("Consolas-Bold-12")' + "\n")
        tp.write('  ' + point_name_3 + ' ' + '90deg font("Consolas-Bold-12")' + "\n")
        tp.write('  ' + point_name_4 + ' ' + '90deg font("Consolas-Bold-12")' + "\n")
        tp.write('end' + "\n")
    
    
    with open('./data/' + "lable.txt", 'a') as lb:
        if quadrilateral_type == "parallelogram":
            if int(first_angle_degree) != 90:
               lb.write(image_name + ".png" + "| " + "1|" +"a " 
               + "right" + " triangle"
               + " with points " 
               + point_name_1 + " "
               + point_name_2 + " "
               + point_name_3 + " " + "and angle "
               + point_name_3 + point_name_1 + point_name_2 + " equals " + "90deg "
               + "\n")
            elif int(second_angle_degree) != 90:
               lb.write(image_name + ".png" + "| " + "1|" + "a " 
               + "right" + " triangle"
               + " with points " 
               + point_name_1 + " "
               + point_name_2 + " "
               + point_name_3 + " " + "and angle "
               + point_name_1 + point_name_2 + point_name_3 + " equals " + "90deg "
               + "\n")            
            else :
                lb.write(image_name + ".png" + "| " + "1|" + "a " + "normal "
                    + triangle_type 
                    + " with points " 
                    + point_name_1 + " "
                    + point_name_2 + " "
                    + point_name_3 + " " + "and angle "
                    + point_name_3 + point_name_1 + point_name_2 + " equals " + first_angle_degree + "deg "
                    + "and angle"
                    + point_name_1 + point_name_2 + point_name_3 + " equals " + second_angle_degree + "deg "
                    + "\n")
        if quadrilateral_type == "rectangle" or int(first_angle_degree) == 90 or int(second_angle_degree) == 90:
            lb.write(image_name + ".png" + "| " + "1|"  + "a " 
                + triangle_type + " triangle"
                + " with points " 
                + point_name_1 + " "
                + point_name_2 + " "
                + point_name_3 + " " + "angle "
                + point_name_3 + point_name_1 + point_name_2 + " equals " + "90deg "
                + "\n")
    
        if triangle_type == "isosceles":
            lb.write(image_name + ".png" + "| " + "1|" + "a " 
                + triangle_type + " triangle"
                + " with points " 
                + point_name_1 + " "
                + point_name_2 + " "
                + point_name_3 + " " 
                + "and"
                + "line " + point_name_3 + point_name_1 + " equals " 
                + "line " + point_name_3 + point_name_2 + " and " + "angle "
                + point_name_3 + point_name_1 + point_name_2 + " equals " + "angle "
                + point_name_3 + point_name_2 + point_name_1 + " equals " + first_angle_degree
                + "\n")
        if triangle_type == "equilateral":
            lb.write(image_name + ".png" + "| " + "1|" + "a " 
                + triangle_type + " triangle"
                + " with points " 
                + point_name_1 + " "
                + point_name_2 + " "
                + point_name_3 + " " 
                + "and "
                + "line " + point_name_3 + point_name_1 + " equals " 
                + "line " + point_name_3 + point_name_2 + " equals "
                + "line " + point_name_1 + point_name_2 + " and " + "angle "
                + point_name_3 + point_name_1 + point_name_2 + " equals " + "angle "
                + point_name_3 + point_name_2 + point_name_1 + " equals " + "angle "
                + point_name_1 + point_name_3 + point_name_2 + " equals " + "60deg"
                + "\n")           

if __name__ == '__main__':

    for i in range(100):
        triangle_gen()