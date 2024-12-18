from app.models import Customer, db

def get_all_customers():
    return Customer.query.all()

def get_customer_by_id(customer_id):
    return Customer.query.get(customer_id)

def create_customer(data):
    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()
    return customer

def update_customer(customer_id, data):
    customer = get_customer_by_id(customer_id)
    if not customer:
        return None
    for key, value in data.items():
        if hasattr(customer, key):
            setattr(customer, key, value)
    db.session.commit()
    return customer

def delete_customer(customer_id):
    customer = get_customer_by_id(customer_id)
    if not customer:
        return None
    db.session.delete(customer)
    db.session.commit()
    return customer
