import logging  # importa las herramientas para registrar eventos
from pathlib import Path  # permite construir la ubicacion del archivo

ruta_registro = Path(__file__).with_name("eventos.log")  # guarda el registro junto a este archivo

logger = logging.getLogger("SoftwareFJ")  # crea el registrador de la aplicación
logger.setLevel(logging.INFO)  # permite registrar la informacion y los errores
logger.propagate = False  # evita enviar los mensajes a otros registradores

if not logger.handlers:  # evita agregar el mismo manejador varias veces
    archivo = logging.FileHandler(ruta_registro, encoding="utf-8")  # permite abrir el archivo sin borrar lo anterior
    formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")  # incluye fecha, nivel y mensaje
    archivo.setFormatter(formato)  # aplica el formato
    logger.addHandler(archivo)  # conecta el registrador con el archivo