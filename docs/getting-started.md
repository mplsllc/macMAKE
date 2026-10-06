# Getting Started

macMAKE is currently under active development. Binary releases for Linux hosts will be published via GitHub Releases on this repository once the public preview milestone is reached.

---

## Prerequisites (Preview)

When binary releases become available, the general host requirements will be:

- **Operating System:** 64-bit Linux (x86_64)
- **User-Supplied SDKs:** For projects targeting Classic Mac OS (System 7 through Mac OS 9), users will need to provide their own historical SDK files (such as Apple Universal Interfaces 3.4 or CodeWarrior libraries) located on their local machine.

---

## Installation

Full installation instructions, package archives, and setup guides will accompany the first binary release.

---

## Typical Workflow (Planned)

Once installed, building a project with macMAKE is designed to be straightforward:

```sh
# Inspect a project model and target configuration
macmake inspect path/to/project

# Build the default target
macmake build path/to/project
```

Stay tuned for release announcements on [macmake.dev](https://macmake.dev) and the GitHub Releases page.
