# Classic PowerPC Rust/C interop example

This is a small Classic Mac OS PowerPC application with one Rust-compiled
function called from its C entry point. Rust computes `41 + 1`; the C caller
beeps through the CarbonLib import when the returned value is correct, then
exits through the ordinary CodeWarrior MSL startup path.

macMAKE v0.1.1 does not include a Rust compiler provider. This sample uses the
separately installed Rust nightly pinned below to produce a single big-endian
PowerPC XCOFF object, then uses the normal `macmake build` path for native
XCOFF linking, CFM/PEF generation, resource/Finder metadata, and MacBinary II
packaging. It is a reproducible integration sample, not a claim that Rust
source is accepted directly by `macmake build` or that the Rust toolchain is
bundled with macMAKE.

## Prerequisites

- Linux x86-64 and the macMAKE v0.1.1 installation.
- `rustup`, `cargo`, GNU `ar`, `rg`, and Python 3.
- Rust `nightly-2023-03-28` (`rustc 1.70.0-nightly`, commit `2036fdd24`)
  with `rust-src`; the pinned `rust-toolchain.toml` requests it.
- The separately supplied Universal Interfaces and three MSL archives
  described by [`first-app`](../first-app/README.md). The `sdk/` directory is
  local input and is excluded from source control.

The target specification follows the `powerpc-apple-macos.json` target in
MacRust's `classic-mac-rust` revision
`ecab002216f7b5764b12e339a1880f4d96cdad90`, with Rust final linking delegated
to macMAKE. MacRust's broader historical demonstrations also document
callbacks, allocation, and a Rust-owned Window Manager event loop using C
Toolbox shims. This example deliberately uses a scalar C ABI because the
measured MacRust work found a by-value aggregate ABI mismatch between Rust's
AIX-derived XCOFF ABI and the Macintosh C ABI. Use pointer/out-parameter
interfaces or a C shim for aggregate values.

## Build

Prepare and register the same authorized SDK inputs used by `first-app`, then
run the helper to copy the three verified MSL archives into this example's
ignored `sdk/` directory:

```sh
macmake sdk fetch --minimal
macmake sdk add "$HOME/.local/share/macmake/macMAKELibs/Universal" \
  --id macos9-sdk
macmake sdk verify macos9-sdk
../first-app/setup-user-msl.sh \
  "$HOME/.local/share/macmake/macMAKELibs" ./sdk
```

The user must be authorized to use these historical SDK and runtime files.
From this directory:

```sh
./build-rust.sh
macmake doctor . --target "Classic PPC Rust Interop"
macmake build . --target "Classic PPC Rust Interop"
macmake inspect-artifact build/RustInterop/ClassicPPCRustInterop/RustInterop.pef \
  --resource-fork build/RustInterop/ClassicPPCRustInterop/RustInterop.rsrc \
  --finder-info build/RustInterop/ClassicPPCRustInterop/.finf/RustInterop.APPL \
  --creator HmRS --file-type APPL --json
```

For a repeatable check that rebuilds the Rust object, invokes the installed
macMAKE `doctor` and `build` commands, and verifies the link evidence, output
hashes, imports, Finder data, and structural artifact checks, run:

```sh
python3 test-rust-interop.py --macmake macmake
```

The test leaves its generated files under the example's ignored `build/` and
`rust/target/` directories. It checks Linux-side build and structure only; it
does not claim a Classic Mac OS launch.

The MacBinary II application is emitted beside the PEF. On a Classic
PowerPC Macintosh, launching it should produce a short system beep and return
to the Finder. This compact sample is designed to exercise the Rust/C call
and native macMAKE package path; the MacRust repository separately retains
the larger window/event-loop demonstration.

## Evidence boundary

The pinned MacRust experiments include a Rust-produced XCOFF object linked
into a PEF by CodeWarrior and a C-to-Rust scalar call that wrote a `PASS`
marker (`E0-CW-16`), plus callback/allocation and a Rust-owned window/event
loop (`E0-CW-11`, `E0-CW-13`). Those development experiments are separate
from the macMAKE build above. This example's host build and structural
inspection are separately reproducible; OS runtime testing must be recorded
for the exact macMAKE executable and Mac OS version used.

## Version-check regression tests

Run `python3 test-version-check.py` to exercise the build helper's compiler-version gate without installing Rust or the SDK. The tests cover matching, mismatched and empty output, output larger than a pipe buffer, and a failing compiler that prints a matching version.

## Troubleshooting

- **Nightly Rust toolchain error**: Ensure `rustup toolchain install nightly-2023-03-28 --component rust-src` has been executed. The pinned target requires `-Zbuild-std=core`.
- **Target JSON not found**: Verify `powerpc-apple-macos.json` is present in `rust/`.
- **Undefined symbols at link time**: Ensure `build-rust.sh` has executed before `macmake build` so `librust_classic_ppc.a` exists in `rust/target/powerpc-apple-macos/release/`.

## Relevant CLI Help

- `macmake help targets`
- `macmake help libraries`
- `macmake help manifest`
- `macmake help build`
- `macmake help output`

