# macMAKE CLEAR — upcoming developer preview

**Release status:** preparation and acceptance testing in progress. **The latest public release is v0.1.1.** These instructions describe the direction of the next release; they are not a claim that the new binary or installer is published.

## Two explicit development paths

**CLEAR (default)** is intended to compile and package supported Classic Macintosh applications without Metrowerks CodeWarrior implementation libraries or proprietary Apple SDK development headers. It uses macMAKE's generated Classic interfaces, versioned C runtime/ABI profile, semantic CFM/PEF linker and resource packager. OS-supplied CarbonLib on Mac OS 9 remains a normal runtime dependency, not a development-tool prerequisite.

**Legacy compatibility (optional)** supports projects that explicitly require CodeWarrior libraries and older Universal Interfaces. For convenient setup, the next installer is being prepared to offer a separate optional fetch from [macMAKELibs](https://github.com/mplsllc/macMAKELibs), pinned to commit `65b3201d352079010cabaeb57a81824b307ed22d` and verified file checksums. Existing user-supplied CodeWarrior installation paths will remain an explicit alternative. This mode must not be selected silently by CLEAR builds, and the optional files are not bundled into the default archive.

The currently published v0.1.1 `--with-sdk` option combines minimal Universal Interfaces fetching and first-app MSL setup. Its behavior remains unchanged for that published version. The next release will separate CLEAR setup from optional legacy-library installation. Exact commands will be published after the candidate CLI and installer are tested together; do not assume proposed flags already exist in v0.1.1.

## What is verified, and what remains open

The development branch's MacSurf CLEAR effort has compiled all 979 original source memberships, performed audited semantic linking and PEF/resource packaging without proprietary CodeWarrior/MSL implementation inputs, and passed independent structural checks. Historical CLEAR MacSurf candidates have also demonstrated real Mac OS 9 browser startup and JavaScript/closure/reload/quit behavior. A particular new candidate is accepted for runtime only after its exact artifact is tested; older binary results are not transferable.

General CodeWarrior Pro 8 feature parity is **not** established. C++ ABI/RTTI/exceptions, all legacy SDK APIs, arbitrary historical applications, complete Classilla rebuilding, and broad System 6/7/8 runtime claims remain separately gated. Some toolchain-generated Retro68 CFM import archives have been read for provenance metadata; their stub objects were not linked in the audited MacSurf build. The release must disclose what its own executed-input audit proves.

## How the preview will be tested

The release candidate must pass on a clean Linux x86-64 user account or VM with no developer checkout, no historical libraries and no Retro68 installation:

1. Install the exact frozen, checksum-verified archive without analytics when opted out.
2. Configure the default CLEAR SDK/profile without downloading MSL libraries.
3. Run doctor on the supported example, build it from source, inspect PEF/CFM/forks/Finder metadata and confirm no proprietary development inputs were accessed.
4. Transfer and launch on a supported Classic Macintosh guest, demonstrate the expected application behavior, and quit normally.
5. Reinstall or upgrade safely; verify opt-out persistence and failed-download rollback.
6. Repeat optional legacy setup independently, verifying the pinned `macMAKELibs` subset, clear profile selection and absence of silent legacy fallback.

The candidate's exact version, executable help/schema, install flags, test logs, checksum and download links will be added only after these checks pass.

Until then, use the [current v0.1.1 documentation](README.md) and the [published releases](https://github.com/mplsllc/macMAKE/releases).
