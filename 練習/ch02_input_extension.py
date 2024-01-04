salary = int(input("請輸入薪資金額： ") )
bonus = int(input("\n請輸入工作獎金： ") )
overtime_pay = int(input("\n請輸入加班費： ") )

monthly_salary = salary + bonus + overtime_pay

print("本月實領金額為： " + str(monthly_salary) )