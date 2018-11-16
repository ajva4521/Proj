a = [10,2,5]

sum_of_list = a[0] + a[1] + a[2]
print(sum_of_list)

sum_of_list2 = 0
for i in a:
    sum_of_list2 += i

print(sum_of_list2)


div_of_list = a[0] * a[0]
for i in a:
    if i == 0:
        print("nulou nelze dělit")
    else:
        div_of_list /= i

print(div_of_list)


mul_of_list  = 1
for i in a:
    mul_of_list *= i

print(mul_of_list)


sub_of_list = a[0] + a[0]
for i in a:
    sub_of_list -= i
print(sub_of_list)    
