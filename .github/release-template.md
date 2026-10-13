# macMAKE Release Notes Template

## Corresponding Source for Open-Source Components

This binary distribution includes separately licensed GNU GCC and GNU Binutils components. Their applicable licenses and notices are preserved; the corresponding source archives, patches, build scripts, and configuration manifests for the exact toolchain binaries in this release are available at:

- **Source Repository:** [mplsllc/macmake-gpl](https://github.com/mplsllc/macmake-gpl)
- **Source Release:** [`<CORRESPONDING_SOURCE_TAG>`](https://github.com/mplsllc/macmake-gpl/releases/tag/<CORRESPONDING_SOURCE_TAG>)
- **Distribution Manifest:** [`corresponding-source-manifest.json`](https://github.com/mplsllc/macmake-gpl/blob/<CORRESPONDING_SOURCE_TAG>/corresponding-source-manifest.json)

> **Maintainer Instructions for Releases:**  
> Replace `<CORRESPONDING_SOURCE_TAG>` with the immutable source release tag for the exact compiler and Binutils binaries in the release. For macMAKE v0.1.0, use `macmake-v0.1.0-toolchain-sources`; the older `v0.1.1-toolchain-sources` tag does not correspond to this binary.

### Component Identifiers & Source Digests (Reference)
- **GCC 12.2.0 (`powerpc-unknown-macmake`)**:
  - Archive: `gcc-12.2.0.tar.xz` (SHA-256: `e549cf9cf3594a00e27b6589d4322d70e0720cdd213f39beb4181e06926230ff`)
  - Patch: `gcc/gcc-12.2.0.patch` (SHA-256: `20d025ecf9f4d83da5144ce5f03d9b9d382df53c986ab7152d9a2766910c16c9`)
  - Configure: `--target=powerpc-unknown-macmake --enable-languages=c --disable-bootstrap --disable-multilib --disable-libstdcxx --without-headers --prefix=<build-root>/install --with-build-time-tools=<build-root>/build/build-time-tools`
  - The v0.1.0 toolchain builds and distributes `libgcc.a`; its build does not use `--disable-libgcc`. The supported frontend set is C.
- **GNU Binutils 2.46.1 (`powerpc-ibm-aix7.1.0.0`)**:
  - Archive: `binutils-2.46.1.tar.xz` (SHA-256: `e127a709cba24c76de8936cb7083dd768f28cd37eb010492e2f19b71eb1294e4`)
  - Configure: `--target=powerpc-ibm-aix7.1.0.0 --disable-nls --disable-werror --disable-gold --disable-ld --disable-gdb --disable-sim --disable-gprofng --enable-gas --enable-binutils`
