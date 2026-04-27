def loan_check(age, income, credit):
    # Primary logic using compound conditional
    if age >= 18 and income > 15000 and credit >= 500:
        # Advanced nested categorization
        tier = "Gold" if credit >= 750 else "Silver" if credit >= 600 else "Bronze"
        return f"✅ Approved! Tier: {tier}"
    
    # Advanced logic to identify specific failure
    reasons = [
        "Age < 18" if age < 18 else "",
        "Income <= 15k" if income <= 15000 else "",
        "Credit < 500" if credit < 500 else ""
    ]
    return f"❌ Rejected: {' & '.join(filter(None, reasons))}"

# Quick Test
print(loan_check(25, 20000, 650))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

  

    reasons = [
        "Age < 18" if age < 18 else "",
        "Income <= 15k" if income <= 15000 else "",
        "Credit < 500" if credit < 500 else ""
    ]
    return f"❌ Rejected: {' & '.join(filter(None, reasons))}"
print(loan_check(25, 20000, 650))

