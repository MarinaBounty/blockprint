import time
from .utils import fetch_latest_block
from .visualizer import generate_block_image

def run_blockprint():
    print("🔄 Получаем последний блок Ethereum...")
    block_data = fetch_latest_block()
    if block_data:
        print(f"✅ Блок #{block_data['number']} получен.")
        generate_block_image(block_data)
        print("🖼️ Изображение сгенерировано: blockprint_<blocknumber>.png")
    else:
        print("❌ Не удалось получить данные блока.")
