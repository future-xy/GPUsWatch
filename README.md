# The GPU's Watch

This repository contains a Python script for background monitoring using [Weights & Biases (wandb)](https://wandb.ai/). It is configured to run as a systemd service on Linux systems, ensuring it starts automatically on system boot and runs continuously in the background.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Setting Up the systemd Service](#setting-up-the-systemd-service)
- [Managing the Service](#managing-the-service)
- [Logging and Troubleshooting](#logging-and-troubleshooting)

## Prerequisites

- **Operating System:** Linux (systemd-based distributions like Ubuntu, Debian, CentOS, etc.)
- **Python:** 3.6 or higher
- **pip:** Python package manager
- **Weights & Biases Account:** [Sign up here](https://wandb.ai/site) if you don't have one.

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/future-xy/GPUsWatch
cd GPUsWatch
```

2. **Install the Required Python Packages**

```bash
pip install -r requirements.txt --user
```

## Configuration

1. **Login to Weights & Biases**

```bash
wandb login
```

Note: Prepare your Weights & Biases API key if you haven't logged in before. You can find it in your [W&B account settings](https://wandb.ai/settings).

2. **(Optional) Customize the monitoring script**

You can modify the script to monitor different GPU metrics or add more metrics. The script is located at `gpus_watch.py`.

## Setting Up the systemd Service

1. **Copy the systemd service file**

```bash
sudo cp systemd/monitor.service.example /etc/systemd/system/monitor.service
```

2. **(Optional) Modify the service file**

```bash
sudo vim /etc/systemd/system/monitor.service
```

Update the `User` and `WorkingDirectory` fields in the service file to match your system configuration.

3. **Reload systemd manager configuration**

```bash 
sudo systemctl daemon-reload
```

4. **Enable the service to start on boot**

```bash
sudo systemctl enable monitor.service
```

5. **Start the service**

```bash
sudo systemctl start monitor.service
```

6. **Check the service status**

```bash
sudo systemctl status monitor.service
```

## Managing the Service

- **Restart the service**

```bash
sudo systemctl restart monitor.service
```

- **Stop the service**

```bash
sudo systemctl stop monitor.service
```

- **Disable the service from starting on boot**

```bash
sudo systemctl disable monitor.service
```

## Logging and Troubleshooting

- **View the service logs**

```bash
sduo journalctl -u monitor.service -f
```