import PySide6.QtCore as qtc


class MetricsTableModel(qtc.QAbstractTableModel):
    HEADER_MAP = {
        "Class": "Klasse",
        "Images": "Bilder",
        "Instances": "Instanzen",
        "Box-P": "Präzision",
        "Box-R": "Recall",
        "Box-F1": "F1-Score",
        "mAP50": "mAP50",
        "mAP50-95": "mAP50-95"
    }
    PERCENT_COLUMNS = {"Box-P", "Box-R", "Box-F1","mAP50", "mAP50-95" }

    def __init__(self, rows=[]):
        super().__init__()
        self.rows = rows
        self.columns = list(rows[0].keys()) if rows else []

    def rowCount(self, parent=None):
        return len(self.rows)

    def columnCount(self, parent=None):
        return len(self.columns)

    # def data(self, index:qtc.QModelIndex, role=qtc.Qt.DisplayRole):
    #     if not index.isValid():
    #         return None
        
    #     if role == qtc.Qt.DisplayRole:
    #         row = self.rows[index.row()]
    #         col = self.columns[index.column()]
    #         return str(row.get(col, ""))
    #     return None

    def data(self, index:qtc.QModelIndex, role=qtc.Qt.DisplayRole):
        if not index.isValid():
            return None
        
        if role == qtc.Qt.DisplayRole:
            row = self.rows[index.row()]
            col = self.columns[index.column()]
            value = row.get(col, "")
            if not value:
                return 0
            if col in self.PERCENT_COLUMNS:
                try:
                    return f"{value * 100:.2f} %"
                except (TypeError, ValueError):
                    return f"{0.00:.2f} %"

            return str(value)
        return None

    # def headerData(self, section, orientation, role):
    #     if role == qtc.Qt.DisplayRole and orientation == qtc.Qt.Horizontal and section < len(self.columns):
    #         return self.columns[section]
    #     return None
    def headerData(self, section, orientation, role):
        if role == qtc.Qt.DisplayRole and orientation == qtc.Qt.Horizontal:
            if section < len(self.columns):
                key = self.columns[section]
                return self.HEADER_MAP.get(key, key)
        return None
    
    def clear(self):
        self.beginResetModel()
        self.rows.clear()
        self.columns.clear()
        self.endResetModel()

    def setRows(self, rows=[]):
        self.beginResetModel()
        self.rows = rows
        self.columns = list(self.rows[0].keys()) if rows else []
        self.endResetModel()
