# STUN NAT Type Detection Script

This Python script uses the `pystun3` library to determine your NAT type by querying a public STUN server. This is useful for troubleshooting network issues related to NAT (Network Address Translation), especially for applications like VoIP, gaming, and peer-to-peer communication.

---

## Prerequisites

- **Windows 11** (or any OS with Python 3.11 installed)
- **Python 3.11** installed from [python.org](https://www.python.org/downloads/release/python-3110/)
  - The script has compatibility issues with Python 3.13+ due to how the `stun` package is implemented.
- `pystun3` Python package installed for Python 3.11

---

## Installation Steps

### 1. Install Python 3.11

Download and install Python 3.11 from the official source:

- https://www.python.org/downloads/release/python-3110/

Make sure to:

- Add Python to your system PATH during installation
- Or use the Python launcher `py` to specify Python version explicitly

### 2. Install the `pystun3` package

Open a new PowerShell or Command Prompt and run:

```powershell
py -3.11 -m pip install pystun3
