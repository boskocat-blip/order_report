from dataclasses import dataclass

@dataclass
class Order:
    """
    Dataklass som representerar en enskild order från CSV-filen.
    """
    order_id: str
    order_date: str
    customer_id: str
    region: str
    product_category: str
    quantity: int
    unit_price: float
    discount: float
    returned: bool

    @property
    def brutto_total(self) -> float:
        """Beräknar bruttovärdet för ordern."""
        return self.quantity * self.unit_price

    @property
    def net_total(self) -> float:
        """Beräknar rabatterat värde för ordern."""
        return self.brutto_total * (1.0 - self.discount)