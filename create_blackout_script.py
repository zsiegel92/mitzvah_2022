import os

num_group_one = 6
num_group_two = 3

cmds = [f"python read_g_form.py {i} {j}" for i in range(num_group_one) for j in range(num_group_two)]
cmd=" && ".join(cmds)
print(cmd)
os.system(cmd)

