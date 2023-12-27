import psutil
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time, csv

class CPUMetrics:
    @staticmethod
    def get_cpu_percent():
        return psutil.cpu_percent()

    @staticmethod
    def plot_cpu_usage(start_time, end_time, interval, export_csv=False):
        timestamps = []
        cpu_data = []

        current_time = start_time
        while current_time <= end_time:
            timestamps.append(current_time)
            cpu_percent = CPUMetrics.get_cpu_percent()
            cpu_data.append(cpu_percent)

            time.sleep(interval)
            current_time = datetime.now()

        plt.plot(timestamps, cpu_data, label='CPU Usage')
        plt.title('CPU Usage Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Percentage')
        plt.legend()
        plt.show()

        # Export data to CSV if export_csv is True
        if export_csv:
            csv_filename = 'cpu_metrics_data.csv'
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Timestamp', 'CPU Usage (%)'])
                for timestamp, cpu_percent in zip(timestamps, cpu_data):
                    csv_writer.writerow([timestamp, cpu_percent])
