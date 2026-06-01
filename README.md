# Port scanner
A local Python cybersecurity script designed to scan web addresses or IP numbers to find open ports ("digital doors"). Project #5 in my coding journey.

### Overview
As my fifth project—and my very first one focused on cybersecurity and networking—this script was born out of my passion for offensive security and elite red teaming. While my previous project (the File Organizer) focused on managing my computer's file system, this application dives into network communications and sockets. My primary goal was to build a functional tool that mimics the initial "spy phase" of an ethical hack to find accessible services running on a target server.

### How to Use It
Since this script runs locally on your computer, follow these simple steps to safely test it:

**Step 1: Save the Code**
- Make sure you save the script inside VS Code as `main.py` or `scanner.py`.

**Step 2: Run the Script**
- Open your terminal or VS Code PowerShell.
- Run the script by typing: `python main.py`

**Step 3: Enter the Target Host**
- The terminal will prompt you with a message: `Enter the target website or IP: `
- Type in a legal testing address like `scanme.nmap.org` and press Enter.
- Watch the live terminal logs display the open ports as it checks them one by one!

### Features
- **Dynamic Address Translation:** Automatically translates readable web addresses (like `scanme.nmap.org`) into the exact numerical IP address computers use.
- **Automated Port Looping:** Utilizes a loop to systematically scan a specific range of standard operational ports (from port 20 up to 85) without requiring manual inputs for each one.
- **Crash-Proof Scanning:** Uses specialized error handling to check if a connection succeeds or fails, ensuring the script keeps running smoothly instead of crashing on a closed port.
- **Custom Terminal UI:** Generates a clean, professional command-line banner using string formatting to make the scanning targets easy to read.

### What I Learned
- **Python Socket Module:** Learning how to use the built-in `socket` library to spawn network connections and talk to external servers over the internet.
- **The Concept of Sockets:** Understanding that a socket is like a digital telephone line that must be created, used to "knock" on a port, and then properly hung up using `.close()`.
- **Error Coding (`connect_ex`):** Figuring out how `connect_ex` operates under the hood by returning a standard error code of `0` for a successful open connection instead of throwing a giant red error message.
- **Network Timeouts:** Setting a custom `.settimeout(1.0)` limit so the script doesn't hang forever waiting for a response from protected or dead servers.
- **String Multiplication:** Using neat Python tricks like `"=" * 40` to quickly generate terminal boundaries without typing them out by hand.

### Status
- Completed
