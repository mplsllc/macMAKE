# Architecture Overview

macMAKE bridges modern host-side development environments with Classic Mac OS execution targets.

```
       Modern Linux Workstation
  +---------------------------------+
  | Modern IDE / Git / Automation   |
  |                                 |
  |   macmake build (CLI)           |
  |             |                   |
  |   Project & Target Graph Model  |
  |   (Access paths, definitions)   |
  |             |                   |
  |   CodeWarrior Project Import    |
  |             |                   |
  |   Classic PowerPC Toolchain:    |
  |   - GCC 12 C/C++ Frontend       |
  |   - Binutils Assembler          |
  |   - macMAKE Semantic Linker     |
  |   - PEF Generation Engine       |
  |   - Resource & Fork Packaging   |
  +-------------+-------------------+
                |
                v (PEF / MacBinary / App Package)
  +---------------------------------+
  | Classic Mac OS (System 7 - OS 9)|
  | CFM / Code Fragment Manager     |
  | Classic PowerPC ABI Execution   |
  +---------------------------------+
```

## High-Level Pipeline

1. **Project Understanding:**  
   macMAKE parses CodeWarrior project files, target definitions, access paths, and build settings, translating them into an explicit semantic dependency graph.

2. **Source Compilation:**  
   Source files are compiled using a Classic PowerPC target configuration that reproduces historical ABI behaviors (such as GPR2 TOC preservation, transition vectors, and structure alignment).

3. **Semantic Linking:**  
   Instead of relying on modern ELF linkers or emulation, macMAKE analyzes object files, CodeWarrior archives (`MWOB`), and import libraries, constructing symbol tables and relocation directives according to the Code Fragment Manager (CFM) specification.

4. **Executable & Resource Packaging:**  
   macMAKE outputs Preferred Executable Format (PEF) containers alongside Macintosh resource forks (`cfrg`, `SIZE`, menus, dialogs), producing valid MacBinary or raw dual-fork applications ready for execution on vintage hardware or emulators.

---

For details on licensing and components, see [licensing.md](licensing.md).
