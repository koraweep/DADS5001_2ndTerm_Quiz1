from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QAbstractTableModel, QVariant, QModelIndex
import pandas as pd


class PandasModel(QAbstractTableModel):
	def __init__(self, df=pd.DataFrame(), parent=None):
		super().__init__(parent)
		self._df = df

	def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
		if role != Qt.ItemDataRole.DisplayRole:
			return QVariant()
		if orientation == Qt.Orientation.Horizontal:
			try:
				return self._df.columns.tolist()[section]
			except IndexError:
				return QVariant()
		elif orientation == Qt.Orientation.Vertical:
			try:
				return self._df.index.tolist()[section]
			except IndexError:
				return QVariant()

	def rowCount(self, parent=QModelIndex()):
		return self._df.shape[0]

	def columnCount(self, parent=QModelIndex()):
		return self._df.shape[1]

	def data(self, index, role=Qt.ItemDataRole.DisplayRole):
		if role != Qt.ItemDataRole.DisplayRole:
			return QVariant()
		if not index.isValid():
			return QVariant()
		return QVariant(str(self._df.iloc[index.row(), index.column()]))


