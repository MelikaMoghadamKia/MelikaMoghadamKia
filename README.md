<h1 align="center">Melika MoghadamKia</h1>
<h3 align="center">Post-Quantum Cryptography · IoT & Satellite Security · Network Engineering</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Post--Quantum%20Cryptography-6a0dad?style=flat-square" />
  <img src="https://img.shields.io/badge/Research-IoT%20%26%20Satellite%20Security-2a5db0?style=flat-square" />
  <img src="https://img.shields.io/badge/Seeking-MSc%20Cybersecurity%20%2F%20Cryptography-1f6f43?style=flat-square" />
</p>

---

## About Me

I am a Software Engineering graduate seeking admission to a **2-year, research-based MSc program in Cybersecurity and Cryptography** in Europe. My academic trajectory moves from a rigorous foundation in network infrastructure toward cryptographic research addressing the transition to a post-quantum world.

I began my career with hands-on, standards-based network engineering — routing (OSPF, IS-IS), overlay architectures (VXLAN), and enterprise-grade Cisco/Linux deployments — before redirecting this systems-level understanding toward the security layer itself. My current research centers on **Post-Quantum Cryptography (PQC)**, with applied work in **IoT constrained-device security** and **satellite communications**, examining how lattice-based cryptographic primitives can be deployed under real-world computational and bandwidth constraints.

This combination — practical infrastructure experience paired with cryptographic research — is the foundation I intend to build on at the graduate level.

---

## Research Experience

### Project A — Post-Quantum Key Encapsulation for Satellite Communications
*Bachelor's Thesis*

This thesis addresses the security of the satellite communication uplink/downlink against quantum-capable adversaries, replacing classical key exchange with NIST-standardized post-quantum primitives.

**Core contributions:**
- Designed and simulated a key establishment layer using **ML-KEM (CRYSTALS-Kyber)** for post-quantum key encapsulation over a satellite communication channel.
- Integrated **ML-DSA (CRYSTALS-Dilithium)** for message authentication, providing quantum-resistant digital signatures alongside the encapsulation layer — a combination that strengthens the protocol's resistance to both passive and active adversaries.
- Benchmarked cryptographic performance in Python using **liboqs**, comparing post-quantum key encapsulation against classical RSA-3072 key exchange under equivalent conditions.

**Simulation results — ML-KEM-768 vs. RSA-3072 (liboqs, Python):**

| Operation | ML-KEM-768 | RSA-3072 | Result |
|---|---|---|---|
| Key generation | `[insert ms]` | `[insert ms]` | `[Xx faster]` |
| Encapsulation / Encryption | `[insert ms]` | `[insert ms]` | `[Xx faster]` |
| Decapsulation / Decryption | `[insert ms]` | `[insert ms]` | `[Xx faster]` |
| Public key size | `[insert bytes]` | `[insert bytes]` | — |
| Ciphertext size | `[insert bytes]` | `[insert bytes]` | — |

*Table populated from local simulation output — insert your recorded figures to finalize.*

---

### Project B — Post-Quantum Cryptography for IoT
*Published Paper*

This work evaluates the feasibility of deploying post-quantum key exchange on resource-constrained IoT hardware, where memory, energy, and bandwidth budgets are orders of magnitude smaller than in conventional computing environments.

**Core contributions:**
- Benchmarked **Kyber-512** on an **ARM Cortex-M4** target, quantifying the real hardware cost of post-quantum key exchange on embedded devices.
- Measured and reported the metrics most relevant to constrained deployment: **energy consumption per operation**, **peak RAM usage**, and **public key / ciphertext sizes**, establishing whether Kyber-512 fits within typical IoT power and memory budgets.
- Proposed a **hybrid classical–post-quantum key exchange** as a transitional solution — combining a classical primitive with Kyber-512 to preserve backward compatibility and defense-in-depth during the current migration period, while full post-quantum-only deployment matures.

**Key device-level metrics (ARM Cortex-M4, Kyber-512):**

| Metric | Value |
|---|---|
| Energy per key exchange | `[insert mJ]` |
| Peak RAM usage | `[insert KB]` |
| Public key size | `[insert bytes]` |
| Ciphertext size | `[insert bytes]` |

*Table populated from the published paper's benchmark results — insert your reported figures to finalize.*

---

## Technical & Engineering Skills

**Cryptography & Security**
`Post-Quantum Cryptography (ML-KEM, ML-DSA, Kyber)` · `liboqs` · `Key Encapsulation Mechanisms` · `Hybrid Cryptographic Schemes` · `Applied Cryptographic Benchmarking`

**Infrastructure & Networking**
`CCNP Enterprise` · `CCNP SD-WAN` · `OSPF` · `IS-IS` · `VXLAN` · `Cisco Catalyst` · `Enterprise Network Design`

**Systems & OS**
`Linux` · `Docker` · `LXC` · `Embedded / ARM Cortex-M4 Targets`

**Programming**
`Python` (primary — research & simulation) · `C++` · `JavaScript` · `HTML/CSS`

The infrastructure and networking skill set underpins the research above directly: understanding routing, overlay networks, and enterprise deployment constraints informs how cryptographic protocols must behave under real network and hardware conditions — not just in isolated simulation.

---

## Contact

<p align="left">
  <a href="mailto:your.email@example.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://linkedin.com/in/your-linkedin"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

*Open to research collaboration and discussion related to post-quantum cryptography, IoT security, and satellite communications.*
