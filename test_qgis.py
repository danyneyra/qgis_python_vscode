import qgis
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    Qgis
)

print("😺 QGIS cargado correctamente desde:", qgis.__file__)

# Inicializar QGIS en modo sin interfaz
QgsApplication.setPrefixPath("", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# ✔️ Obtener versión directamente del módulo qgis
print("🐾 Versión de QGIS:", Qgis.QGIS_DEV_VERSION)
print("🐾 Versión numérica:", Qgis.QGIS_VERSION_INT)

# Probar cargar una capa vacía de memoria
layer = QgsVectorLayer("Point?crs=EPSG:4326", "test_layer", "memory")
if not layer.isValid():
    print("😿 La capa no se pudo crear")
else:
    print("😺 Capa creada con éxito:", layer.name())

# Finalizar QGIS
qgs.exitQgis()
