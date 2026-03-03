import platform
import subprocess
import sys
import threading
import time

# ==========================================
# CONFIGURATION AREA
# ==========================================
SERVER_GROUPS = {
    "1": {
        "name": "Iran Servers",
        "hosts": [
            "soft98.ir",
            "varzesh3.com",
            "aparat.com",
            "digikala.com"
        ]
    },
    "2": {
        "name": "Kharej Servers (Intl)",
        "hosts": [
            "google.com",
            "github.com",
            "cloudflare.com",
            "1.1.1.1"
        ]
    },
    "3": {
        "name": "Local Network",
        "hosts": [
            "127.0.0.1",
            "192.168.1.1"
        ]
    }
}

DEFAULT_PING_COUNT = 4

# ==========================================
# SYSTEM & UI UTILITIES
# ==========================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

    @staticmethod
    def disable():
        Colors.HEADER = ''
        Colors.BLUE = ''
        Colors.CYAN = ''
        Colors.GREEN = ''
        Colors.WARNING = ''
        Colors.FAIL = ''
        Colors.ENDC = ''
        Colors.BOLD = ''

if platform.system().lower() == 'windows' and platform.release() == '7':
    Colors.disable()

print_lock = threading.Lock()

def get_ping_cmd(host):
    """Returns the single ping command based on OS"""
    os_name = platform.system().lower()
    if 'windows' in os_name:
        # -n 1: count 1, -w 1000: timeout 1000ms
        return ['ping', '-n', '1', '-w', '1000', host]
    else:
        # -c 1: count 1, -W 1: timeout 1 second
        return ['ping', '-c', '1', '-W', '1', host]

def measure_ping(host, total_count, results):
    """
    Pings the host 'total_count' times individually.
    This allows us to count exactly how many succeeded (e.g., 2/4).
    """
    successful_pings = 0
    latencies = []
    
    # We send pings one by one to count success accurately without regex parsing
    for _ in range(total_count):
        cmd = get_ping_cmd(host)
        
        start_t = time.time()
        try:
            # Run ping command (suppress output)
            response = subprocess.run(
                cmd, 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            end_t = time.time()
            
            if response.returncode == 0:
                successful_pings += 1
                # Calculate duration in ms
                latencies.append((end_t - start_t) * 1000)
            else:
                # If failed, we don't record time
                pass
                
        except Exception:
            pass
            
    # Calculate stats
    avg_time = sum(latencies) / len(latencies) if latencies else 0
    is_fully_online = (successful_pings == total_count)
    
    # Store data for the final report
    data = {
        "host": host,
        "success": successful_pings,
        "total": total_count,
        "avg_ms": avg_time,
        "fully_online": is_fully_online
    }
    results.append(data)
    
    # Live feedback line
    with print_lock:
        if successful_pings > 0:
            print(f"  > Completed: {Colors.CYAN}{host:<20}{Colors.ENDC} Avg: {int(avg_time)}ms")
        else:
            print(f"  > Completed: {Colors.FAIL}{host:<20}{Colors.ENDC} (Unreachable)")

# ==========================================
# MAIN LOGIC
# ==========================================

def print_banner():
    # Clear screen command (works on most terminals)
    if platform.system().lower() == "windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)

    print(f"{Colors.HEADER}================================================={Colors.ENDC}")
    print(f"{Colors.BOLD}        ADVANCED SERVER MONITOR (PRO)            {Colors.ENDC}")
    print(f"{Colors.HEADER}================================================={Colors.ENDC}")

def main_loop():
    while True:
        print_banner()
        
        # 1. Select Groups
        print(f"{Colors.BOLD}Available Groups:{Colors.ENDC}")
        for key, val in SERVER_GROUPS.items():
            print(f"  [{Colors.CYAN}{key}{Colors.ENDC}] {val['name']}")
        
        print(f"\n{Colors.BLUE}[TIP] You can select multiple (e.g., '1,2' or '1 3'){Colors.ENDC}")
        selection_input = input(f"{Colors.WARNING}Enter group numbers (or 'q' to quit): {Colors.ENDC}").strip()
        
        if selection_input.lower() == 'q':
            print("Exiting...")
            sys.exit(0)

        # Parse Selection
        selected_keys = selection_input.replace(',', ' ').split()
        target_hosts = []
        group_names = []
        
        for key in selected_keys:
            if key in SERVER_GROUPS:
                target_hosts.extend(SERVER_GROUPS[key]['hosts'])
                group_names.append(SERVER_GROUPS[key]['name'])
        
        # Remove duplicates
        target_hosts = list(set(target_hosts))
        
        if not target_hosts:
            input(f"\n{Colors.FAIL}[!] No valid groups selected. Press Enter to try again...{Colors.ENDC}")
            continue

        # 2. Select Count
        print(f"\nSelected Groups: {Colors.BOLD}{', '.join(group_names)}{Colors.ENDC}")
        count_input = input(f"{Colors.WARNING}Ping retry count (default {DEFAULT_PING_COUNT}): {Colors.ENDC}").strip()
        if count_input.isdigit() and int(count_input) > 0:
            count = int(count_input)
        else:
            count = DEFAULT_PING_COUNT
        
        print(f"\n{Colors.HEADER}--- Pinging {len(target_hosts)} Servers ({count} times each) ---{Colors.ENDC}")
        
        # 3. Execute
        threads = []
        results = []
        
        start_time = time.time()
        
        for host in target_hosts:
            t = threading.Thread(target=measure_ping, args=(host, count, results))
            t.daemon = True
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
            
        total_duration = time.time() - start_time
        
        # 4. Final Table
        print(f"\n{Colors.HEADER}================ FINAL REPORT ==================={Colors.ENDC}")
        print(f"{'SERVER/HOST':<25} | {'STATUS':<12} | {'LATENCY':<10}")
        print(f"--------------------------------------------------")
        
        for res in results:
            host_display = res['host']
            succ = res['success']
            tot = res['total']
            avg = res['avg_ms']
            
            # Determine Color and Status Text
            if succ == tot:
                status_color = Colors.GREEN
                status_text = "ONLINE"
            elif succ == 0:
                status_color = Colors.FAIL
                status_text = "OFFLINE"
            else:
                status_color = Colors.WARNING
                status_text = f"{succ}/{tot} UP"
            
            # Latency Text
            if succ > 0:
                latency_text = f"{int(avg)}ms"
                # Color code high latency (>200ms yellow, >500ms red)
                if avg > 500: latency_color = Colors.FAIL
                elif avg > 200: latency_color = Colors.WARNING
                else: latency_color = Colors.ENDC
            else:
                latency_text = "-"
                latency_color = Colors.ENDC

            print(f"{host_display:<25} | {status_color}{status_text:<12}{Colors.ENDC} | {latency_color}{latency_text:<10}{Colors.ENDC}")
            
        print(f"--------------------------------------------------")
        print(f"Completed in {total_duration:.2f} seconds.")
        
        input(f"\nPress {Colors.BOLD}Enter{Colors.ENDC} to return to menu...")

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}Force Exit.{Colors.ENDC}")
        sys.exit(0)
