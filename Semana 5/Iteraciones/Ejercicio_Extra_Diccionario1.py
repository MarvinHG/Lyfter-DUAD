'''
1. Dada una lista de ventas con la siguiente información:
    - `date`
    - `customer_email`
    - `items`
- Y cada item teniendo la siguiente información:
    - `name`
    - `upc`
    - `unit_price`
- Cree un diccionario que guarde el total de ventas de cada UPC.
- Ejemplos:
    - Entrada:
        
        ```python
        sales = [
        	{
        		'date': '27/02/23',
        		'customer_email': 'joe@gmail.com',
        		'items': [
        			{
        				'name': 'Lava Lamp',
        				'upc': 'ITEM-453',
        				'unit_price': 65.76,
        			},
        			{
        				'name': 'Iron',
        				'upc': 'ITEM-324',
        				'unit_price': 32.45,
        			},
        			{
        				'name': 'Basketball',
        				'upc': 'ITEM-432',
        				'unit_price': 12.54,
        			},
        		],
        	},
        	{
        		'date': '27/02/23',
        		'customer_email': 'david@gmail.com',
        		'items': [
        			{
        				'name': 'Lava Lamp',
        				'upc': 'ITEM-453',
        				'unit_price': 65.76,
        			},
        			{
        				'name': 'Key Holder',
        				'upc': 'ITEM-23',
        				'unit_price': 5.42,
        			},
        		],
        	},
        	{
        		'date': '26/02/23',
        		'customer_email': 'amanda@gmail.com',
        		'items': [
        			{
        				'name': 'Key Holder',
        				'upc': 'ITEM-23',
        				'unit_price': 3.42,
        			},
        			{
        				'name': 'Basketball',
        				'upc': 'ITEM-432',
        				'unit_price': 17.54,
        			},
        		],
        	},
        ]
        ```
        
    - Salida:
        
        ```python
        result = {
        	'ITEM-453': 131.52,
        	'ITEM-324': 32.45,
        	'ITEM-432': 30.08,
        	'ITEM-23': 8.84,
        }
        ```
'''
# Create the list
sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name': 'Iron',      'upc': 'ITEM-324', 'unit_price': 32.45},
            {'name': 'Basketball','upc': 'ITEM-432', 'unit_price': 12.54},
        ],
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name': 'Key Holder','upc': 'ITEM-23',  'unit_price': 5.42},
        ],
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {'name': 'Key Holder','upc': 'ITEM-23',  'unit_price': 3.42},
            {'name': 'Basketball','upc': 'ITEM-432', 'unit_price': 17.54},
        ],
    },
]

#Create the dictionary
result = {}  

for sale in sales:                       # iterate each sale
    for item in sale['items']:           # iterate every item in the sale
        upc = item['upc']                # get the item's UPC code
        price = item['unit_price']       # get the item's unit price

        # add price to the running total for that UPC
        # if upc not yet in result, start from 0
        result[upc] = result.get(upc, 0) + price

# Print the result dictionary
print(result)

