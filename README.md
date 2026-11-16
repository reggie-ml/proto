# reggie-ml/proto

Protocol Buffer definitions for the Reggie ML workers.

## Usage

### Go module

```sh
go get github.com/reggie-ml/proto/gen/go@latest
```

```go
import workers "github.com/reggie-ml/proto/gen/go"
```

### Python package

```sh
pip install "reggie-proto @ git+https://github.com/reggie-ml/proto#subdirectory=gen/python"
```

```python
from reggie_proto import workers_pb2, workers_pb2_grpc
```

## Developing

Generated code is committed to the repo. After editing `workers.proto`, regenerate and commit the result:

```sh
make generate
```

## Releasing

Versions follow [semver](https://semver.org); the `VERSION` file is the source of truth.

| Change type | Version bump |
| --- | --- |
| New fields, new RPCs, non-breaking additions | patch or minor |
| Removal or rename of fields/RPCs, type changes | **major** |

To make a release:

1. In a PR, bump `VERSION`, run `make generate`, and merge to `master`.
2. Push the matching tag from `master`:

   ```sh
   git tag "v$(cat VERSION)" && git push origin "v$(cat VERSION)"
   ```
