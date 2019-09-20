# generate data using euklides
import os
import random

vocabulary_Captal_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"]

vocabulary_No_Captal_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"]

triangle_type_list = ["triangle", "right", "isosceles", "equilateral"]

triangle_type = random.choices(triangle_type_list, k=1)
triangle_type = triangle_type[0].__str__()

point_name_choice = random.choices(vocabulary_Captal_list, k=3)

point_name_1 = point_name_choice[0].__str__()
point_name_2 = point_name_choice[1].__str__()
point_name_3 = point_name_choice[2].__str__()

line_length_1 = 6
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

num = 0
num = num.__str__()
image_name = "img_" + num

print(triangle_type)
print(type(triangle_type))
with open(image_name + '.euk', 'w') as tp:
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


with open("lable.txt", 'a') as lb:
    if triangle_type == "triangle":
        if int(first_angle_degree) != 90:
           lb.write("a " 
           + "right" + " triangle"
           + " with points " 
           + point_name_1 + " "
           + point_name_2 + " "
           + point_name_3 + " " + "and angle "
           + point_name_3 + point_name_1 + point_name_2 + " equals " + "90deg "
           + "\n")
        elif int(second_angle_degree) != 90:
           lb.write("a " 
           + "right" + " triangle"
           + " with points " 
           + point_name_1 + " "
           + point_name_2 + " "
           + point_name_3 + " " + "and angle "
           + point_name_1 + point_name_2 + point_name_3 + " equals " + "90deg "
           + "\n")            
        else :
            lb.write("a " + "normal "
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
        lb.write("a " 
            + triangle_type + " triangle"
            + " with points " 
            + point_name_1 + " "
            + point_name_2 + " "
            + point_name_3 + " " + "angle "
            + point_name_3 + point_name_1 + point_name_2 + " equals " + "90deg "
            + "\n")

    if triangle_type == "isosceles":
        lb.write("a " 
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
        lb.write("a " 
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

cmd = "./convert.sh " + image_name + ".euk"
os.system(cmd)