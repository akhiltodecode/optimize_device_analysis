from optimize_device_analysis.cpu_metrics import CPUMetrics
from optimize_device_analysis.memory_metrics import MemoryMetrics
from optimize_device_analysis.network_metrics import NetworkMetrics

class WindowsMetrics(CPUMetrics, MemoryMetrics, NetworkMetrics):
    print(UnderConstruction, Meanwhile you can just call generic methods from cpu_metrics, memory_metrics, network_metrics')
    pass