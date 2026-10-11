weight=int(input("çəkini daxil et :"))
height=float(input("boyunu daxil et :"))
BMI=weight/height**2
if BMI<18.5:
    print("Underweight")
elif BMI <=24.9 and BMI >=18.5:
    print("Normal Weight ")
elif BMI >=25 and BMI <=29.9:
    print("Overweight")
else:
    print("Obese")
