# CRIZ_GH0STR1D3R IT Network Tool

A terminal-based IT and network support tool for daily troubleshooting.

## 💻 How to Install on Another Linux PC

### 1. Install Git

Open Terminal and run:

```bash
sudo apt update
sudo apt install git
```

Check:

```bash
git --version
```

---

### 2. Install Python

```bash
sudo apt install python3
```

Check:

```bash
python3 --version
```

---

### 3. Install Required Network Tools

Install the tools used by CRIZ_GH0STR1D3R IT:

```bash
sudo apt install iproute2 iputils-ping xclip speedtest-cli
```

Check Speedtest:

```bash
speedtest-cli --version
```

---

## 📥 4. Download the Tool from GitHub

Go to the directory where you want to save the tool:

```bash
cd ~/Projects
```

If the `Projects` folder does not exist:

```bash
mkdir -p ~/Projects
cd ~/Projects
```

Clone the repository:

```bash
git clone https://github.com/Crizneil/nettool.git
```

Enter the project:

```bash
cd nettool
```

---

## ▶️ 5. Run the Tool

Run:

```bash
python3 main.py
```

The CRIZ_GH0STR1D3R IT menu should appear.

---

## ⚡ 6. Optional: Create `nettool` Command

To run the program by simply typing:

```bash
nettool
```

run:

```bash
chmod +x main.py
```

Then:

```bash
sudo ln -s "$(pwd)/main.py" /usr/local/bin/nettool
```

Now you can run:

```bash
nettool
```

from any directory.

Example:

```bash
cd ~
nettool
```

---

## 🔄 7. Update the Tool

When a newer version is available on GitHub:

Go to the project:

```bash
cd ~/Projects/nettool
```

Download the latest changes:

```bash
git pull
```

Then run:

```bash
nettool
```

---

## 🛠️ 8. If `nettool` Does Not Work

Run:

```bash
cd ~/Projects/nettool
```

Then:

```bash
chmod +x main.py
```

Create the command again:

```bash
sudo ln -s "$(pwd)/main.py" /usr/local/bin/nettool
```

Test:

```bash
nettool
```

---

## 📌 Quick Installation

For a PC that already has Git and Python:

```bash
sudo apt update
sudo apt install git python3 iproute2 iputils-ping xclip speedtest-cli
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/Crizneil/nettool.git
cd nettool
chmod +x main.py
sudo ln -s "$(pwd)/main.py" /usr/local/bin/nettool
nettool
```

---

## 🔐 Note

This tool is intended for authorized IT and network support use only.

Only troubleshoot networks, devices, and subscribers that you are authorized to manage.

---

**CRIZ_GH0STR1D3R_IT**

IT / Network Support Toolkit
