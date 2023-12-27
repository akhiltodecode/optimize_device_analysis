Usage
=====

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