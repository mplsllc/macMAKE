**This project is developed with the assistance of an LLM**

# macMAKE

<p align="center">
  <img src="img/logo.png" alt="macMAKE">
</p>

**macMAKE v0.1.1 is a Linux-native toolchain for building Classic Macintosh applications.** Its supported release path targets Mac OS 9 PowerPC CFM/PEF applications, primarily written in C, alongside an experimental native Motorola 68000 application backend.

It grew out of a simple problem: compiling Classic Mac software with a modern compiler is possible, but large historical Macintosh applications were built around much more than a compiler.

They depended on CodeWarrior project semantics, the Classic PowerPC ABI, CFM linking, PEF binaries, resource forks, historical runtime behavior, target membership, access paths, library ordering, and numerous assumptions that were normally invisible because CodeWarrior handled them.

macMAKE attempts to reproduce that environment on a modern host.

It is not a CodeWarrior emulator and it is not a frontend for Retro68. The goal is to understand what a CodeWarrior-era project means and reproduce the relevant build behavior directly.

> Retro68 asks: **How can modern GCC produce a Classic Mac program?**
>
> macMAKE asks: **What did CodeWarrior mean when it built this Classic Mac project, and how can we reproduce that behavior from Linux?**

<p align="center"><strong>Support development</strong></p>
<p align="center">
  <a href="https://ko-fi.com/macsurf" target="_blank"><img src="https://img.shields.io/badge/Ko--fi-Support-FF5E5B?style=for-the-badge&logo=kofi&logoColor=white" alt="Support on Ko-fi" height="40"></a>
  &nbsp;
  <a href="https://www.patreon.com/cw/MacSurf" target="_blank"><img src="https://img.shields.io/badge/Patreon-Support-FF424D?style=for-the-badge&logo=patreon&logoColor=white" alt="Support on Patreon" height="40"></a>
  &nbsp;
  <a href="https://github.com/sponsors/mplsllc" target="_blank"><img src="https://img.shields.io/badge/GitHub-Sponsor-DB61A2?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Sponsor on GitHub" height="40"></a>
</p>

<p align="center"><strong>Thanks to our supporters:</strong><br>Ko-Fi: <strong>Chris Marks, Rogue, Turuun, kilgeist</strong><br>Patreon: <strong>Mack Chamberlain, Lucas, Joseph Mulvaney, Shlooom, Bigdipper</strong></p>

---
## Next release: CLEAR developer preview (in preparation)

The next release is being tested with a **CLEAR-first** development path: supported Classic Mac OS applications built without proprietary CodeWarrior implementation libraries or Apple SDK development headers. Historical CodeWarrior/MSL compatibility remains an **explicit optional setup**, using a pinned subset of [macMAKELibs](https://github.com/mplsllc/macMAKELibs) or developer-supplied paths; it must not silently enter a CLEAR build.

[Read the CLEAR preview scope and clean-install acceptance requirements](docs/clear-preview.md). **v0.1.1 remains the latest public release** until the new candidate has been built, tested, and published. The preview's capabilities are not claims about the existing v0.1.1 binary.

## What macMAKE does

macMAKE provides an end-to-end development workflow on Linux x86-64 for creating Classic Macintosh applications:

- **CodeWarrior-style project configuration**: `macmake.toml` manifests with explicit target membership, access paths, and ordered libraries.
- **Classic PowerPC toolchain**: Bundled GNU GCC 12.2.0 and Binutils 2.46.1 producing big-endian PowerPC XCOFF objects.
- **Native CFM linker and PEF generator**: Eliminates dependence on external linkers to emit valid Preferred Executable Format (PEF) containers with transition vectors and CFM import/export fragments.
- **Macintosh resource compiler and packager**: Generates resource forks (`.rsrc`), Finder metadata (`.finf`), and MacBinary II (`.bin`) distribution packages.
- **SDK catalog and onboarding**: Automated minimal SDK fetching and verification for authorized Classic Macintosh headers.
- **Offline CLI and machine-readable reference**: Built-in documentation, deterministic JSON help schemas, and manifest validation schemas.

## What's new in v0.1.1

macMAKE v0.1.1 delivers seven release enhancements:

1. **Installer and first application**: Case-sensitive layout handling in `macMAKELibs`, clean onboarding from clean home directories, and verified incremental rebuilds.
2. **Streamlined SDK onboarding**: `macmake sdk fetch --minimal` sparse checkout of the pinned Universal Interfaces subset with SHA-256 validation, plus verified local MSL helper scripts.
3. **Independent native Motorola 68000 application builds**: Bundled GNU GCC 12.2.0 / Binutils 2.46.1 `m68k-unknown-elf` toolchain building bounded C89 applications with CODE 0/1 segments, Toolbox veneers, Finder metadata, and MacBinary II packaging without requiring Retro68. Includes a sequenced OS roadmap separating toolchain capabilities from application-specific observations.
4. **External Rust-to-Classic XCOFF interop**: Consumes big-endian PowerPC XCOFF objects emitted by external pinned Rust nightly (`powerpc-apple-macos.json`), with macMAKE handling native CFM/PEF linking, resources, and MacBinary packaging.
5. **CodeWarrior XML import & Classilla build boundary**: `macmake import-cw-xml` feature matrix and workflow guide for importing historical CodeWarrior XML projects into `macmake.toml`, alongside Classilla 128-target inventory and packaging boundaries.
6. **Optional emulator execution (`macmake run`)**: Safe profile-driven QEMU Mac OS 9.2.2 runner using copy-on-write disk overlays, QMP P6 PPM screenshot capture and checkpoint validation, and structured run reports. Known nonblocking issue: prompt repetition on 250ms timeouts during interactive wait.
7. **Analytics opt-out**: Full telemetry transparency with `--no-analytics`, `MACMAKE_DISABLE_ANALYTICS=1`, and persistent preference markers.

## Verified Mac OS 9.2.2 runtime acceptance

macMAKE v0.1.1 has verified real-guest runtime acceptance:

- **Environment**: QEMU 8.2.2, `mac99` / G4, 1 GiB RAM, 800×600 display, running Mac OS 9.2.2.
- **Application fixture**: makePAD MacBinary (SHA-256 `505a3b1deb62ffc396537b1010c8f23921f4ae4308ac6ee989ccf7cd285ca3d1`).
- **Runtime observations**: The application launched from the guest volume, interactive text entry was confirmed ("rc7 runtime ok"), the application window rendered the text, File > Quit invoked the unsaved-changes dialog, choosing "Don't Save" closed the dialog, and the guest returned cleanly to Finder.
- **Screenshot evidence**: Unmodified P6 PPM captures at `guest_boot.ppm` (SHA-256 `7dc1fce7441346067023e89d542dc95e9c2e91006e26703769a4326a7c8e6ab2`) and `application_state.ppm` (SHA-256 `2fc378da228afdb12490e3079eb913d2e485f79c8e87966758e152cf61de8bf1`).
- **Disk integrity**: Base guest disk hash unchanged (SHA-256 `5998d787dea695734948a52285e7b57d6cae840f2681a174f98e33ec9e8045e8`).

## Support boundaries and current limitations

- **Host platform**: Linux x86-64 only. macOS (Intel and Apple Silicon) and Windows hosts are not supported.
- **Qualified primary target**: Classic Mac OS 9 PowerPC CFM/PEF applications, primarily in C.
- **Experimental 68K profile**: C89, one near-model CODE 1 segment, CODE 0 jump table/startup, bounded PC-relative file-backed data, and no external linked libraries. CFM-68K and multi-segment A5 applications are not supported in v0.1.1.
- **Rust integration**: Demonstrates CLI integration with external big-endian PowerPC XCOFF objects from a pinned Rust nightly compiler. macMAKE does not bundle `rustc` or compile Rust source directly.
- **C++ support**: Limited to preview syntax without Itanium ABI runtime parity, general RTTI, exception handling, or `libstdc++`.
- **CodeWarrior XML import**: Handles project structure, source membership, and access paths from XML exports; does not read proprietary binary `.mcp` files.
- **Third-party SDK material**: Apple Universal Interfaces and Metrowerks MSL are proprietary historical materials. Users must supply files they are authorized to use.

## Working examples

The release includes reproducible, inspectable examples:

- [`examples/first-app/`](examples/first-app/README.md): Two-source Classic PowerPC C application demonstrating Universal Interfaces imports, MSL linking, and MacBinary packaging.
- [`examples/first-app/hello-window-68k/`](examples/first-app/hello-window-68k/README.md): Experimental native Motorola 68000 HelloWindow application using CODE resources without Retro68.
- [`examples/classic-rust-interop/`](examples/classic-rust-interop/README.md): External Rust-to-PowerPC XCOFF interop example linking Rust scalar code with a Classic C caller.
- [`docs/codewarrior-xml-and-classilla.md`](docs/codewarrior-xml-and-classilla.md): Step-by-step guide and feature matrix for CodeWarrior XML importing.

## Installation

Install macMAKE for the current Linux user:

```sh
curl -fsSL https://macmake.dev/install.sh | bash
```

To opt out of the post-install completion telemetry:

```sh
curl -fsSL https://macmake.dev/install.sh | bash -s -- --no-analytics
```

To fetch the versioned minimal SDK subset during installation (requires authorization for Apple Universal Interfaces):

```sh
curl -fsSL https://macmake.dev/install.sh | bash -s -- --with-sdk
```

For full options and manual installation details, see [docs/INSTALL.md](docs/INSTALL.md) and the [online installation guide](https://macmake.dev/install.html).

## Licensing and corresponding source

The macMAKE CLI executable and proprietary core are closed-source software under the [macMAKE Proprietary Binary License v1.0](LICENSE). It permits free development, testing, agentic coding, and commercial software creation while restricting redistribution of the proprietary binary. Developers retain complete ownership of applications they build with macMAKE.

The toolchain bundles GNU GCC 12.2.0 and GNU Binutils 2.46.1 executables. These remain licensed under the GPL and their respective terms. The exact matching GNU corresponding source release is published at:
[macmake-v0.1.1-rc4-toolchain-sources](https://github.com/mplsllc/macmake-gpl/releases/tag/macmake-v0.1.1-rc4-toolchain-sources) (archive SHA-256 `ddd3b20cbaf3e2cbdca4ed5f61f34946065f71089b9ea7a99bac188213145433`).

See [docs/licensing.md](docs/licensing.md) for complete component inventories, licenses, and legal boundaries.

## Downloads and releases

- **v0.1.1 Release**: [GitHub Releases v0.1.1](https://github.com/mplsllc/macMAKE/releases/tag/v0.1.1)
  - Binary archive: `macmake-v0.1.1-linux-x86_64.tar.xz`
  - SHA-256: `d83c173d4184a67738df3bad7d0cadb2b6eab45fa2cc06df89f9f7eff4bd0656`
- **v0.1.0 Release**: [GitHub Releases v0.1.0](https://github.com/mplsllc/macMAKE/releases/tag/v0.1.0)
  - Binary archive: `macmake-v0.1.0-linux-x86_64.tar.xz`
  - SHA-256: `3c9da84e53022d16a07208d0591a9964b8399dbe043b3628e227373a6aa6e980`
- **GNU Corresponding Source**: [macmake-gpl releases](https://github.com/mplsllc/macmake-gpl/releases)

## Project links

- Website: [macmake.dev](https://macmake.dev)
- Compatibility tracker: [Classic Macintosh OS compatibility](https://macmake.dev/compatibility/)
- Documentation: [Online documentation index](https://macmake.dev/docs/)
- CLI reference: [Generated command contracts](https://macmake.dev/docs/cli-reference.html)
- Getting started: [First application walkthrough](https://macmake.dev/getting-started.html)
- Issue tracker: [GitHub Issues](https://github.com/mplsllc/macMAKE/issues)
