import psutil
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time, csv

class MemoryMetrics:
    @staticmethod
    def get_virtual_memory_percent():
        return psutil.virtual_memory().percent

    @staticmethod
    def plot_memory_usage(start_time, end_time, interval,  export_csv=False):
        timestamps = []
        memory_data = []

        current_time = start_time
        while current_time <= end_time:
            timestamps.append(current_time)
            memory_percent = MemoryMetrics.get_virtual_memory_percent()
            memory_data.append(memory_percent)

            time.sleep(interval)
            current_time = datetime.now()

        plt.plot(timestamps, memory_data, label='Memory Usage')
        plt.title('Memory Usage Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Percentage')
        plt.legend()
        plt.show()

        # Export data to CSV if export_csv is True
        if export_csv:
            csv_filename = 'memory_metrics_data.csv'
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Timestamp', 'Memory Usage (%)'])
                for timestamp, memory_percent in zip(timestamps, memory_data):
                    csv_writer.writerow([timestamp, memory_percent])