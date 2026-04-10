import json
sales_data = []
user_total_values = {}
product_totals = {}

with open("data.txt","r") as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) == 4:
            user_name = data[0]
            product_name = data[1]
            amount = int(data[2])
            price = float(data[3])
            total_value = amount * price
            sales_data.append({
            "user_name": user_name,
            "product_name": product_name,
            "amount": amount,
            "total_value": total_value
            })    
            user_total_values[user_name] = user_total_values.get(user_name, 0) + total_value
            product_totals[product_name] = product_totals.get(product_name, 0) + amount
            
max_quantity = max(i ['amount'] for i in sales_data)
max_purchase_by_quantity_users = [u ['user_name'] for u in sales_data if u['amount'] == max_quantity]
max_total_value = max(user_total_values.values())
max_purchase_by_total_value_users = [user for user, total in user_total_values.items() if total == max_total_value]
avg_purchase_value = sum(sale['total_value'] for sale in sales_data) / len(sales_data)
avg_purchase_quantity = sum(sale['amount'] for sale in sales_data) / len(sales_data)
max_product_quantity = max(product_totals.values())
most_sold_products = [product for product, quantity in product_totals.items() if quantity == max_product_quantity]
               
sales_analyse_dict={    
    "max_purchase_by_quantity_users": max_purchase_by_quantity_users,
    "max_purchase_by_total_value_users": max_purchase_by_total_value_users,
    "average_purchase_value": avg_purchase_value,
    "average_purchase_quantity": avg_purchase_quantity,
    "most_sold_products": most_sold_products
    }                

with open("sales_analyse_dict.json", "w") as sales_analyse_file:
    json.dump(sales_analyse_dict, sales_analyse_file,indent=4)

