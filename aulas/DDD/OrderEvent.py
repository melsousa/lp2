from ddd_domain_events import DomainEvents, DomainEventCallable
from enum import Enum

class OrderEvent(Enum):
    # Evento de domínio gerado para casos de uso de pedidos especiais
    HIGH_QUANTITY = 'HIGH_QUANTITY'
    HIGH_VOLUME_PRICE = 'HIGH_VOLUME_PRICE'