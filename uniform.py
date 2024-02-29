from random import uniform


current = round(uniform(2.3, 2.8), 2)
voltage = round(uniform(220.0, 230.0), 2)
rpm = round(uniform(300.0, 310.0), 2)
mpu = round(uniform(3.3, 3.8), 2)

concatenated_values = f"{current}/{voltage}/{rpm}/{mpu}"

print(concatenated_values)
print(type(concatenated_values))