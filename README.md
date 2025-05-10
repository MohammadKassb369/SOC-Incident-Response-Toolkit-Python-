# SOC-Incident-Response-Toolkit-Python-
SOC Incident Response Toolkit (Python)

SOC_Triage_Toolkit_v1/
├── main.py                  → Entry point (menu + orchestrator)

├── modules/                 → Individual forensic modules

│   ├── system_info.py
│   ├── network_info.py
│   ├── process_info.py
│   ├── user_info.py
│   ├── services_info.py
│   ├── persistence_info.py
│   ├── yara_scanner.py
│   ├── file_hashing.py
│   ├── memory_capture.py
│   └── reporting.py

├── tools/                   → External tools (e.g. yara64.exe, winpmem.exe)
├── output/                  → Collected data
├── config/                  → Settings, IOC lists, yara rules
├── utils.py                 → Helper functions (zip, logger, etc.)
├── requirements.txt         → Python package dependencies
├── README.md                → Project documentation
└── LICENSE

| Library             | Purpose                           |
| ------------------- | --------------------------------- |
| `psutil`            | System, process, network info     |
| `platform`          | OS & hardware info                |
| `socket`            | Hostname, IP                      |
| `yara-python`       | YARA scanning                     |
| `pywin32`           | Windows event logs, WMI, registry |
| `colorama`          | Colored terminal output           |
| `shutil`, `zipfile` | File packaging                    |
| `argparse`          | Optional CLI support              |
