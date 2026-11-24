```text
                                                 [RING-0]
                                                 .---.
                                                 |CPU|--> [PML4]
                                                 '---'      |
                                                            v
   ____  ____   ___   ____ __  __    _  _____ ___   [PHYS_ADDR]
  |  _ \|  _ \ / _ \ / ___|  \/  |  / \|_   _|_ _|      |
  | |_) | |_) | | | | |  _| |\/| | / _ \ | |  | |       v
  |  __/|  _ <| |_| | |_| | |  | |/ ___ \| |  | |   [PAGE_FAULT: 0]
  |_|   |_| \_\___/ \____|_|  |_/_/   \_\_| |___|   [CR3: LOADED]

 .-----------------------------------------------------------------------------.
 | (x) (-) (+)                     ~/kernel_space.sys                          |
 |-----------------------------------------------------------------------------|
 |                                                                             |
 | Systems & Low-Level Software Engineer from Brazil.                          |
 |                                                                             |
 | Focus: Windows Kernel Drivers (WDM / KMDF), x64 Virtual Memory,             |
 | PTE Manipulation, Hypervisor Interfaces, Process Internals, Reverse         |
 | Engineering, and High-Throughput Native Systems in C, C++ and Rust.         |
 |                                                                             |
 | "Ring 0 over Ring 3. Native performance over abstractions."                 |
 | -@progmatios23                                                              |
 |                                                                             |
 '-----------------------------------------------------------------------------'
```

<p><img src="./imgs/headings/stack.svg" alt="01 Stack" width="180" height="44"></p>

<p>
  <img src="./imgs/icons/lang-c.svg" alt="C" title="C" width="60" height="60"
  ><img src="./imgs/icons/lang-cpp.svg" alt="C++" title="C++" width="60" height="60"
  ><img src="./imgs/icons/lang-rust.svg" alt="Rust" title="Rust" width="60" height="60"
  ><img src="./imgs/icons/lang-asm.svg" alt="ASM" title="x86_64 ASM" width="60" height="60"
  ><img src="./imgs/icons/lang-kernel.svg" alt="Ring 0 Kernel" title="Windows Kernel" width="60" height="60"
  ><img src="./imgs/icons/lang-re.svg" alt="Reverse Engineering" title="Reverse Engineering" width="60" height="60"
  ><img src="./imgs/icons/lang-linux.svg" alt="Linux" title="Linux POSIX" width="60" height="60"
  ><img src="./imgs/icons/lang-python.svg" alt="Python" title="Python Tooling" width="60" height="60">
</p>

<p><img src="./imgs/headings/projects.svg" alt="02 Repositories" width="240" height="44"></p>

| Repository | Domain | Language | Architecture & Features |
| :--- | :--- | :--- | :--- |
| **[NEWKM](https://github.com/progmatios23/NEWKM)** | Windows Kernel Driver | `C++` / `C` | WDM, manual mapping via kdmapper, PTE manipulation, CR3 traversal, synthetic call stack spoofing |
| **[street-decrepytor](https://github.com/progmatios23/street-decrepytor)** | Reverse Engineering Suite | `Rust` / `Python` | Native Rust debugger engine, process memory dumper, Unicorn engine emulation, binary disassembly |
| **[lfi-traversal-lab](https://github.com/progmatios23/lfi-traversal-lab)** | Systems Security Research | `Python` | Path traversal research, null-byte truncation breakdown, WAF evasion normalization, canonicalization defense |
| **[oh-my-pi-rs](https://github.com/progmatios23/oh-my-pi-rs)** | Native Systems Rework | `Rust` | Single static binary architecture, zero-Node runtime, minimal memory footprint |
| **[Street-decryter](https://github.com/progmatios23/Street-decryter)** | Disassembler & Debugger | `C++` | IDA-style listing, x64dbg-style engine, PE/ELF/Mach-O parsers, built-in MCP server |

<p><img src="./imgs/headings/kernel.svg" alt="03 Kernel / Internals" width="280" height="44"></p>

* **Kernel & Driver Development**
  * Windows Kernel Architecture (WDM / KMDF), manual mapping via vulnerable signed drivers (kdmapper).
  * x64 Virtual Memory Translation: Page Table Entry (PTE) modifications, CR3 directory base walking, direct physical RAM access.
  * Synthetic Call Stack Spoofing: evading kernel stack walking heuristics and anti-cheat thread inspection.
  * Driver Signature Enforcement (DSE) bypasses and kernel object manipulation (DKOM).

* **Reverse Engineering & Binary Analysis**
  * Dynamic debugging, static disassembly, and decompilation (IDA Pro, x64dbg, Ghidra).
  * Binary formats: PE32/PE32+, ELF64, Mach-O, section headers, relocations, export/import directory parsing.
  * Hooking methodologies: IAT/EAT patching, inline detours, hardware breakpoint routing, memory page guarding (`PAGE_GUARD`).

* **High-Throughput Systems Software**
  * Performance engineering in modern Rust and C++20 with zero-allocation models.
  * Network transport, socket multiplexing, and TLS fingerprint replication (BoringSSL, JA3/JA4).

<p><img src="./imgs/headings/contact.svg" alt="04 Connect" width="200" height="44"></p>
Add Me>  " ejog710kj "|usario discord -

<p>
  <a href="https://github.com/progmatios23"><img src="./imgs/icons/icon-git.svg" alt="GitHub: @progmatios23" title="GitHub: @progmatios23" width="60" height="60"></a>
</p>

```text
 progmatios23@ntoskrnl ~ % exit
 logout
 Saving ring0 session... completed.

 [Process completed]▌
```
