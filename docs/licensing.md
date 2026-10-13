# Licensing for macMAKE v0.1.0

**Release status:** the v0.1.0 package and license text are staged for review. The proposed proprietary terms below have not yet received final MPLS LLC or qualified legal approval, and no public binary release is authorized.

macMAKE is a mixed distribution. The proprietary macMAKE executable and separately licensed toolchain components have distinct license boundaries. The proprietary license applies only to the files it identifies; it does not override the license or redistribution rights of third-party components.

## Proprietary macMAKE executable

The macMAKE CLI and original macMAKE product implementation are proprietary and closed-source. The proposed [macMAKE Proprietary Binary License](../LICENSE) permits free personal, educational, research, nonprofit, and commercial development use, including use from scripts, coding agents, CI, and automated build environments. It permits installations and reasonable internal backup copies within an individual's or organization's authorized environment. It restricts public redistribution, mirroring, resale, sublicensing, and distribution of modified proprietary executable copies unless MPLS LLC expressly authorizes that channel. The exact text remains subject to MPLS LLC owner and qualified legal approval.

The proposed license states that developers retain ownership and licensing control of independent applications they create with macMAKE. It does not itself govern any third-party runtime code incorporated into an application. The release candidate also carries a separate proposed license for `examples/first-app`, allowing users to incorporate and distribute that example as part of their own applications. Both license texts require MPLS LLC approval before publication.

## GNU compiler and Binutils

The distribution includes separate GNU GCC 12.2.0 and GNU Binutils 2.46.1 executables. Their source and binaries retain their applicable GNU licenses and may be copied or redistributed as those licenses permit. The proprietary macMAKE terms do not restrict those rights.

The exact v0.1.0 source preparation is associated with the proposed immutable tag [`macmake-v0.1.0-toolchain-sources`](https://github.com/mplsllc/macmake-gpl/releases/tag/macmake-v0.1.0-toolchain-sources), source revision `c3efc1504e0c2c005b4402c98a325bef7a0065e0`. Its prepared archive is `macmake-v0.1.0-toolchain-corresponding-source.tar.xz`, SHA-256 `fde5254ecda60264e7e0ab25098e74c3b6108de34e506f2d3941011059923a96`. It contains the complete GCC 12.2.0 and Binutils 2.46.1 upstream source archives, the exact GCC patch, compiler and runtime build scripts/configuration, runtime source provenance, notices, and packaged component hashes. The tag and archive remain unpublished; the source release must be made accessible no later than the covered binary release.

The separately staged Linux x86-64 binary candidate is `macmake-v0.1.0-linux-x86_64.tar.xz`, SHA-256 `3c9da84e53022d16a07208d0591a9964b8399dbe043b3628e227373a6aa6e980`. It preserves the validated RC2.2 executable (`80531f6794f74345991854e5f94e53cd872fcb382051000f24732304341971f7`); no compiler or product executable was rebuilt for final packaging. Neither the binary nor source archive is publicly available.

The RC2.2 toolchain inputs verified for this package include GCC 12.2.0 patch SHA-256 `20d025ecf9f4d83da5144ce5f03d9b9d382df53c986ab7152d9a2766910c16c9`, packaged `libgcc.a` SHA-256 `9204ff56371500f9aa92401623ec2a2877918396498b87ad40943980458928aa`, and packaged `crtdbase.o` SHA-256 `01ab3b224d6906fa3f6a1fb9dd61d062a9685b6102d5ca02b9a3b69f38b5be4f`. The source files and their individual notices determine whether the GCC Runtime Library Exception applies. The C sample selected `__main.o` and `_ctors.o` from `libgcc.a`; it did not link `crtdbase.o`. A qualified review of the exact package and build workflow remains outstanding.

## Other third-party dependencies

Rust dependency notices and license texts are included separately in the release archive under `licenses/`. Binutils carries its GNU and bundled zlib license notices; GCC carries GPL and runtime exception notices. Each component remains under its own terms. The complete release manifest and notices identify packaged components.

## User-supplied historical development files

The distribution does not include Apple Universal Interfaces, Metrowerks MSL, CodeWarrior archives, or other nonredistributable historical SDK material. Users must provide files they are authorized to use and register them with the installed CLI. Those user-supplied files are not covered by macMAKE's proprietary license or included in the GPL corresponding-source package.

## Legal review boundary

This document records the prepared component inventory and proposed license boundary; it is not legal advice or a statement of legal clearance. Counsel should review the GPL treatment of the distributed GCC/Binutils programs, GCC runtime object files, the aggregate archive, corresponding-source access, and the actual CFM/PEF application compilation and linking workflow before public distribution.
