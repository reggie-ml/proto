# proto

The gRPC contract between the Reggie ML **conductor** (Go, gRPC server) and its **workers**
(gRPC clients, e.g. `reggie-ml/worker-py`). Everything downstream depends on this repo.

- `workers.proto`: the one source file (`WorkerService` with a single bidi stream: worker sends
  `WorkerUpdate` (started/progress/completed/failed), conductor sends `JobCommand` (cancel)).
- `gen/go/`: generated Go code, its own Go module `github.com/reggie-ml/proto/gen/go`
  (package name `_go`, so consumers alias the import: `pb "github.com/reggie-ml/proto/gen/go"`).
- `gen/python/`: generated Python package `reggie-proto` (`reggie_proto.workers_pb2`, `_grpc`, `.pyi`).
- **Everything under `gen/` is generated and committed. Never hand-edit it.**

If you're in the `reggie-ml/workspace` checkout, use the `/proto-change` skill. A contract
change isn't done until conductor and worker-py are updated (`../scripts/check-sync.py`).

## Commands

```sh
buf lint
buf breaking --against ".git#tag=$(git tag --sort=-version:refname | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$' | head -1)"
make generate        # buf generate + fix python grpc import + sync VERSION into gen/python/pyproject.toml
(cd gen/go && go build ./...)
```
`make generate` needs `buf`, `protoc-gen-go`, `protoc-gen-go-grpc` on PATH (`~/go/bin`) and
network access (the Python plugins are remote `buf.build` plugins). Always commit the regenerated
`gen/` together with the `.proto` change. CI regenerates and fails if `gen/` differs.

## Versioning & releases

- `VERSION` is the source of truth. Semver table in `README.md`: additive is patch/minor,
  removing/renaming fields or RPCs or changing types is **major**. At 0.x, ask the user which
  bump to use for breaking changes.
- Never reuse field numbers. Mark removed ones `reserved`.
- Release = bump `VERSION` in a PR → merge to `master` → push tag `v$(cat VERSION)` (only when the
  user asks; see `/release`). `release.yml` verifies the tag matches `VERSION`, creates the
  `gen/go/vX.Y.Z` tag the Go submodule needs, and a GitHub release.
- CI: `verify.yml` on PRs (lint, breaking-change check vs last tag, regenerate + diff, Go build,
  Python import). `release.yml` on tags.

## Rules

- `master` is protected: work on a branch, open a PR. Never push to `master`, never push tags
  without explicit approval.
- Keep comments in `workers.proto` accurate. They're the only documentation of the stream
  lifecycle (which message comes first, when the stream closes).
