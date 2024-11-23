class Product:
    def __init__(self, product_id, name, origin, destination, status):
        self.product_id = product_id
        self.name = name
        self.origin = origin
        self.destination = destination
        self.status = status

    def get_product_data(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'origin': self.origin,
            'destination': self.destination,
            'status': self.status
        }
