
import socket
import threading
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(
    filename="scan_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

            if result == 0:
                status = "OPEN"
            else:
                status = "CLOSED"

            print(f"Port {port}: {status}")
            logging.info(f"{host}:{port} - {status}")

    except socket.timeout:
        print(f"Port {port}: TIMEOUT")
        logging.info(f"{host}:{port} - TIMEOUT")

    except OSError as error:
        print(f"Port {port}: ERROR - {error}")
        logging.error(f"{host}:{port} - ERROR - {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Multithreaded TCP Port Scanner"
    )

    parser.add_argument("host", help="Authorized target hostname or IP")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=1024)
    parser.add_argument("--timeout", type=float, default=0.5)
    parser.add_argument("--threads", type=int, default=50)

    args = parser.parse_args()

    if not (1 <= args.start <= args.end <= 65535):
        parser.error("Ports must be between 1 and 65535.")

    if args.timeout <= 0 or not (1 <= args.threads <= 200):
        parser.error("Timeout must be positive and threads 1-200.")

    try:
        target_ip = socket.gethostbyname(args.host)
        print(f"\nScanning {args.host} ({target_ip})")
        print(f"Port range: {args.start}-{args.end}\n")

        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            for port in range(args.start, args.end + 1):
                executor.submit(
                    scan_port, target_ip, port, args.timeout
                )

        print("\nScan completed. Results saved to scan_results.log")

    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")


if __name__ == "__main__":
    main()
