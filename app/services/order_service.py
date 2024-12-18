from app.models import Order, db

def get_all_orders():
    return Order.query.all()

def get_order_by_id(order_id):
    return Order.query.get(order_id)

def create_order(data):
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return order

def delete_order(order_id):
    order = get_order_by_id(order_id)
    if not order:
        return None
    db.session.delete(order)
    db.session.commit()
    return order
