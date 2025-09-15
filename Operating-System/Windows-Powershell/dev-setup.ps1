# -------------------------------
# Dev Environment Setup Script
# -------------------------------
# Make sure winget is available

# -------------------------------
# Install VS Code
# -------------------------------
winget install --id Microsoft.VisualStudioCode -e --accept-source-agreements --accept-package-agreements

# -------------------------------
# Install Languages & Tools
# -------------------------------

# Python
winget install --id Python.Python.3 -e

# Node.js (LTS)
winget install --id OpenJS.NodeJS.LTS -e

# Java JDK (Temurin/OpenJDK)
winget install --id Eclipse.Adoptium.Temurin.17.JDK -e

# C/C++ Compiler (MinGW)
winget install --id MSYS2.MSYS2 -e

# Git (Required for most devs)
winget install --id Git.Git -e

# -------------------------------
# Optional: Install NVM for Node version management
# -------------------------------
Invoke-WebRequest https://raw.githubusercontent.com/coreybutler/nvm-windows/master/nvm-setup.exe -OutFile "$env:TEMP\nvm-setup.exe"
Start-Process "$env:TEMP\nvm-setup.exe" -Wait

# -------------------------------
# Install VS Code Extensions
# -------------------------------

# Helper function
function Install-VSCodeExtension($ext) {
    code --install-extension $ext
}

# Wait until VS Code CLI available
Start-Sleep -Seconds 10

# Python extension
Install-VSCodeExtension ms-python.python

# C/C++ extension
Install-VSCodeExtension ms-vscode.cpptools

# Java Extension Pack
Install-VSCodeExtension vscjava.vscode-java-pack

# Node.js Extension Pack
Install-VSCodeExtension eg2.vscode-npm-script

# GitLens
Install-VSCodeExtension eamodio.gitlens

# Code Runner (to run snippets)
Install-VSCodeExtension formulahendry.code-runner

# Prettier
Install-VSCodeExtension esbenp.prettier-vscode

# -------------------------------
# Final Message
# -------------------------------
Write-Host "✅ All development tools installed successfully!" -ForegroundColor Green
