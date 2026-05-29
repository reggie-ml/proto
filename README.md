# reggie-ml/proto

Protocol Buffer definitions for the Reggie ML workers.

## Using the Go module

```go
import workers "github.com/reggie-ml/proto/gen/go"
```

```sh
go get github.com/reggie-ml/proto/gen/go@latest
```

## Using the Python package

The generated Python stubs are packaged as `reggie-proto` under `gen/python`.
Pin to a release tag the same way the Go module is consumed:

```sh
pip install "reggie-proto @ git+https://github.com/reggie-ml/proto@v0.1.0#subdirectory=gen/python"
```

```python
from reggie_proto import workers_pb2, workers_pb2_grpc
```

## Versioning

Releases follow [semver](https://semver.org) and are tracked in the `VERSION` file.

| Change type | Version bump |
| --- | --- |
| New fields, new RPCs, non-breaking additions | patch or minor |
| Removal or rename of fields/RPCs, type changes | **major** |
