# Function that takes three parameters and returns a tuple of six values.
def mortgage_payments(principal, rate, amortization):

# Converting percentage to decimal.
    rq = rate / 100
    
 
# Calculating appropriate periodic interest rates since fixed-rate mortgages are quoted as semiannually compounded rates.
    r_monthly = (1 + rq / 2) ** (2/12) - 1
    r_semi_monthly = (1 + rq / 2) ** (2/24) - 1
    r_bi_weekly = (1 + rq / 2) ** (2/26) - 1
    r_weekly = (1 + rq / 2) ** (2/52) - 1
    
    # Calculating the number of payments based on payment periods
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52
    
    # Calculating present value of annuity
    def pva(r, n):
        return (1 - (1 + r) ** -n) / r if r > 0 else n  # Handle zero interest rate case
    
    # Calculating periodic payments using PVA formula, payment periods, and periodic interest rates.
    monthly_payment = principal / pva(r_monthly, n_monthly)
    semi_monthly_payment = principal / pva(r_semi_monthly, n_semi_monthly)
    bi_weekly_payment = principal / pva(r_bi_weekly, n_bi_weekly)
    weekly_payment = principal / pva(r_weekly, n_weekly)
    
# Calculating accelerated payments
    accelerated_bi_weekly_payment = monthly_payment / 2
    accelerated_weekly_payment = monthly_payment / 4

 # Rounding each payment amount to two decimal places to be presented as a dollar value
    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(accelerated_bi_weekly_payment, 2),
        round(accelerated_weekly_payment, 2)
    )

# Prompting user to enter principal, quoted rate, and amortization period in years using input () function
principal = float(input("What is the mortgage principal amount? "))
rate = float(input("What is the quoted annual interest rate (e.g., 4.85 for 4.85%)? "))
amortization = int(input("What is the amortization period in years? "))

# Calculating payments
payments = mortgage_payments(principal, rate, amortization)

# Displaying results after calculating payment amounts (rounded to the nearest penny). 
print(f"\nMonthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Accelerated Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Accelerated Weekly Payment: ${payments[5]:,.2f}")
