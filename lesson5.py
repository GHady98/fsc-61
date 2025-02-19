def main():
    salary = float(input("Salary: "))
    month = input("Month: ")
    
    savings_percent = float(input("Savings %: "))
    rent_percent = float(input("Rent %: "))
    electricity_percent = float(input("Electricity %: "))
    
    savings = (savings_percent / 100) * salary
    rent = (rent_percent / 100) * salary
    electricity = (electricity_percent / 100) * salary
    
    total_spent = savings + rent + electricity
    remaining = salary - total_spent
    
    yearly_rent = rent * 12
    yearly_electricity = electricity * 12
    
    salary_squared = salary ** 2
    
    extra_savings = 50
    savings_division = extra_savings / savings if savings > 0 else 0
    

    
    print(f"\n{month} Summary")
    print(f"Salary: ${salary:.2f}")
    print(f"Savings: ${savings:.2f}")
    print(f"Rent: ${rent:.2f}")
    print(f"Electricity: ${electricity:.2f}")
    print(f"Total Spent: ${total_spent:.2f}")
    print(f"Remaining: ${remaining:.2f}")
    print(f"Yearly Rent: ${yearly_rent:.2f}")
    print(f"Yearly Electricity: ${yearly_electricity:.2f}")
    print(f"Salary Squared: {salary_squared:.2f}")
    print(f"$50 divided by savings: {savings_division:.2f}")
    
if __name__ == "__main__":
    main()

