# Сбор информации о графических процессорах

import GPUtil


def get_gpu_info():
    gpus = GPUtil.getGPUs()

    if gpus:
        gpu = gpus[0]
        gpu_name = gpu.name
        gpu_load = gpu.load * 100
        gpu_memory_total = f'{gpu.memoryTotal / 1024:.2f} GB'
        gpu_memory_used = f'{gpu.memoryUsed / 1024:.2f} GB'
        gpu_memory_free = f'{gpu.memoryFree / 1024:.2f} GB'

        return gpu_name, gpu_load, gpu_memory_total, gpu_memory_used, gpu_memory_free


gpu_info = get_gpu_info()

if gpu_info:
    gpu_name, gpu_load, gpu_memory_total, gpu_memory_used, gpu_memory_free = gpu_info

    print(f'Графический процессор: {gpu_name}')
    print(f'Загрузка: {gpu_load:.2f}%')
    print(f'Использовано памяти: {gpu_memory_used} / {gpu_memory_total}')
    print(f'Свободно памяти: {gpu_memory_free}')
else:
    print('Графический процессор не обнаружен')