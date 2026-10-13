# Getting Started

This guide follows the `examples/first-app` project included with the macMAKE v0.1.0 candidate. Check the [Downloads page](https://macmake.dev/downloads.html) for release availability; the candidate is not a public download until approved.

## Requirements

- Linux x86-64 (validated on Ubuntu 24.04; Debian 13 is the documented compatible baseline).
- macMAKE v0.1.0 and its bundled compiler/toolchain.
- Authorized CodeWarrior MSL archives and Apple Universal Interfaces inputs for this example. They are not included with macMAKE.

## Discover the installed CLI

The executable includes its version-specific manual and works offline:

```sh
macmake --version
macmake help
macmake help quickstart
macmake help manifest
macmake schema manifest --json
```

## Get the example project

The release archive includes the sample under `examples/first-app`. After installation, copy it into a writable project directory:

```sh
cp -a "$HOME/.local/share/macmake/current/examples/first-app" "$HOME/HelloPPC"
cd "$HOME/HelloPPC"
```

The sample has a separate license at `LICENSE.txt`; it does not contain SDK binaries or headers.

## Register the Universal Interfaces SDK

From an authorized CodeWarrior installation, register its Universal Interfaces directory:

```sh
macmake sdk add "$HOME/SDKs/Metrowerks CodeWarrior/MacOS Support/Universal" \
  --id macos9-sdk
macmake sdk verify macos9-sdk
```

The SDK catalog records the selected path and fingerprints. `sdk add` does not copy SDK files. Use only SDK material you are authorized to use.

## Supply the MSL archives

From the example directory, use the helper to copy the required MSL archives from your authorized CodeWarrior installation:

```sh
cd examples/first-app
./setup-user-msl.sh "$HOME/SDKs/Metrowerks CodeWarrior"
```

The helper reports the copied files' hashes. It does not add those files to macMAKE's distribution.

## Check and build

```sh
export MACMAKE_TOOLCHAIN_ROOT="$HOME/.local/share/macmake/current/toolchain"
macmake inspect .
macmake doctor . --target "Classic PPC C"
macmake build . --target "Classic PPC C"
```

The example manifest explicitly lists two C source files and requires the `macos9-sdk` registration and local MSL archives. Its build produces `build/HelloPPC/ClassicPPCC/HelloPPC.bin` (MacBinary II), `HelloPPC.pef`, `HelloPPC.rsrc`, Finder metadata, and build evidence. This tiny program opens no window and returns through the MSL startup path.

Inspect the generated application:

```sh
macmake inspect-artifact build/HelloPPC/ClassicPPCC/HelloPPC.pef \
  --resource-fork build/HelloPPC/ClassicPPCC/HelloPPC.rsrc \
  --finder-info build/HelloPPC/ClassicPPCC/.finf/HelloPPC.APPL \
  --creator HmPP --file-type APPL --json
```

A successful Linux build and structural artifact inspection do not establish Mac OS 9 runtime behavior. Runtime testing requires transferring the MacBinary application to a Mac OS 9 environment and launching it there.

For full syntax, side effects, and troubleshooting, use `macmake help build`, `macmake help sdk`, `macmake help output`, and `macmake help troubleshooting` in the installed CLI.
