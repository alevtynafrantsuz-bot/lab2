a = int(input())
b = int(input())

if a > 40:
    regular_pay = 40 * b
    overtime_hours = a - 40
    overtime_pay = overtime_hours * (b * 1.5)
    total_pay = regular_pay + overtime_pay
else:
    total_pay = a * b

print(f"{total_pay:.2f}")