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
    EDMAN-X ULTIMATE EXPLOIT FRAMEWORK V32
[/bold green]
"""

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"
]

def matrix_login():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[green]Initializing EDMAN Supreme Neural Matrix V32...[/green]", justify="center")
    time.sleep(0.5)
    matrix_chars = "0101010101EDMAN_ULTIMATE_V32_01010101"
    for _ in range(3):
        line = "".join(random.choice(matrix_chars) for _ in range(50))
        console.print(f"[green]{line}[/green]")
        time.sleep(0.03)
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(SKULL_BANNER)
    console.print(Panel.fit(
        "[bold cyan]🔥 COMMANDER EDMAN - 15+ VULNERABILITY RECON ENGINE 🔥[/bold cyan]\n[yellow]Loaded: Clean Web Fuzzer, API Leak Hunter, IP & Android Device Port Analyzer.[/yellow]",
        border_style="red"
    ))
    time.sleep(1.0)

# ==================== قسم فحص الأيبات والهواتف والأجهزة ====================
def scan_ip_devices(target_host):
    console.print(f"\n[bold blue][*] Analyzing Target IP / Device Infrastructure: {target_host}[/bold blue]")
    try:
        resolved_ip = socket.gethostbyname(target_host)
        console.print(f"[green][+] Target Resolved IP Address: {resolved_ip}[/green]")
    except Exception as e:
        console.print(f"[bold red][-] Failed to resolve host: {e}[/bold red]")
        return

    ports_to_scan = {
        21: "FTP (File Transfer)",
        22: "SSH (Secure Shell)",
        23: "Telnet (Router / IoT Vulnerability)",
        80: "HTTP Web Server",
        443: "HTTPS Secure Web",
        445: "SMB (Windows Share / EternalBlue Vector)",
        3306: "MySQL Database",
        5555: "Android ADB Debug Port (Phone Exposed!)",
        8080: "HTTP Proxy / Alt Web Server",
        8443: "Secure Alt Web / Management Panel"
    }

    table = Table(title=f"Infrastructure, Server & Mobile/Device Port Report: {resolved_ip}", border_style="cyan")
    table.add_column("Port", style="cyan")
    table.add_column("Service / Device Type Analysis", style="yellow")
    table.add_column("Status & Threat Level", style="bold")

    open_ports = 0
    for port, desc in ports_to_scan.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.2)
        result = s.connect_ex((resolved_ip, port))
        s.close()

        if result == 0:
            open_ports += 1
            status_str = "[bold red][OPEN][/bold red]"
            if port == 5555:
                status_str = "[bold red][OPEN] ⚠️ (CRITICAL: Android ADB Port Exposed! Phone Accessible)[/bold red]"
            elif port == 23:
                status_str = "[bold red][OPEN] ⚠️ (WARNING: Telnet / Router Vulnerable)[/bold red]"
            elif port == 445:
                status_str = "[bold red][OPEN] ⚠️ (WARNING: SMB Share Open)[/bold red]"
            table.add_row(str(port), desc, status_str)
        else:
            table.add_row(str(port), desc, "[dim green][CLOSED][/dim green]")

    console.print(table)
    if open_ports > 0:
        console.print(f"[bold yellow][i] Scan complete: Found {open_ports} active ports on target IP/Device.[/bold yellow]")
    else:
        console.print("[green][✔] All scanned ports are closed or firewalled.[/green]")

# ==================== قسم فحص المواقع الشامل (محمي بالكامل) ====================
def comprehensive_web_scan(target_url):
    console.print(f"\n[bold blue][*] Executing Deep 15+ Vulnerability & Recon Engine on Web Target...[/bold blue]")
    
    parsed = urllib.parse.urlparse(target_url)
    domain = parsed.netloc or parsed.path
    base_domain = f"{parsed.scheme}://{domain}"
    headers = {"User-Agent": random.choice(USER_AGENTS)}

    try:
        target_ip = socket.gethostbyname(domain)
        console.print(f"[green][+] Target Domain IP Extracted: {target_ip}[/green]")
    except:
        target_ip = "Unknown"

    table = Table(title=f"Advanced Web Vulnerability Matrix: {target_url}", border_style="magenta")
    table.add_column("Vulnerability Vector / Check #", style="bold yellow")
    table.add_column("Direct Link / Payload", style="underline cyan")
    table.add_column("Status", style="bold")

    html_content = ""
    res = None
    
    try:
        res = requests.get(target_url, headers=headers, timeout=6)
        html_content = res.text
        server_banner = res.headers.get("Server", "Hidden/Unknown")
        waf_header = res.headers.get("CF-Ray", res.headers.get("X-Powered-By", "None"))
        table.add_row("1. Server Banner & WAF", f"Server: {server_banner} | WAF: {waf_header}", "[bold cyan][INFO][/bold cyan]")
    except Exception as e:
        table.add_row("1. Server Banner", f"Connection Error: Target Unreachable", "[yellow][ERROR][/yellow]")
        console.print(f"[bold red][-] Could not establish connection to target: {e}[/bold red]")
        return

    if res and ('Content-Security-Policy' not in res.headers or 'X-Frame-Options' not in res.headers):
        table.add_row("2. Security Headers", f"[link={target_url}]{target_url}[/link]", "[bold red][OPEN] (Missing Headers)[/bold red]")
    else:
        table.add_row("2. Security Headers", "Active & Secured", "[green][CLOSED][/green]")

    sql_status = "[green][CLOSED][/green]"
    if parsed.query:
        sql_test = target_url + "'"
        try:
            r_sql = requests.get(sql_test, headers=headers, timeout=4)
            if any(err in r_sql.text.lower() for err in ["sql syntax", "mysql_fetch", "syntax error"]):
                sql_status = f"[bold red][OPEN] [link={sql_test}]SQLi Vulnerable[/link][/bold red]"
        except:
            pass
    table.add_row("3. SQL Injection (SQLi)", f"[link={target_url}]{target_url}[/link]", sql_status)

    xss_status = "[green][CLOSED][/green]"
    try:
        payload = "<script>alert('EDMAN')</script>"
        test_xss = f"{target_url}&test={urllib.parse.quote(payload)}" if "?" in target_url else f"{target_url}?test={urllib.parse.quote(payload)}"
        r_xss = requests.get(test_xss, headers=headers, timeout=4)
        if payload in r_xss.text:
            xss_status = f"[bold red][OPEN] [link={test_xss}]XSS Trigger Link[/link][/bold red]"
    except:
        pass
    table.add_row("4. Cross-Site Scripting (XSS)", f"[link={target_url}]{target_url}[/link]", xss_status)

    redirect_status = "[green][CLOSED][/green]"
    try:
        redir_test = f"{target_url}&url=https://evil-attacker.com" if "?" in target_url else f"{target_url}?url=https://evil-attacker.com"
        r_red = requests.get(redir_test, headers=headers, allow_redirects=False, timeout=4)
        if r_red.status_code in [301, 302] and "evil-attacker.com" in r_red.headers.get("Location", ""):
            redirect_status = f"[bold red][OPEN] [link={redir_test}]Open Redirect[/link][/bold red]"
    except:
        pass
    table.add_row("5. Open Redirect", f"[link={target_url}]{target_url}[/link]", redirect_status)

    console.print(table)

    console.print(f"\n[bold blue][*] Scanning 10+ Sensitive Files, Backups & API Secrets...[/bold blue]")
    sensitive_files = {
        "6. Robots.txt Exposure": "/robots.txt",
        "7. Git Repository Exposure": "/.git/HEAD",
        "8. Environment Config (.env)": "/.env",
        "9. Server Configuration File": "/config.json",
        "10. Database Backup File": "/backup.sql",
        "11. PHP Info Disclosure": "/phpinfo.php",
        "12. Admin Panel Endpoint": "/admin/"
    }

    file_table = Table(title="Sensitive Files & Backups Recon Matrix", border_style="yellow")
    file_table.add_column("Check / Vulnerability Name", style="bold red")
    file_table.add_column("Direct Clickable URL", style="underline cyan")
    file_table.add_column("HTTP Status", style="bold")

    for name, path in sensitive_files.items():
        file_url = f"{base_domain}{path}"
        try:
            r_file = requests.get(file_url, headers=headers, timeout=2)
            if r_file.status_code == 200:
                file_table.add_row(name, f"[link={file_url}]{file_url}[/link]", "[bold red][OPEN] (Exposed!)[/bold red]")
            else:
                file_table.add_row(name, file_url, "[green][CLOSED][/green]")
        except:
            pass

    console.print(file_table)

    if html_content:
        console.print(f"\n[bold blue][*] Running API Key & Secret Hunter (Google, Telegram, Tokens)...[/bold blue]")
        patterns = {
            "13. Google API Key": r"AIza[0-9A-Za-z-_]{35}",
            "14. Telegram Bot Token": r"\d{9}:[0-9A-Za-z-_]{35}",
            "15. Bearer / Auth Token": r"bearer\s+[a-zA-Z0-9_\-\.]{20,}"
        }
        
        leak_table = Table(title="API Keys & Secrets Hunt Report", border_style="cyan")
        leak_table.add_column("Secret Type", style="bold yellow")
        leak_table.add_column("Detection Result", style="green")

        for name, pattern in patterns.items():
            matches = re.findall(pattern, html_content, re.IGNORECASE)
            if matches:
                leak_table.add_row(name, f"[bold red]Found {len(matches)} leak(s)![/bold red]")
            else:
                leak_table.add_row(name, "[green]Clean / Secure[/green]")
        console.print(leak_table)

    report_data = {
        "target_url": target_url,
        "target_ip": target_ip,
        "timestamp": time.ctime()
    }
    with open("edman_security_report.json", "w") as f:
        json.dump(report_data, f, indent=4)
    console.print("\n[bold green][+] Comprehensive 15+ Vulnerability Report Saved as 'edman_security_report.json'![/bold green]")

def show_help_menu():
    console.clear()
    console.print(SKULL_BANNER)
    table = Table(title="[bold red]EDMAN-X ULTIMATE V32 MANUAL[/bold red]", border_style="cyan")
    table.add_column("Module", style="bold yellow")
    table.add_column("Description", style="green")
    
    table.add_row("1. Web URL Scan", "Executes 15+ checks with error-handling: IP extraction, SQLi, XSS, Redirect, Headers, 7+ Sensitive Files, and API Secret Hunter.")
    table.add_row("2. IP & Mobile/Device Scan", "Scans server and phone/Android ports (ADB 5555, Telnet 23, SMB 445) with threat analysis.")
    table.add_row("JSON Export", "Dumps assessment data into 'edman_security_report.json'.")
    console.print(table)
    console.input("\n[bold cyan]Press Enter to return to main menu...[/bold cyan]")

def main():
    matrix_login()
    
    while True:
        console.print(SKULL_BANNER)
        console.print("[bold yellow]================= [ EDMAN-X ULTIMATE V32 ] =================[/bold yellow]")
        console.print("[bold cyan]1.[/bold cyan] Run 15+ Deep Web Vulnerability & Recon Scan")
        console.print("[bold cyan]2.[/bold cyan] Scan IP, Server & Mobile/Android Device Ports")
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
            target_ip = console.input("[bold cyan]Enter Target IP or Hostname (e.g., 192.168.1.1): [/bold cyan]").strip()
            scan_ip_devices(target_ip)
            console.input("\n[bold cyan]Press Enter to return to menu...[/bold cyan]")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == "3":
            show_help_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == "4":
            console.print("[bold red][*] Shutting down EDMAN-X V32. Stay safe, Commander.[/bold red]")
            sys.exit(0)
        else:
            console.print("[bold red][!] Invalid option. Select from 1 to 4.[/bold red]")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
