import os
import sys
import json
import time
import socket
import urllib.parse
import random
import re

try:
    import requests
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ImportError:
    print("[-] Initializing core modules...")
    os.system("pip install requests rich")
    import requests
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table

console = Console()

# شعار EDMAN الفخم الجديد حسب طلبك
EDMAN_BANNER = """
[bold cyan]
███████╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║
█████╗  ██║  ██║██╔████╔██║███████║██╔██╗ ██║
██╔══╝  ██║  ██║██║ ╚═╝ ██║██╔══██║██║╚██╗██║
███████╗██████╔╝██║     ██║██║  ██║██║ ╚██╗██║
╚══════╝╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
          [ SUPREME EXPLOIT FRAMEWORK V25 ]
[/bold cyan]
"""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
]

def matrix_login():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[green]Initializing EDMAN Supreme Neural Matrix V25...[/green]", justify="center")
    time.sleep(0.5)
    matrix_chars = "0101010101EDMAN_ULTIMATE_V25_01010101"
    for _ in range(3):
        line = "".join(random.choice(matrix_chars) for _ in range(50))
        console.print(f"[green]{line}[/green]")
        time.sleep(0.03)
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(EDMAN_BANNER)
    console.print(Panel.fit(
        "[bold cyan]🔥 COMMANDER EDMAN - SUPREME CYBER WEAPON V25 LOADED 🔥[/bold cyan]\n[yellow]All Modules Active: Clickable Vulnerability Links, Secret Hunter, Fuzzer & IP/Android Analyzer.[/yellow]",
        border_style="red"
    ))
    time.sleep(1.0)

# 1. كاشف مفاتيح الـ API والتسريبات البرمجية
def hunt_secrets_and_apis(target_url, html_content):
    console.print(f"\n[bold blue][*] Hunting for API Keys, Tokens & Sensitive Data Leaks...[/bold blue]")
    patterns = {
        "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
        "Telegram Bot Token": r"\d{9}:[0-9A-Za-z-_]{35}",
        "Authorization Token": r"bearer\s+[a-zA-Z0-9_\-\.]{20,}",
        "Private IP Leak": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    }

    table = Table(title="Secret & API Leak Detection Report", border_style="yellow")
    table.add_column("Leak Type / Pattern", style="bold red")
    table.add_column("Match Result / Status", style="green")

    found_leaks = 0
    for name, pattern in patterns.items():
        matches = re.findall(pattern, html_content, re.IGNORECASE)
        if matches:
            found_leaks += 1
            table.add_row(name, f"[bold red]Found {len(matches)} potential match(es)![/bold red]")
        else:
            table.add_row(name, "[green]Clean / Not Found[/green]")

    console.print(table)

# 2. محرك الفحص الخارق للمسارات المخفية (مع إرجاع روابط قابلة للضغط)
def directory_fuzzer(base_domain):
    console.print(f"\n[bold blue][*] Launching High-Speed Directory & Vulnerability Link Fuzzer...[/bold blue]")
    common_paths = [
        "admin", "administrator", "login", "dashboard", "cp", "panel", 
        "backup", "db", "config.json", ".env", "api/v1", "robots.txt", ".git/HEAD"
    ]

    table = Table(title=f"Exposed Endpoints & Direct Links: {base_domain}", border_style="cyan")
    table.add_column("Target Path / Vulnerability Link", style="yellow")
    table.add_column("Direct Clickable URL", style="underline cyan")
    table.add_column("HTTP Status", style="bold")

    exposed_paths = 0
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    for path in common_paths:
        url = f"{base_domain}/{path}"
        try:
            res = requests.get(url, headers=headers, timeout=2)
            if res.status_code == 200:
                exposed_paths += 1
                table.add_row(path, f"[link={url}]{url}[/link]", "[bold red][OPEN] (Status 200)[/bold red]")
            elif res.status_code == 403:
                table.add_row(path, f"[link={url}]{url}[/link]", "[yellow][PROTECTED] (Status 403)[/yellow]")
        except:
            pass

    console.print(table)
    if exposed_paths == 0:
        console.print("[green][✔] No vulnerable common directories exposed.[/green]")

# 3. فحص الأيبات والأجهزة والأندرويد (IP & Port Scanner)
def scan_ip_devices(target_host):
    console.print(f"\n[bold blue][*] Analyzing Target IP/Host Infrastructure: {target_host}[/bold blue]")
    try:
        resolved_ip = socket.gethostbyname(target_host)
        console.print(f"[green][+] Resolved IP Address: {resolved_ip}[/green]")
    except Exception as e:
        console.print(f"[bold red][-] Failed to resolve host: {e}[/bold red]")
        return

    ports_to_scan = {
        21: "FTP (File Transfer)",
        22: "SSH (Secure Shell)",
        23: "Telnet (Router/IoT)",
        80: "HTTP Web Server",
        443: "HTTPS Secure Web",
        445: "SMB (Windows Share)",
        3306: "MySQL Database",
        5555: "Android ADB Debug Port",
        8080: "HTTP Proxy / Alt Web"
    }

    table = Table(title=f"Infrastructure & Device Port Report: {resolved_ip}", border_style="cyan")
    table.add_column("Port", style="cyan")
    table.add_column("Service / Device Type", style="yellow")
    table.add_column("Status", style="bold")

    for port, desc in ports_to_scan.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.2)
        result = s.connect_ex((resolved_ip, port))
        s.close()

        if result == 0:
            status_str = "[bold red][OPEN][/bold red]"
            if port == 5555:
                status_str = "[bold red][OPEN] ⚠️ (Potential Android ADB Exposed!)[/bold red]"
            elif port == 23:
                status_str = "[bold red][OPEN] ⚠️ (Telnet / Router Vulnerable)[/bold red]"
            table.add_row(str(port), desc, status_str)
        else:
            table.add_row(str(port), desc, "[dim green][CLOSED][/dim green]")

    console.print(table)

# 4. فحص المواقع الشامل مع الروابط التفاعلية المباشرة
def comprehensive_web_scan(target_url):
    console.print(f"\n[bold blue][*] Executing Full Web, Recon & Vulnerability Assessment...[/bold blue]")
    
    parsed = urllib.parse.urlparse(target_url)
    domain = parsed.netloc or parsed.path
    base_domain = f"{parsed.scheme}://{domain}"
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    table = Table(title=f"Web Threat & Direct Links Report: {target_url}", border_style="magenta")
    table.add_column("Vulnerability / Check Vector", style="bold yellow")
    table.add_column("Direct Exploit / Payload Link", style="underline cyan")
    table.add_column("Status", style="bold")

    report_results = {}
    html_content = ""

    # Security Headers & Server Banner
    try:
        res = requests.get(target_url, headers=headers, timeout=5)
        html_content = res.text
        server_banner = res.headers.get("Server", "Unknown")
        table.add_row("Server Banner", f"Server: {server_banner}", "[bold cyan][INFO][/bold cyan]")

        if 'Content-Security-Policy' not in res.headers or 'X-Frame-Options' not in res.headers:
            table.add_row("Security Headers", f"[link={target_url}]{target_url}[/link]", "[bold red][OPEN] (Vulnerable Headers)[/bold red]")
        else:
            table.add_row("Security Headers", "Standard headers active", "[green][CLOSED][/green]")
    except:
        pass

    # SQL Injection link check
    sql_status = "[green][CLOSED][/green]"
    if parsed.query:
        sql_test_url = target_url + "'"
        try:
            r = requests.get(sql_test_url, headers=headers, timeout=4)
            if any(err in r.text.lower() for err in ["sql syntax", "mysql_fetch", "syntax error"]):
                sql_status = f"[bold red][OPEN] [link={sql_test_url}]Click to Test SQLi[/link][/bold red]"
        except:
            pass
    table.add_row("SQL Injection (SQLi)", f"[link={target_url}]{target_url}[/link]", sql_status)

    # Reflected XSS link check
    xss_status = "[green][CLOSED][/green]"
    try:
        payload = "<script>alert('EDMAN')</script>"
        test_u = f"{target_url}&test={urllib.parse.quote(payload)}" if "?" in target_url else f"{target_url}?test={urllib.parse.quote(payload)}"
        r = requests.get(test_u, headers=headers, timeout=4)
        if payload in r.text:
            xss_status = f"[bold red][OPEN] [link={test_u}]Click XSS Payload[/link][/bold red]"
    except:
        pass
    table.add_row("Cross-Site Scripting (XSS)", f"[link={target_url}]{target_url}[/link]", xss_status)

    console.print(table)

    if html_content:
        hunt_secrets_and_apis(target_url, html_content)
    
    directory_fuzzer(base_domain)

    # Save JSON Report
    report_data = {
        "target": target_url,
        "timestamp": time.ctime(),
        "vulnerabilities": report_results
    }
    with open("edman_security_report.json", "w") as f:
        json.dump(report_data, f, indent=4)
    console.print("\n[bold green][+] Ultimate Report successfully saved as 'edman_security_report.json' ![/bold green]")

def show_help_menu():
    console.clear()
    console.print(EDMAN_BANNER)
    table = Table(title="[bold red]EDMAN-X GOD-MODE V25 MANUAL[/bold red]", border_style="cyan")
    table.add_column("Module", style="bold yellow")
    table.add_column("Description & Capabilities", style="green")
    
    table.add_row("1. Web URL Scan", "Scans websites for XSS, SQLi, Headers, Secret Hunting, and outputs DIRECT CLICKABLE VULNERABILITY LINKS.")
    table.add_row("2. IP / Android Scan", "Scans IP/Hosts for core ports and Android ADB debug port 5555.")
    table.add_row("JSON Export", "Dumps full scan data into 'edman_security_report.json'.")
    console.print(table)
    console.input("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")

def main():
    matrix_login()
    
    while True:
        console.print(EDMAN_BANNER)
        console.print("[bold yellow]================= [ EDMAN-X GOD-MODE V25 ] =================[/bold yellow]")
        console.print("[bold cyan]1.[/bold cyan] Run Ultimate Web Scan (Vulnerabilities, Clickable Links, Secrets, Fuzzer)")
        console.print("[bold cyan]2.[/bold cyan] Scan IP / Host / Android Device Ports ([OPEN] / [CLOSED])")
        console.print("[bold cyan]3.[/bold cyan] Help & Exploit Manual")
        console.print("[bold cyan]4.[/bold cyan] Exit / Terminate")
        
        choice = console.input("\n[bold green]EDMAN-X > Select choice (1-4): [/bold green]").strip()
        
        if choice == "1":
            target = console.input("[bold cyan]Enter Target URL (e.g., https://example.com/page?id=1): [/bold cyan]").strip()
            if not target.startswith("http"):
                target = "https://" + target
            comprehensive_web_scan(target)
            console.input("\n[bold cyan]Press Enter to return to menu...[/bold cyan]")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == "2":
            target_ip = console.input("[bold cyan]Enter Target IP or Hostname (e.g., 192.168.1.1 or example.com): [/bold cyan]").strip()
            scan_ip_devices(target_ip)
            console.input("\n[bold cyan]Press Enter to return to menu...[/bold cyan]")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == "3":
            show_help_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == "4":
            console.print("[bold red][*] Shutting down EDMAN-X V25. Stay safe, Commander.[/bold red]")
            sys.exit(0)
        else:
            console.print("[bold red][!] Invalid option. Select from 1 to 4.[/bold red]")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
