from sqlalchemy import (
    Column,
    Integer,
    VARCHAR, ForeignKey,
)

from .meta import Base


class Order(Base):
    """
    Заказ
    """
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    doc_number = Column(VARCHAR(30), comment="Номер заказа")


class OrderItem(Base):
    """
    Детализация по заказу
    """
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer,  ForeignKey("orders.id"), comment='Заказ')
    product_name = Column(VARCHAR(30), comment="Название товара")
    amount = Column(Integer, comment="Количество товара")
    price = Column(Integer, comment="Цена товара")
