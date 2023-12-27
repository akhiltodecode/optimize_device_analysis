import psutil
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time, csv

class NetworkMetrics:
    @staticmethod
    def get_network_io_counters():
        network_stats = psutil.net_io_counters()
        return network_stats.bytes_sent, network_stats.bytes_recv

    @staticmethod
    def plot_network_activity(start_time, end_time, interval,  export_csv=False):
        timestamps = []
        sent_data = []
        recv_data = []

        current_time = start_time
        while current_time <= end_time:
            timestamps.append(current_time)
            bytes_sent, bytes_recv = NetworkMetrics.get_network_io_counters()
            sent_data.append(bytes_sent)
            recv_data.append(bytes_recv)

            time.sleep(interval)
            current_time = datetime.now()

        plt.plot(timestamps, sent_data, label='Bytes Sent')
        plt.plot(timestamps, recv_data, label='Bytes Received')
        plt.title('Network Activity Over Time')
        plt.xlabel('Timestamp')
        plt.ylabel('Bytes')
        plt.legend()
        plt.show()

        # Export data to CSV if export_csv is True
        if export_csv:
            csv_filename = 'network_metrics_data.csv'
            with open(csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Timestamp', 'Bytes Sent', 'Bytes Received'])
                for timestamp, sent, recv in zip(timestamps, sent_data, recv_data):
                    csv_writer.writerow([timestamp, sent, recv])