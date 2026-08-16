# Network Traffic Analyzer

This beginner Python project analyzes sample network traffic and counts the
number of packets that use each protocol.

The sample data includes three common protocols:

- **TCP**: Often used when data needs a reliable connection.
- **UDP**: Often used when speed is more important than guaranteed delivery.
- **ICMP**: Used for network messages such as `ping`.

## How to run it

From this project folder, run:

```bash
python network_traffic_analyzer.py
```

You should see:

```text
Network Traffic Analysis
------------------------
Total packets: 10

ICMP: 3 packet(s)
TCP: 4 packet(s)
UDP: 3 packet(s)
```

## How it works

1. `load_packets()` opens `sample_traffic.csv` and reads each row.
2. `count_protocols()` looks at the `protocol` column and counts each value.
3. `display_results()` prints the total number of packets and each protocol count.
4. `main()` connects these steps together.

The `Counter` class from Python's built-in `collections` module makes counting
repeated values easy. No extra packages are needed.

## Try changing the project

Open `sample_traffic.csv` and add another row. For example:

```text
11,192.168.1.19,192.168.1.20,TCP
```

Run the program again and notice that the TCP count increases by one.