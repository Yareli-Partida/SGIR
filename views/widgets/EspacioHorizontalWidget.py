from PySide6.QtWidgets import QSpacerItem, QSizePolicy

class EspacioHorizontalWidget(QSpacerItem):
    """
    Un Spacer Item pre-configurado para expandirse horizontalmente porque no quiero hacerlo cada vez que lo voy a usar.
    """

    def __init__(self):
        super().__init__(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)