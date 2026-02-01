```markdown
# 🌅 Module 1: Day 0 — Identity & Topology

> **"The Genesis Layer"**

Before policies (Day 1) or assurance (Day 2) can exist, we must establish the **Identity** of the Organization and the **Topology** of the network. This module automates the foundational infrastructure using "Digital Twin" principles, creating a verifiable model of the network before physical hardware is ever involved.

---

## 🔑 Key Concepts

### 1. Control Plane Identity (Reachability)
We treat the **Juniper Mist Cloud** is the Cloud AI Controller. Before any automation attempts to configure infrastructure, the API performs a **Layer 7 Handshake** (`POST /org/self`) to verify API Token Identity:
* ✅ **Authentication:** Is the API Token cryptographically valid?
* ✅ **Context:** Does the Organization UUID exist in this cloud instance?
* ✅ **Authorization:** Does the token have required permissions?

### 2. Algorithmic Topology
We reject manual IP management and spreadsheets. The API uses a `NetworkCalculator` service to mathematically carve a **/8 Supernet** into **8 geographic Zones** (using `/11` blocks). This deterministic approach guarantees **zero IP collisions** across the entire enterprise.

### 3. Supply Chain Identity (ZTP)
Hardware is claimed and assigned to sites programmatically via the API. The **"Identity"** of the device (MAC Address/Claim Code) is bound to the **"Topology"** of the site (Configuration) *before* the device is physically installed.

---

## 🔄 The Workflow

| Step | Endpoint | Domain | Action |
|:---:|---|---|---|
| 1️⃣ | `POST /org/self` | **Identity** | **Reachability Probe:** Verifies Token, Org Context & Permissions. |
| 2️⃣ | `POST /site/provision` | **Topology** | **Design:** Calculates IP Plan & Creates the Site Shell. |
| 3️⃣ | `POST /inventory/ztp` | **Logistics** | **ZTP:** Ingests Claim Codes & Binds Hardware to Site. |

---

## 📁 Files

| File | Domain | Description |
|---|---|---|
| `org.py` | **Identity** | Handles the initial Control Plane handshake and verification. |
| `sites.py` | **Topology** | Site creation logic and algorithmic IP plan generation. |
| `inventory.py` | **Logistics** | Supply chain integration (ZTP) and device claiming. |
| `models.py` | **Validation** | Pydantic models for request/response validation. |

```
