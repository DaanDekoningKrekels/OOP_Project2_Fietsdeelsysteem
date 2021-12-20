import sys
from collections import deque

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QTreeView, QVBoxLayout, QApplication


class Vensters(QWidget):
    def __init__(self):
        super().__init__()
        self.tree = QTreeView(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.tree)
        self.model = QStandardItemModel()

    def importData(self, data, root=None):
        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        seen = {}  # List of  QStandardItem
        values = deque(data)
        while values:
            value = values.popleft()
            if value['unique_id'] == 1:
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value['unique_id']
            parent.appendRow([
                QStandardItem(value['short_name']),
                QStandardItem(value['height']),
                QStandardItem(value['weight'])
            ])
            seen[unique_id] = parent.child(parent.rowCount() - 1)

    def stationsTree(self):
        self.model.setHorizontalHeaderLabels(['ID', 'Naam', 'Aantal plaatsen', 'Lat, long', 'Fietsen'])
        self.tree.header().setDefaultSectionSize(180)
        self.tree.setModel(self.model)
        self.importData([{'unique_id': 1, 'parent_id': 0, 'short_name': '', 'height': ' ', 'weight': ' '}])
        self.tree.expandAll()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Vensters()
    view.setGeometry(300, 100, 600, 300)
    view.setWindowTitle('QTreeview Example')
    view.stationsTree()
    view.show()
    sys.exit(app.exec())
