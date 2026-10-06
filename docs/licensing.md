# Licensing Model

macMAKE is designed with a clear separation between its proprietary core engine, redistributed open-source toolchain components, and historical third-party development materials.

---

## 1. Proprietary macMAKE Core

The core macMAKE build engine, command-line interface, project model, semantic linker, PEF generator, and packaging tools are **proprietary software** developed by Minneapolis LLC.

- The proprietary source code is not included in the public `macMAKE` repository.
- Binaries will be distributed under the terms outlined in the [LICENSE](../LICENSE) file.
- The macMAKE core does not statically or dynamically link with copyleft (GPL/LGPL) code.

---

## 2. Open-Source Toolchain Components (`macmake-gpl`)

macMAKE utilizes certain open-source tools to provide host-side compilation and assembly services. These tools are invoked as separate external processes across standard command-line and filesystem boundaries:

- **GNU Compiler Collection (GCC 12.2.0):**  
  Provides PowerPC C/C++ compilation via a customized target configuration (`powerpc-unknown-macmake`). Covered by the GNU General Public License v3 (GPL-3.0-or-later) with the GCC Runtime Library Exception.
- **GNU Binutils (2.46.1):**  
  Provides the PowerPC assembler (`as`) and object utilities. Covered by GPL-3.0-or-later.

In accordance with the requirements of the GPL, all corresponding source code, patches, build scripts, and configuration recipes required to reproduce these binaries are published in the separate public repository:

**[`https://github.com/mplsllc/macmake-gpl`](https://github.com/mplsllc/macmake-gpl)**

The redistribution of these GPL-covered tools does not make macMAKE itself open source or subject to the GPL.

---

## 3. Historical Apple & Metrowerks SDKs

To compile historical Macintosh software, projects often depend on proprietary headers and libraries:
- **Apple Universal Interfaces:** Proprietary headers and stub libraries defining Toolbox APIs.
- **Metrowerks Standard Library (MSL):** Proprietary C and C++ runtime libraries (`MSL_C_Carbon.Lib`, `MSL_Runtime_PPC_D.Lib`, etc.).

**macMAKE does not redistribute proprietary Apple or Metrowerks materials without authorization.**

Users must supply their own copies of historical development files from software they legally possess. macMAKE provides mechanisms to detect, catalog, and consume these user-supplied SDK roots safely on the development host.
