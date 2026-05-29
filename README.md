# reggie-ml/proto

Protocol Buffer definitions for the Reggie ML workers.

## Using the Go module

```go
import workers "github.com/reggie-ml/proto/gen/go"
```

```sh
go get github.com/reggie-ml/proto/gen/go@latest
```

## Versioning

Releases follow [semver](https://semver.org) and are tracked in the `VERSION` file.

| Change type | Version bump |
| --- | --- |
| New fields, new RPCs, non-breaking additions | patch or minor |
| Removal or rename of fields/RPCs, type changes | **major** |
