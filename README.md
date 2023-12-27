# Computer Info Generator

![Python Version](https://img.shields.io/badge/python-3.12.svg)
![License](https://img.shields.io/github/license/akhiltodecode/optimize_device_analysis/)
![Package](https://img.shields.io/pypi/pyversions/optimize_device_analysis)

Optimize_device_analysis is a comprehensive solution for collecting and analyzing system performance metrics. 
This Python package provides a suite of functionalities to effortlessly gather data on CPU usage, memory allocation, 
and network activity, delivering detailed insights into the performance of your computer system. With the ability to represent 
this data through interactive graphs, the performance-package empowers users in performance testing and analysis-related projects. 
Whether you are fine-tuning your application, conducting system optimizations, or simply monitoring resource utilization,the package 
facilitates a seamless and intuitive experience, making it an invaluable tool for developers and system administrators alike. 
Another feature of the optimize_device_analysis is its ability to export the final analyzed data to a CSV file, 
making it ideal for discrete analysis and batch processing. Whether you are fine-tuning applications, 
conducting system optimizations, or performing real-time monitoring, empowers users with 
the versatility needed for efficient performance testing and analysis-related projects.

## Installation

```bash
pip install optimize_device_analysis

USAGE:

1. Create instances of the metrics classes:

   .. code-block:: python

      cpu_metrics = CPUMetrics()
      memory_metrics = MemoryMetrics()
      network_metrics = NetworkMetrics()

2. Use the methods to collect metrics:

   .. code-block:: python

      cpu_percent = cpu_metrics.get_cpu_percent()
      memory_percent = memory_metrics.get_virtual_memory_percent()
      bytes_sent, bytes_recv = network_metrics.get_network_io_counters()

   You can use these methods to collect metrics at any point in your code.

3. Plot the collected metrics:

   .. code-block:: python

      start_time = datetime.now()
      end_time = start_time + timedelta(minutes=5)
      interval = 5

      cpu_metrics.plot_cpu_usage(start_time, end_time, interval, export_csv=True)
      memory_metrics.plot_memory_usage(start_time, end_time, interval, export_csv=True)
      network_metrics.plot_network_activity(start_time, end_time, interval, export_csv=True)

----------------------------------or----------------------------------------------

1. Use the class name and call static methods:

   .. code-block:: python

      cpu_metrics = CPUMetrics.get_cpu_percent()
      memory_metrics = MemoryMetrics.get_virtual_memory_percent()
      network_metrics = NetworkMetrics.get_network_io_counters()

   You can use these methods to collect metrics at any point in your code.

2. Plot the collected metrics:

   .. code-block:: python
      #For Example the user wants to analyse the statistics for time period of 5 minutes, along with csv import:-
      from datetime import datetime, timedelta
      
      start_time = datetime.now()
      end_time = start_time + timedelta(minutes=5)
      interval = 5

      CPUMetrics.plot_cpu_usage(start_time, end_time, interval, export_csv=True)
      MemoryMetrics.plot_memory_usage(start_time, end_time, interval, export_csv=True)
      NetworkMetrics.plot_network_activity(start_time, end_time, interval, export_csv=True)


Sample Usage:
'Generating the stats for over 5 minutes on CPU, Memory and Network usage in an order'

from optimize_optimize_device_analysis.cpu_metrics import CPUMetrics
from optimize_optimize_device_analysis.memory_metrics import MemoryMetrics
from optimize_optimize_device_analysis.network_metrics import NetworkMetrics
from datetime import datetime, timedelta

cpu_metrics = CPUMetrics.get_cpu_percent()
memory_metrics = MemoryMetrics.get_virtual_memory_percent()
network_metrics = NetworkMetrics.get_network_io_counters()

start_time = datetime.now()
end_time = start_time + timedelta(minutes=5)
interval = 5
CPUMetrics.plot_cpu_usage(start_time, end_time, interval, export_csv=True)

start_time = datetime.now()
end_time = start_time + timedelta(minutes=5)
interval = 5
MemoryMetrics.plot_memory_usage(start_time, end_time, interval, export_csv=True)

start_time = datetime.now()
end_time = start_time + timedelta(minutes=5)
interval = 5
NetworkMetrics.plot_network_activity(start_time, end_time, interval, export_csv=True)

FEATURES:
Comprehensive Metrics: Collect detailed CPU, memory, and network performance metrics for insightful system analysis.
Dynamic Graphs: Visualize performance data through dynamic graphs using the powerful matplotlib library.
Versatile Application: Ideal for performance testing, optimization, real-time monitoring and importing data in diverse computing environments.

DEPENDENCIES:
psutil: Cross-platform library for accessing system details.
matplotlib: Package for advanced plotting techniques.

TEST-ENVIRONMENT: Python SDK - 3.12, Windows Platform - Windows 10 x64 OS