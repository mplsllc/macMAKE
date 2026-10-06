# Evidence-Based Compatibility

macMAKE does not assume compatibility based on clean compilation alone. Compatibility claims are backed by empirical measurement and validation against real historical software and reference environments.

## The Compatibility Approach

Historic Classic Macintosh applications rely on implicit conventions that are not captured by standard C/C++ language specifications:
- Structure packing and alignment rules (`#pragma options align=mac68k` vs `power`).
- Classic PowerPC Calling Conventions (Apple Runtime Architecture: GPR2 TOC preservation, 16-byte stack frames, parameter areas, indirect calls via transition vectors).
- Subword return value promotion conventions (extraction from low-order GPR3 byte/halfword).
- CFM / PEF container layout, loader sections, and runtime relocations.
- Static initialization ordering and Code Fragment Manager hooks (`__sinit`).

To ensure that builds behave identically to originals built with Metrowerks CodeWarrior 8, macMAKE uses a multi-tiered qualification model:

```
[Level 0: Source/Inspection] -> [Level 1: Object/Linkage] -> [Level 2: CFM/PEF Verification] -> [Level 3: OS 9 Execution]
```

## Current Compatibility Status

The following areas have verified status:

| Area | Status | Evidence / Verification Method |
|---|---|---|
| **Project Model** | Implemented | Verified parsing of CodeWarrior project definitions, recursive access paths, subtargets, and build ordering. |
| **C ABI (PPC)** | Verified | Scalar, floating-point, aggregate, and varargs call/return conventions tested against CodeWarrior 8 known-answer models. |
| **Pascal String Literals** | Verified | Opt-in `\p` string literal support matching CodeWarrior and Toolbox requirements. |
| **Structure Alignment** | Verified | Mac68k, Power, and reset alignment modes verified across standard Macintosh headers. |
| **Object Inspection** | Verified | Independent parsing of XCOFF relocatable objects and CodeWarrior MWOB library archives. |
| **Semantic Linking** | Active Development | Resolution of CFM imports, transition-vector synthesis, and compact TOC generation. |
| **PEF Generation** | Verified | PEF containers generated and validated against Apple's specification and historical CodeWarrior PEF binaries. |
| **Resource Fork Packaging** | Verified | Generation of `cfrg`, `SIZE`, and Macintosh application resource forks in MacBinary format. |
| **C++ Runtime / ABI** | Under Active Investigation | C++ mangling, exception frame parsing, RTTI, and MSL C++ runtime interactions currently being cataloged against large historical codebases. |

Further compatibility reports will be published as additional historical benchmarks are qualified.
