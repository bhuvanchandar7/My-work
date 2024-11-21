from datetime import datetime
def read_products(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        products={}
        for line in lines:
            details={}
            product_id=line.split(',')[0]
            name=line.split(',')[1]
            price=float(line.split(',')[2])
            details['name']=name
            details['price']=price
            products[product_id]=details
    return products

def read_sales(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        sales=[]
        for line in lines:
            sale={}
            sale['transaction_id']=line.split(',')[0]
            date=line.split(',')[1]
            date=date.split('-')
            date='/'.join(date)
            updated_date=datetime.strptime(date,'%d/%m/%Y')
            sale['date']=updated_date
            sale['product_id']=line.split(',')[2]
            sale['quantity']=int(line.split(',')[3])
            sale['discount']=float(line.split(',')[4])
            sales.append(sale)   
        return sales

def read_returns(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        returns=[]
        for line in lines:
            ret={}
            ret['transaction_id']=line.split(',')[0]
            date=line.split(',')[1].strip()
            date=date.split('-')
            date='/'.join(date)
            updated_date=datetime.strptime(date,'%Y/%m/%d')
            ret['date']=updated_date
            returns.append(ret)    
        return returns

def transactions_made(products, sales, returns):
        product_units_sold = {}
        product_revenue = {}
        product_discounts = {}
        
        for product_id in products.keys():
            product_units_sold[product_id] = 0
            product_revenue[product_id] = 0
            product_discounts[product_id] = 0
       
        for sale in sales:   
            if sale['transaction_id'] not in [return_entry['transaction_id'] for return_entry in returns]:
                product_id = sale['product_id']
                quantity = sale['quantity']
                discount = sale['discount']
                product_units_sold[product_id] += quantity
                product_revenue[product_id] += quantity*products[product_id]['price']
                product_discounts[product_id] += quantity*products[product_id]['price'] * discount
  
        return product_units_sold, product_revenue, product_discounts

if __name__ == "__main__":
        products_data = read_products("transactions_Products.csv")
        sales_data = read_sales("transactions_Sales.csv")
        returns_data = read_returns("transactions_Returns.csv")
    
        product_units_sold, product_revenue, product_discounts = transactions_made(products_data, sales_data, returns_data)
      
        num_sold=list(product_units_sold.values())
        top_3_units_sold=sorted(product_units_sold.values())[-3:][::-1]
        product_id=list(product_units_sold.keys())
        key_index=[]
        for i in top_3_units_sold:
            key_index.append(num_sold.index(i))
        list_id=[]
        for j in key_index:
            list_id.append(product_id[j])
        for i in range(3):
            product_name = products_data[list_id[i]]['name']
            units_sold=top_3_units_sold[i]
            print(f"{product_name:>20} {units_sold:>3}")
        print()        
        
        amounts=list(product_revenue.values())
        top_3_amounts_sold=sorted(product_revenue.values())[-3:][::-1]
        product_id=list(product_revenue.keys())
        key_index=[]
        for i in top_3_amounts_sold:
            key_index.append(amounts.index(i))
        list_id=[]
        for j in key_index:
            list_id.append(product_id[j])
        for i in range(3):
            product_name = products_data[list_id[i]]['name']
            units_sold=top_3_amounts_sold[i]-product_discounts[list_id[i]]
            print(f"{product_name:>20} ${units_sold:10,.2f}")       
        print()        
        
        print("+---+--------------------+---+-----------+------+-----------+")
        discounts=list(product_discounts.values())
        arranged_discounts=sorted(product_discounts.values())[::-1]
        product_id=list(product_units_sold.keys())
        key_index=[]
        for i in arranged_discounts:
            key_index.append(discounts.index(i))
        list_id=[]
        for j in key_index:
            list_id.append(product_id[j])  
        for product_id in list_id:
            units_sold = product_units_sold[product_id]
            revenue = product_revenue[product_id]-product_discounts[product_id]
            discount_amount = product_discounts[product_id]
            avg_discount = product_discounts[product_id]/product_revenue[product_id]*100
            formatted_product_id = f"{product_id:3}"
            formatted_product_name = f"{products_data[product_id]['name']:20}"
            formatted_units_sold = f"{units_sold:3}"
            formatted_revenue = "${:10,.2f}".format(revenue)
            formatted_avg_discount = "{:05.2f}%".format(avg_discount)
            formatted_discount_amount = "${:10,.2f}".format(discount_amount)
            print(f"|{formatted_product_id}|{formatted_product_name}|{formatted_units_sold}|{formatted_revenue}|{formatted_avg_discount}|{formatted_discount_amount}|")
            print("+---+--------------------+---+-----------+------+-----------+")    
        print()
            
        weekday_counts = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        count_sales = {weekday: 0 for weekday in weekday_counts.keys()}
        
        for sale in sales_data:
            weekday = sale['date'].weekday()
            count_sales[weekday] += 1        
        
        for weekday, count in count_sales.items():
            formatted_output = f"{weekday_counts[weekday]:9}:{count:3}"
            print(formatted_output)
        print()
        
        return_counts={}
        for returns in returns_data:
                transaction_id = returns['transaction_id']
                for sale in sales_data:
                    if transaction_id==sale['transaction_id']:
                        product_id=sale['product_id']
                        if product_id in return_counts:
                            return_counts[product_id] += 1
                        else:
                            return_counts[product_id] = 1       
        for product_id, return_count in return_counts.items():
            product_name = products_data.get(product_id).get('name')
            print(f"{product_id:3} {product_name:<20} {return_count:>3}")           
        print()
        
        with open("transactions_units.txt",'w') as file:
            for items in product_units_sold.items():
                i=[]
                for item in items:
                    item=str(item)
                    i.append(item)
                text=', '.join(i)
                file.write(text)
                file.write('\n')