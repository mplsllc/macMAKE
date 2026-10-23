#!/usr/bin/env bash
set -euo pipefail

example_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
rust_root="$example_root/rust"
output_dir="$example_root/build/rust"
rlib="$rust_root/target/powerpc-apple-macos/release/libmacmake_rust_value.rlib"

mkdir -p -- "$output_dir"
(
    cd -- "$rust_root"
    # Capture first: grep -q can close a pipe early and cause rustc to SIGPIPE.
    rustc_version=$(rustc -vV)
    grep -Fq 'commit-hash: 2036fdd24f77d607dcfaa24c48fbe85d3f785823' <<<"$rustc_version"
    cargo build --manifest-path Cargo.toml \
        -Zbuild-std=core \
        -Zbuild-std-features=compiler-builtins-mem \
        --release --target "$rust_root/powerpc-apple-macos.json"
)

mapfile -t members < <(ar t "$rlib" | rg '\.rcgu\.o$')
if [[ "${#members[@]}" -ne 1 ]]; then
    printf 'expected one Rust XCOFF object in %s, found %s\n' "$rlib" "${#members[@]}" >&2
    exit 1
fi
ar p "$rlib" "${members[0]}" > "$output_dir/macmake_rust_value.o"

python3 - "$output_dir/macmake_rust_value.o" <<'PY'
import pathlib
import sys

path = pathlib.Path(sys.argv[1])
data = path.read_bytes()
if data[:2] != b"\x01\xdf":
    raise SystemExit(f"Rust output is not a big-endian PowerPC XCOFF32 object: {path}")
print(f"Rust PowerPC XCOFF object: {path} ({len(data)} bytes)")
PY
