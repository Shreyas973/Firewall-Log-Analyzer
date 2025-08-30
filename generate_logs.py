import random
import time
import django
import os
from datetime import datetime

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fw_analyzer.settings")
django.setup()

from analyzer.models import LogEntry

actions = ["ALLOW", "DENY", "DROP"]
protocols = ["TCP", "UDP", "ICMP"]
ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3", "8.8.8.8"]

print("🔥 Starting log generator... (Press CTRL+C to stop)")

try:
    while True:
        action = random.choice(actions)
        protocol = random.choice(protocols)
        src_ip = random.choice(ips)
        dst_ip = random.choice(ips)
        dst_port = random.randint(1, 65535) if protocol in ["TCP", "UDP"] else None
        raw = f"{datetime.now()} {action} {protocol} {src_ip} -> {dst_ip}:{dst_port}"

        log = LogEntry.objects.create(
            timestamp=datetime.now(),
            action=action,
            protocol=protocol,
            src_ip=src_ip,
            dst_ip=dst_ip,
            dst_port=dst_port,
            raw=raw,
        )
        print(f"[+] Inserted log: {log}")

        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Log generator stopped.")
