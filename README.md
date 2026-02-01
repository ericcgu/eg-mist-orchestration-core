[![CI Status](https://github.com/ericcgu/juniper-mist-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/ericcgu/juniper-mist-ai/actions)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688.svg)](https://fastapi.tiangolo.com)
[![Redis](https://img.shields.io/badge/Redis-8.0-DC382D.svg)](https://redis.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Railway](https://img.shields.io/badge/Deployed%20on-Railway-0B0D0E.svg)](https://railway.app)

# 🚀 Juniper Mist Multi-Site Provisioning Service

> **Enterprise Network Automation at Scale** — A Masterclass in Domain-Driven Design & Intent-Based Networking for the AI-Driven Enterprise.

## 🌐 Live Demo

**[👉 Launch Interactive API Documentation](https://juniper-mist.up.railway.app/)**

---

## 📋 Table of Contents

- [Executive Summary](#-executive-summary)
- [The Biggest Wins of Juniper Mist AI](#-the-biggest-wins-of-juniper-mist-ai)
- [About This Approach](#-about-this-approach-the-distinguished-engineer-pattern)
- [Architecture Overview](#-architecture-overview)
- [The 13-Step Workflow](#-the-13-step-workflow)
- [Technical Highlights](#-technical-highlights)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)

---

## 💼 Executive Summary

This repository serves as a **curated masterclass** in deploying Zero-Touch, AI-driven networks at a global scale. It moves beyond simple scripting to demonstrate **Infrastructure as Software**, implementing high-level architectural patterns that bridge the gap between DevOps and Network Engineering.

By treating the network as a distributed software system, this framework bridges the gap between Network Design (The "What") and Software Architecture (The "How"). It moves beyond simple scripting to deliver a Full-Stack Automation Platform capable of orchestrating the entire lifecycle—from Day 0 Zero-Touch Provisioning (ZTP) logic to Day 1 Intent-Based Templates, and finally Day 2 AI-Driven Assurance.

### Network Lifecycle & Software Patterns

| Feature | Traditional Network Design | AI-Native Software Engineering (This Project) |
|---------|---------------------------|----------------------------------------------|
| **Topology** | Manual "Snowflake" Configs | Template-Based Inheritance (Class/Instance Pattern) |
| **IP Planning** | Static Excel Spreadsheets | Algorithmic Subnet Calculation (Factory Pattern) |
| **Provisioning** | Console Cables & CLI | Zero-Touch Provisioning (ZTP) (Supply Chain Integration) |
| **Validation** | Ping & Trace | Automated SLE Assurance (Observer Pattern) |
| **Architecture** | Monolithic Scripts | Domain-Driven Microservices (DDD) |

### Core Architectural Patterns Explored

- **Domain-Driven Design (DDD):** A rigorous decomposition of network logic into distinct domains (Wired, Wireless, WAN), ensuring separation of concerns and maintainable codebases.

- **Intent-Based Networking (IBN):** Implementation of "Late Binding" workflows where business intent (Templates) is defined abstractly and programmatically enforced upon physical infrastructure.

- **Algorithmic IP Planning:** Replacement of static spreadsheets with dynamic, conflict-free subnet calculation algorithms, enabling mathematical scale to 10,000+ sites.

- **Idempotency & State Management:** A robust orchestration engine (backed by Redis) that ensures deployment consistency, allowing workflows to be paused, resumed, or re-run without side effects.

> *This is not just a tool; it is a reference architecture for modern network teams seeking to adopt the reliability, agility, and intelligence of the Juniper Mist AI cloud.*

---

## 🏆 The Biggest Wins of Juniper Mist AI

Before diving into the specific architecture, it is critical to frame why Juniper Mist is the platform of choice for modern enterprises. Its "wins" are rooted in shifting from reactive management to **proactive AIOps**.

### Marvis Virtual Network Assistant (VNA)
The industry's first AI-driven network assistant. It uses Natural Language Processing (NLP) to answer questions like *"Why is Zoom bad in the boardroom?"* and automates troubleshooting by correlating data across WLAN, LAN, and WAN.

### Service Level Expectations (SLEs)
Instead of just monitoring "up/down" status, Mist measures the **user experience** (Time to Connect, Roaming health, Capacity). If users are happy, the network is green—regardless of what the SNMP traps say.

### Dynamic Packet Capture (dPCAP)
Mist automatically captures packets when an issue occurs and stores them in the cloud. This eliminates the need for engineers to fly to a site with a laptop to reproduce a transient bug.

### Microservices Cloud Architecture
Unlike legacy controllers that require massive downtime for upgrades, Mist updates weekly with **zero downtime**. This agility allows new features (like COVID contact tracing or new security protocols) to deploy instantly.

---

## 🎯 About This Approach: The "Distinguished Engineer" Pattern

This project distinguishes itself by treating network infrastructure not as a series of scripts, but as a **software product**.

### Domain-Driven Design (DDD)
The monolithic concept of "Networking" has been decomposed into distinct **Bounded Contexts**: Sites (Day 0), Wired, Wireless, and WAN (Day 1). This ensures that changes to the Wi-Fi policy logic do not break the SD-WAN routing logic, enabling safer, parallel development.

### Intent-Based Networking (IBN)
The architecture separates the **"What"** (Templates/Intent) from the **"Where"** (Sites/Instances). The "Late Binding" workflow is a pure implementation of IBN: you define the Intent (Policy) first, and then map that intent to the physical infrastructure, ensuring the network state always converges to the business requirement.

### Algorithmic Determinism
By replacing manual IP spreadsheets with an algorithmic `network_calculator`, human error is eliminated and mathematical referential integrity is ensured across thousands of subnets.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          FastAPI Application                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                    ORCHESTRATOR LAYER                                 │  │
│  │                                                                       │  │
│  │   POST /orchestrator/deploy-full-stack                               │  │
│  │   ├── Executes all 13 steps in dependency order                      │  │
│  │   ├── Idempotent (safe to retry)                                     │  │
│  │   └── Resumable (skips completed steps)                              │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                    │                                         │
│                    ┌───────────────┼───────────────┐                        │
│                    ▼               ▼               ▼                        │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                      DOMAIN ROUTERS (DDD)                             │  │
│  ├──────────────┬──────────────┬──────────────┬──────────────┬─────────┤  │
│  │    Sites     │  Inventory   │     WAN      │    Wired     │ Wireless│  │
│  │   (Day 0)    │   (Day 0)    │   (Day 1)    │   (Day 1)    │ (Day 1) │  │
│  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────┤  │
│  │ • Create     │ • Claim      │ • Apps       │ • Networks   │ • RF    │  │
│  │ • IP Plan    │ • Assign     │ • Hub Prof.  │ • Switch     │ • WLANs │  │
│  │ • Config     │ • Track      │ • Gateways   │   Templates  │ • PSKs  │  │
│  └──────────────┴──────────────┴──────────────┴──────────────┴─────────┘  │
│                                    │                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                       SERVICES LAYER                                  │  │
│  ├─────────────────────────────────┬────────────────────────────────────┤  │
│  │      NetworkCalculator          │         RedisStateStore            │  │
│  │  • Algorithmic IP planning      │  • Deployment state tracking       │  │
│  │  • Zone/Site subnet math        │  • Idempotency enforcement         │  │
│  │  • No spreadsheets required     │  • Resumable workflows             │  │
│  └─────────────────────────────────┴────────────────────────────────────┘  │
│                                    │                                         │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                      INFRASTRUCTURE                                   │  │
│  │                                                                       │  │
│  │   Redis 8 (State) ◄──► FastAPI ◄──► Juniper Mist Cloud API          │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 The 13-Step Workflow

The orchestrator executes these steps in precise dependency order:

```mermaid
flowchart TB
    subgraph DAY0["☀️ Day 0: Infrastructure Provisioning"]
        S1["1️⃣ Create Site<br/>+ IP Plan"]
        S2["2️⃣ Assign Devices"]
        S1 --> S2
    end

    subgraph DAY1_WAN["🌐 Day 1: WAN Layer"]
        S3["3️⃣ Create Applications"]
        S5["5️⃣ Hub Profiles"]
        S6["6️⃣ Gateway Templates"]
        S3 --> S5 --> S6
    end

    subgraph DAY1_WIRED["🔌 Day 1: Wired Layer"]
        S4["4️⃣ LAN Networks"]
        S7["7️⃣ Switch Templates"]
        S4 --> S7
    end

    subgraph DAY1_WIRELESS["📡 Day 1: Wireless Layer"]
        S8["8️⃣ WLAN Templates"]
        S9["9️⃣ RF Templates"]
        S10["🔟 Create WLANs"]
        S11["1️⃣1️⃣ Create Labels"]
        S12["1️⃣2️⃣ WLAN Policies"]
        S13["1️⃣3️⃣ Org PSKs"]
        S8 --> S9 --> S10 --> S11 --> S12 --> S13
    end

    DAY0 --> DAY1_WAN
    DAY0 --> DAY1_WIRED
    DAY0 --> DAY1_WIRELESS
    
    S6 -.-> |Late Binding| S1
    S7 -.-> |Late Binding| S1
    S9 -.-> |Late Binding| S1
```

### Step Details

| Step | Endpoint | Domain | Description |
|:----:|----------|--------|-------------|
| 1 | `POST /sites` | Day 0 | Create site container with algorithmic IP allocation |
| 2 | `POST /inventory/assign` | Day 0 | Assign claimed devices to the site |
| 3 | `POST /wan/applications` | Day 1 | Define application signatures for AppQoE |
| 4 | `POST /wired/networks` | Day 1 | Create VLANs/networks for L2 foundation |
| 5 | `POST /wan/hub-profiles` | Day 1 | Configure SD-WAN overlay topology |
| 6 | `POST /wan/gateway-templates` | Day 1 | Deploy WAN edge (SSR/SRX) configurations |
| 7 | `POST /wired/templates` | Day 1 | Deploy switch port profiles and policies |
| 8 | `POST /wireless/wlan-templates` | Day 1 | Create WLAN template containers |
| 9 | `POST /wireless/rf-templates` | Day 1 | Configure radio parameters |
| 10 | `POST /wireless/wlans` | Day 1 | Define individual SSIDs |
| 11 | `POST /wireless/labels` | Day 1 | Create policy matching labels |
| 12 | `POST /wireless/wxrules` | Day 1 | Deploy wireless security rules |
| 13 | `POST /wireless/org-psks` | Day 1 | Create organization-level PSKs |

---

## ⚡ Technical Highlights

### 🧮 Algorithmic IP Planning

**No more spreadsheets.** IP subnets are calculated mathematically from zone and site identifiers:

```python
# Formula: 10.{zone_id}.{site_id}.0/24
# Zone 1, Site 5 → Management: 10.1.5.0/24
#                → Data:       10.101.5.0/24
#                → Voice:      10.151.5.0/24
```

### 🔁 Idempotent Operations

Every operation is safe to retry. The orchestrator tracks state in Redis:

```python
# Execution flow
if state_store.is_step_completed(site_id, step_num):
    continue  # Skip - already done
    
state_store.start_step(site_id, step_num)
execute_step()
state_store.complete_step(site_id, step_num)
```

### 🎯 Late Binding Pattern

Templates are created before sites, then bound afterward:

```
1. Create Gateway Template → template_id
2. Create Site → site_id
3. Bind: PUT /sites/{site_id}/config {gatewaytemplate_id: ...}
```

### 🔐 Security-First Design

- API Key authentication via `X-Mist-API-Key` header
- Environment-based configuration (no secrets in code)
- Railway internal networking for Redis

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Redis 8.0+ 
- Juniper Mist AI API token

### Installation

```bash
# Clone the repository
git clone https://github.com/ericcgu/juniper-mist-ai.git
cd juniper-mist-ai

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings
```

### Running Locally

```bash
# Development server
hypercorn src.main:app --reload --bind 0.0.0.0:8000

# Run tests
pytest -v
```

### Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

---

## 📖 API Reference

### Full Stack Deployment

```bash
curl -X POST "https://juniper-mist.up.railway.app/orchestrator/deploy-full-stack" \
  -H "X-Mist-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "org_id": "org-123",
    "site_name": "Branch-NYC-001",
    "zone_id": 1,
    "site_id": 5,
    "device_serials": ["ABC123", "DEF456"]
  }'
```

### Response

```json
{
  "site_id": "1-5",
  "status": "completed",
  "current_step": 13,
  "total_steps": 13,
  "message": "13-Step Workflow Executed Successfully for Branch-NYC-001"
}
```

---

## 📁 Project Structure

```
juniper-mist-ai/
├── src/
│   ├── main.py                 # FastAPI application factory
│   ├── config.py               # Pydantic settings management
│   ├── redis.py                # Redis client configuration
│   ├── routers/
│   │   ├── orchestrator.py     # 13-step workflow engine
│   │   ├── sites.py            # Day 0: Site provisioning
│   │   ├── inventory.py        # Day 0: Device management
│   │   ├── wan.py              # Day 1: SD-WAN configuration
│   │   ├── wired.py            # Day 1: Switch templates
│   │   └── wireless.py         # Day 1: WLAN & RF config
│   └── services/
│       ├── network_calculator.py  # Algorithmic IP planning
│       └── redis_store.py         # State management
├── tests/
│   └── test_main.py
├── requirements.txt
├── railway.json
└── README.md
```

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **FastAPI** | Async web framework | 0.115.0 |
| **Python** | Runtime | 3.12 |
| **Redis** | State management | 7.1.0 (client) / 8.0 (server) |
| **Pydantic** | Data validation & settings | 2.7.0 |
| **Hypercorn** | ASGI server | 0.14.4 |
| **Railway** | Cloud deployment | - |
| **GitHub Actions** | CI/CD pipeline | - |
| **mistapi** | Juniper Mist SDK | 0.55.8 |

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 👤 Author

**Eric Gu**

- GitHub: [@ericcgu](https://github.com/ericcgu)
- LinkedIn: [Connect with me](https://linkedin.com/in/ericcgu)

---

<p align="center">
  <i>Built with ❤️ for network automation excellence</i>
</p>
