# macMAKE Release Notes Template

## Corresponding Source for Open-Source Components

This binary distribution bundles or invokes open-source components covered by the GNU General Public License (GPLv3). In accordance with their respective licenses, the corresponding source archives, patches, build scripts, and configuration manifests for the exact toolchain binaries included in or used by this release are available at:

- **Source Repository:** [mplsllc/macmake-gpl](https://github.com/mplsllc/macmake-gpl)
- **Source Release:** [`<CORRESPONDING_SOURCE_TAG>`](https://github.com/mplsllc/macmake-gpl/releases/tag/<CORRESPONDING_SOURCE_TAG>)
- **Distribution Manifest:** [`corresponding-source-manifest.json`](https://github.com/mplsllc/macmake-gpl/blob/<CORRESPONDING_SOURCE_TAG>/corresponding-source-manifest.json)

> **Maintainer Instructions for Releases:**  
> When creating a macMAKE binary release, replace `<CORRESPONDING_SOURCE_TAG>` with the exact, immutable source release tag (for example, `v0.1.1-toolchain-sources`) corresponding to the compiler and binutils binaries shipped with that specific macMAKE version.

### Component Identifiers & Source Digests (Reference)
- **GCC 12.2.0 (`powerpc-unknown-macmake`)**:
  - Archive: `gcc-12.2.0.tar.xz` (SHA-256: `e549cf9cf3594a00e27b6589d4322d70e0720cdd213f39beb4181e06926230ff`)
  - Patch: `gcc/gcc-12.2.0.patch` (SHA-256: `bc37e4d7c7de86ccec1fb4bfc3c768d2e29cbfe68ace301fccfde01eb59b8c63`)
  - Configure: `--target=powerpc-unknown-macmake --enable-languages=c,c++ --disable-bootstrap --disable-multilib --disable-libgcc --disable-libstdcxx --without-headers`
- **GNU Binutils 2.46.1 (`powerpc-ibm-aix7.1.0.0`)**:
  - Archive: `binutils-2.46.1.tar.xz` (SHA-256: `e127a709cba24c76de8936cb7083dd768f28cd37eb010492e2f19b71eb1294e4`)
  - Configure: `--target=powerpc-ibm-aix7.1.0.0 --disable-nls --disable-werror --disable-gold --disable-ld --disable-gdb --disable-sim --disable-gprofng --enable-gas --enable-binutils`
