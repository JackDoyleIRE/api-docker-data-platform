import json

class CustomerObject:
    columns = ['id', 'firstname', 'lastname', 'username','age','company_name',
               'company_department','outreaches']

    def __init__(self, customer):
        self.id = customer['id']
        self.firstname = customer['firstName']
        self.lastname = customer['lastName']
        self.username = customer['username']
        self.age = customer['age']
        self.company_name = customer['company']['name']
        self.company_department = customer['company']['department']
        self.outreaches = json.dumps(customer['outreaches'])

class PurchaseObject:
    columns = ['id', 'customer_username', 'net_price', 'gross_price']

    def __init__(self, purchase):
        self.id = purchase['id']
        self.customer_username = purchase['customer_username']
        self.net_price = purchase['prices']['net_price']
        self.gross_price = purchase['prices']['gross_price']
     
