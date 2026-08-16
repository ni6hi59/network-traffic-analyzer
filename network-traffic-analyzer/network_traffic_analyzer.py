"""
Network Traffic Analyzer

A simple beginner project that counts packets by network protocol.
"""

import csv
from collections import Counter


def load_packets(filename):
    """Read packet records from a CSV file."""
    packets = []

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            packets.append(row)

    return packets


def count_protocols(packets):
    """Count how many packets belong to each protocol."""
    protocols = []

    for packet in packets:
        protocols.append(packet["protocol"])

    return Counter(protocols)


def display_results(protocol_counts):
    """Print the protocol counts in a friendly format."""
    print("Network Traffic Analysis")
    print("------------------------")

    total_packets = sum(protocol_counts.values())
    print(f"Total packets: {total_packets}")
    print()

    for protocol, count in sorted(protocol_counts.items()):
        print(f"{protocol}: {count} packet(s)")


def main():
    """Run the analyzer using the included sample data."""
    packets = load_packets("sample_traffic.csv")
    protocol_counts = count_protocols(packets)
    display_results(protocol_counts)


if __name__ == "__main__":
    main()