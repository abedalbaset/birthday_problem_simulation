
import random
random.seed(1)
import  copy 
import matplotlib.pyplot as plt


# Initialize variables 
founded_counter = 0
number_of_groups_to_generate = 100000


# Function to check if there two people have the same day birthday in the group 
def is_there_two_same_value_in_arr(grouparr):
    copy_arr = copy.deepcopy(grouparr)
    for cc in range(0,len(grouparr)-1):
        valcheck = copy_arr.pop(0)
        if(valcheck in copy_arr):
            return [True,valcheck]
            

    return [False,-1]


# Generate random people where each one have different day birthday 
def generate_group(numberingroup):
    group_arr = []
    for cc in range(0,numberingroup):
        group_arr.append(random.randint(1,360))
    return group_arr


# Generate # number of groups , will start by generate number of groups and each group have 2 people then increase gradually and collect results in array
# Then draw this results

all_ratios_arr = []
group_size_arr = [] 
for group_size_counter in range(2,80):

    founded_counter = 0
    for cc in range(0,number_of_groups_to_generate):
        group_arr = generate_group(group_size_counter)
        res = is_there_two_same_value_in_arr(group_arr)
        if(res[0]):
            founded_counter += 1

    ratiov = founded_counter/number_of_groups_to_generate
    all_ratios_arr.append(ratiov)
    group_size_arr.append(group_size_counter)



# Draw results 
plt.plot(group_size_arr,all_ratios_arr)
plt.grid()
plt.show()
    
