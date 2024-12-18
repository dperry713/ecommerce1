from app.models import Product, db

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def create_product(data):
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product

def update_product(product_id, data):
    product = get_product_by_id(product_id)
    if not product:
        return None
    for key, value in data.items():
        if hasattr(product, key):
            setattr(product, key, value)
    db.session.commit()
    return product

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return None
    db.session.delete(product)
    db.session.commit()
    return product
