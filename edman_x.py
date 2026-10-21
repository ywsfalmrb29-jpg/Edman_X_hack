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

SKULL_BANNER = """
[bold green]
       .---.
      /     \\
     | () () |
      \\  _  /
      -'---'-
    EDMAN-X GOD-MODE MAX V20 (ULTIMATE)
[/bold green]
"""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
]

def matrix_login():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[green]Initializing EDMAN Supreme Neural Matrix V20...[/green]", justify="center")
    time.sleep(0.5)
    matrix_chars = "0101010101EDMAN_ULTIMATE_GODMODE01010101"
    for _ in range(3):
        line = "".join(random.choice(matrix_chars) for _ in range(50))
        console.print(f"[green]{line}[/green]")
        time.sleep(0.03)
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(SKULL_BANNER)
    console.print(Panel.fit(
        "[bold cyan]🔥 COMMANDER EDMAN - SUPREME CYBER WEAPON V20 LOADED 🔥[/bold cyan]\n[yellow]Modules Active: Web Scanners, Secret Hunter, Fuzzer, CVE Matcher & IP/Android Analyzer.[/yellow]",
        border_style="red"
    ))
    time.sleep(1.0)

# 1. كاشف مفاتيح الـ API والتسريبات البرمجية (Secret & API Key Hunter)
def hunt_secrets_and_apis(target_url, html_content):
    console.print(f"\n[bold blue][*] Hunting for API Keys, Tokens & Sensitive Data Leaks...[/bold blue]")
    
    # تعبيرات نمطية (Regex) للبحث عن المفاتيح والتوكنات الحساسة
    patterns = {
        "Google API Key": r"AIza[0-9A-Za-z-_]{35}",
        "Telegram Bot Token": r"\d{9}:[0-9A-Za-z-_]{35}",
        "Authorization / Bearer Token": r"bearer\s+[a-zA-Z0-9_\-\.]{20,}",
        "Private IP Leak": r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
        "Generic API/Secret Keyword": r"(api_key|secret_key|access_token|password|auth_token)\s*[:=]\s*['\"'][a-zA-Z0-9_\-]+['\"']"
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
    if found_leaks > 0:
        console.print(f"[bold red]⚠️ Alert: Found {found_leaks} potential sensitive data leaks in source code![/bold red]")
    else:
        console.print("[green][✔] No obvious API keys or hardcoded secrets detected in source.[/green]")

# 2. محرك الفحص الخارق للمسارات المخفية (High-Speed Directory Fuzzer)
def directory_fuzzer(base_domain):
    console.print(f"\n[bold blue][*] Launching High-Speed Directory & Admin Panel Fuzzer...[/bold blue]")
    common_paths = [
        "admin", "administrator", "login", "dashboard", "cp", "panel", 
        "backup", "db", "config.json", ".env", "api/v1", "server-status", "wp-login.php"
    ]

    table = Table(title=f"Directory Fuzzing Results: {base_domain}", border_style="cyan")
    table.add_column("Path / Endpoint", style="yellow")
    table.add_column("HTTP Status", style="bold")

    exposed_paths = 0
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    for path in common_paths:
        url = f"{base_domain}/{path}"
        try:
            res = requests.get(url, headers=headers, timeout=2)
            if res.status_code == 200:
                exposed_paths += 1
                table.add_row(url, "[bold red][OPEN] (Status 200)[/bold red]")
            elif res.status_code == 403:
                table.add_row(url, "[yellow][PROTECTED] (Status 403)[/yellow]")
        except:
            pass

    console.print(table)
    if exposed_paths == 0:
        console.print("[green][✔] No vulnerable common directories exposed.[/green]")

# 3. محرك فحص الأيبات والأجهزة والأندرويد (IP & Port Scanner)
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

    open_ports_count = 0
    for port, desc in ports_to_scan.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.2)
        result = s.connect_ex((resolved_ip, port))
        s.close()

        if result == 0:
            open_ports_count += 1
            status_str = "[bold red][OPEN][/bold red]"
            if port == 5555:
                status_str = "[bold red][OPEN] ⚠️ (Potential Android ADB Exposed!)[/bold red]"
            elif port == 23:
                status_str = "[bold red][OPEN] ⚠️ (Telnet / Router Vulnerable)[/bold red]"
            table.add_row(str(port), desc, status_str)
        else:
            table.add_row(str(port), desc, "[dim green][CLOSED][/dim green]")

    console.print(table)

# 4. فحص المواقع الشامل مع كشف الثغرات وإصدارات السيرفر (CVE Matcher Mock)
def comprehensive_web_scan(target_url):
    console.print(f"\n[bold blue][*] Executing Full Web, CVE Recon & Vulnerability Assessment...[/bold blue]")
    
    parsed = urllib.parse.urlparse(target_url)
    domain = parsed.netloc or parsed.path
    base_domain = f"{parsed.scheme}://{domain}"
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    table = Table(title=f"Web Threat & CVE Report: {target_url}", border_style="magenta")
    table.add_column("Vulnerability / Check Vector", style="bold yellow")
    table.add_column("Description", style="cyan")
    table.add_column("Status", style="bold")

    report_results = {}
    html_content = ""

    # Security Headers & Server Banner (CVE check simulation)
    try:
        res = requests.get(target_url, headers=headers, timeout=5)
        html_content = res.text
        server_banner = res.headers.get("Server", "Unknown")
        
        table.add_row("Server Banner (CVE)", f"Detected Server: {server_banner}", "[bold cyan][INFO][/bold cyan]")

        if 'Content-Security-Policy' not in res.headers or 'X-Frame-Options' not in res.headers:
            table.add_row("Security Headers", "Missing vital protection headers", "[bold red][OPEN] (Vulnerable)[/bold red]")
            report_results["security_headers"] = "OPEN"
        else:
            table.add_row("Security Headers", "Standard headers active", "[green][CLOSED][/green]")
            report_results["security_headers"] = "CLOSED"
    except Exception as e:
        table.add_row("Security Headers", f"Connection error: {e}", "[yellow][ERROR][/yellow]")

    # SQL Injection
    sql_status = "[green][CLOSED][/green]"
    sql_val = "CLOSED"
    if parsed.query:
        for p in ["'", "\""]:
            try:
                r = requests.get(target_url + p, headers=headers, timeout=4)
                if any(err in r.text.lower() for err in ["sql syntax", "mysql_fetch", "syntax error", "sqlite3"]):
                    sql_status = "[bold red][OPEN] (Exploitable SQLi)[/bold red]"
                    sql_val = "OPEN"
                    break
            except:
                pass
    table.add_row("SQL Injection (SQLi)", "Database parameter manipulation", sql_status)
    report_results["sqli"] = sql_val

    # Reflected XSS
    xss_status = "[green][CLOSED][/green]"
    xss_val = "CLOSED"
    try:
        payload = "<script>alert('EDMAN')</script>"
        test_u = f"{target_url}&test={urllib.parse.quote(payload)}" if "?" in target_url else f"{target_url}?test={urllib.parse.quote(payload)}"
        r = requests.get(test_u, headers=headers, timeout=4)
        if payload in r.text:
            xss_status = "[bold red][OPEN] (Reflected XSS)[/bold red]"
            xss_val = "OPEN"
    except:
        pass
    table.add_row("Cross-Site Scripting (XSS)", "Unsanitized input reflection", xss_status)
    report_results["xss"] = xss_val

    # Open Redirect
    redirect_status = "[green][CLOSED][/green]"
    try:
        redirect_test = f"{target_url}&url=https://evil-attacker.com" if "?" in target_url else f"{target_url}?url=https://evil-attacker.com"
        r_red = requests.get(redirect_test, headers=headers, allow_redirects=False, timeout=4)
        if r_red.status_code in [301, 302, 303] and "evil-attacker.com" in r_red.headers.get("Location", ""):
            redirect_status = "[bold red][OPEN] (Open Redirect Vulnerable)[/bold red]"
    except:
        pass
    table.add_row("Open Redirect", "Unvalidated external redirection", redirect_status)

    # Sensitive Files (.git & robots.txt)
    try:
        r_file = requests.get(base_domain + "/robots.txt", headers=headers, timeout=3)
        r_git = requests.get(base_domain + "/.git/HEAD", headers=headers, timeout=3)
        
        if r_git.status_code == 200:
            table.add_row("Sensitive Files / Git", "Exposed .git repository found!", "[bold red][OPEN] (Critical Git Exposure)[/bold red]")
        elif r_file.status_code == 200:
            table.add_row("Sensitive Files / Robots", "Exposed robots.txt found", "[bold red][OPEN] (Exposed)[/bold red]")
        else:
            table.add_row("Sensitive Files / Backup", "Hidden or protected", "[green][CLOSED][/green]")
    except:
        table.add_row("Sensitive Files", "Check failed", "[yellow][ERROR][/yellow]")

    console.print(table)

    # تشغيل كاشف المفاتيح والمسارات المخفية تلقائياً داخل الفحص الشامل
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
    console.print(SKULL_BANNER)
    table = Table(title="[bold red]EDMAN-X GOD-MODE MAX V20 MANUAL[/bold red]", border_style="cyan")
    table.add_column("Module", style="bold yellow")
    table.add_column("Description & Capabilities", style="green")
    
    table.add_row("1. Web URL Scan", "Scans websites for XSS, SQLi, Open Redirect, Headers, Git exposure, Secret/API Leak Hunting, and Directory Fuzzing.")
    table.add_row("2. IP / Device / Android Scan", "Scans IP/Hosts for core ports, routers (Telnet/SSH), and Android ADB debug port 5555.")
    table.add_row("JSON Export", "Dumps full scan data into 'edman_security_report.json'.")
    console.print(table)
    console.input("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")

def main():
    matrix_login()
    
    while True:
        console.print(SKULL_BANNER)
        console.print("[bold yellow]================= [ EDMAN-X GOD-MODE MAX V20 ] =================[/bold yellow]")
        console.print("[bold cyan]1.[/bold cyan] Run Ultimate Web Scan (Vulnerabilities, Secrets Hunter, Fuzzer, Recon)")
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
            console.print("[bold red][*] Shutting down EDMAN-X V20. Stay safe, Commander.[/bold red]")
            sys.exit(0)
        else:
            console.print("[bold red][!] Invalid option. Select from 1 to 4.[/bold red]")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
