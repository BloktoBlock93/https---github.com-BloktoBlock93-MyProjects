# Owner of a sneaker shop wants know the best selling brand shoe for the past week.

# initialize sales dictionary for each shoe brand
sales = {"Jordan": 0, "Nike": 0, "New Balance": 0, "Asic": 0}

# Lets find out weekly sales
for day in range(1, 8):
    print("Enter sales for Day " + str(day) + ":")
    
    # get sales for each shoe brand from the user
    jordan_sales = int(input("Jordan sales: "))
    nike_sales = int(input("Nike sales: "))
    nb_sales = int(input("New Balance sales: "))
    asic_sales = int(input("Asic sales: "))
    
    # update sales dictionary with sales for each shoe brand for the current day
    sales["Jordan"] += jordan_sales
    sales["Nike"] += nike_sales
    sales["New Balance"] += nb_sales
    sales["Asic"] += asic_sales
    
# calculate and print the highest total sales for each shoe brand over the week
for brand, brand_sales in sales.items():
    print(brand + " total sales for the week: " + str(brand_sales))
    print(" highest daily sales: " + str(max(sales.values())))


     