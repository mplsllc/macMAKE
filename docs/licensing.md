# Licensing Model

macMAKE is structured with a clear operational separation between its proprietary core engine, redistributed open-source toolchain components, and historical third-party development materials.

---

## 1. Proprietary macMAKE Core

The core macMAKE build engine, command-line interface, project model, semantic linker, PEF generator, and packaging tools are **proprietary software** developed by Minneapolis LLC.

- The proprietary source code is not included in the public `macMAKE` repository.
- Binaries will be distributed under the terms outlined in the [LICENSE](../LICENSE) file.
- The macMAKE engine does not link against third-party GPL or LGPL program code.

---

## 2. Open-Source Toolchain Components (`macmake-gpl`)

macMAKE invokes GCC and GNU Binutils as separate executables using command-line arguments and filesystem objects. The macMAKE engine does not link against their program code. The GPL-covered executables and their corresponding source are distributed as separately licensed components:

- **GNU Compiler Collection (GCC 12.2.0):**  
  Provides PowerPC C/C++ compilation via a customized target configuration (`powerpc-unknown-macmake`). GCC itself is licensed under the GNU General Public License v3 (GPL-3.0-or-later).  
  *Runtime Library Note:* The GCC Runtime Library Exception applies to runtime library units in target executables when built with an eligible compilation process; however, this toolchain build specifically configures `--disable-libgcc` and `--disable-libstdcxx`. The Exception is not the reason macMAKE can execute the GCC compiler.
- **GNU Binutils (2.46.1):**  
  Provides the PowerPC assembler (`as`) and object dumper (`objdump`). Licensed under GPL-3.0-or-later.

To provide the corresponding source required for GPL-covered components distributed with macMAKE:
- Complete pristine upstream source archives (`gcc-12.2.0.tar.xz`, `binutils-2.46.1.tar.xz`), verified against their SHA-256 digests, are preserved in a durable source release under our control.
- Patches, build scripts, configuration metadata, and distribution manifests are published in the corresponding source repository:

**[`https://github.com/mplsllc/macmake-gpl`](https://github.com/mplsllc/macmake-gpl)**  
**Manifest:** [`corresponding-source-manifest.json`](https://github.com/mplsllc/macmake-gpl/blob/main/corresponding-source-manifest.json)

The presence of GPL-covered executables in distributed packages does not make macMAKE itself open source or subject to the GPL.

---

## 3. Historical Apple & Metrowerks SDKs

To compile historical Macintosh software, projects often depend on proprietary headers and libraries:
- **Apple Universal Interfaces:** Proprietary headers and stub libraries defining Toolbox APIs.
- **Metrowerks Standard Library (MSL):** Proprietary C and C++ runtime libraries (`MSL_C_Carbon.Lib`, `MSL_Runtime_PPC_D.Lib`, etc.).

**macMAKE does not redistribute proprietary Apple or Metrowerks materials without authorization.**

Users must supply their own copies of historical development files from software they legally possess. macMAKE provides mechanisms to detect, catalog, and consume these user-supplied SDK roots on the development host.
