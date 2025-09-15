# Windows Setup Guide

## Bypass Windows Microsoft Account Setup

1. Press `Shift + F10` to open Command Prompt.
2. Type the following command and press Enter:
   ```cmd
   start ms-cxh:localonly


---

## Activate Windows and Office

1. Open **PowerShell**.
2. Run the following command:

   ```powershell
   irm https://get.activated.win | iex
   ```

---

## Update All Software

1. Open **Command Prompt** as Administrator.
2. Run the following commands:

   ```cmd
   winget upgrade
   winget upgrade --all
   ```

---

## Install Common Software

Run these commands in **Command Prompt** or **PowerShell**:

```powershell
winget install --id=Google.Chrome -e
winget install --id=7zip.7zip -e
```

---

## Flush DNS and Reset Network Stack

Run the following commands in **Command Prompt**:

```cmd
ipconfig /flushdns
netsh winsock reset
netsh int ip reset
```

---

## Install Development Tools

1. Download the development setup script (`dev-setup.ps1`).
2. Open **PowerShell** in the folder where the script is saved.
3. Run the following commands:

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   .\dev-setup.ps1
   ```


