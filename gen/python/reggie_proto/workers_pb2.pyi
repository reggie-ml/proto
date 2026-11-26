from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STAGE_UNSPECIFIED: _ClassVar[Stage]
    STAGE_LOADING_DATA: _ClassVar[Stage]
    STAGE_PREPROCESSING: _ClassVar[Stage]
    STAGE_TRAINING: _ClassVar[Stage]
    STAGE_EVALUATING: _ClassVar[Stage]
    STAGE_SAVING: _ClassVar[Stage]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_LEVEL_UNSPECIFIED: _ClassVar[LogLevel]
    LOG_LEVEL_DEBUG: _ClassVar[LogLevel]
    LOG_LEVEL_INFO: _ClassVar[LogLevel]
    LOG_LEVEL_WARNING: _ClassVar[LogLevel]
    LOG_LEVEL_ERROR: _ClassVar[LogLevel]

class ArtifactFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARTIFACT_FORMAT_UNSPECIFIED: _ClassVar[ArtifactFormat]
    ARTIFACT_FORMAT_PICKLE: _ClassVar[ArtifactFormat]
    ARTIFACT_FORMAT_KERAS: _ClassVar[ArtifactFormat]
    ARTIFACT_FORMAT_ONNX: _ClassVar[ArtifactFormat]
STAGE_UNSPECIFIED: Stage
STAGE_LOADING_DATA: Stage
STAGE_PREPROCESSING: Stage
STAGE_TRAINING: Stage
STAGE_EVALUATING: Stage
STAGE_SAVING: Stage
LOG_LEVEL_UNSPECIFIED: LogLevel
LOG_LEVEL_DEBUG: LogLevel
LOG_LEVEL_INFO: LogLevel
LOG_LEVEL_WARNING: LogLevel
LOG_LEVEL_ERROR: LogLevel
ARTIFACT_FORMAT_UNSPECIFIED: ArtifactFormat
ARTIFACT_FORMAT_PICKLE: ArtifactFormat
ARTIFACT_FORMAT_KERAS: ArtifactFormat
ARTIFACT_FORMAT_ONNX: ArtifactFormat

class WorkerMessage(_message.Message):
    __slots__ = ("run_id", "started", "progress", "log", "heartbeat", "artifact_chunk", "completed", "failed", "cancelled")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_CHUNK_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    started: RunStarted
    progress: Progress
    log: LogLine
    heartbeat: Heartbeat
    artifact_chunk: ArtifactChunk
    completed: RunCompleted
    failed: RunFailed
    cancelled: RunCancelled
    def __init__(self, run_id: _Optional[str] = ..., started: _Optional[_Union[RunStarted, _Mapping]] = ..., progress: _Optional[_Union[Progress, _Mapping]] = ..., log: _Optional[_Union[LogLine, _Mapping]] = ..., heartbeat: _Optional[_Union[Heartbeat, _Mapping]] = ..., artifact_chunk: _Optional[_Union[ArtifactChunk, _Mapping]] = ..., completed: _Optional[_Union[RunCompleted, _Mapping]] = ..., failed: _Optional[_Union[RunFailed, _Mapping]] = ..., cancelled: _Optional[_Union[RunCancelled, _Mapping]] = ...) -> None: ...

class ConductorMessage(_message.Message):
    __slots__ = ("cancel",)
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    cancel: CancelRun
    def __init__(self, cancel: _Optional[_Union[CancelRun, _Mapping]] = ...) -> None: ...

class CancelRun(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class RunStarted(_message.Message):
    __slots__ = ("worker_id", "worker_version")
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKER_VERSION_FIELD_NUMBER: _ClassVar[int]
    worker_id: str
    worker_version: str
    def __init__(self, worker_id: _Optional[str] = ..., worker_version: _Optional[str] = ...) -> None: ...

class Progress(_message.Message):
    __slots__ = ("stage", "epoch", "total_epochs", "loss", "metrics")
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    STAGE_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    stage: Stage
    epoch: int
    total_epochs: int
    loss: float
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, stage: _Optional[_Union[Stage, str]] = ..., epoch: _Optional[int] = ..., total_epochs: _Optional[int] = ..., loss: _Optional[float] = ..., metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...

class LogLine(_message.Message):
    __slots__ = ("level", "message", "time_unix_ms", "logger")
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    LOGGER_FIELD_NUMBER: _ClassVar[int]
    level: LogLevel
    message: str
    time_unix_ms: int
    logger: str
    def __init__(self, level: _Optional[_Union[LogLevel, str]] = ..., message: _Optional[str] = ..., time_unix_ms: _Optional[int] = ..., logger: _Optional[str] = ...) -> None: ...

class Heartbeat(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ArtifactChunk(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class RunCompleted(_message.Message):
    __slots__ = ("artifact_format", "framework", "framework_version", "artifact_size_bytes", "artifact_sha256", "metrics", "training_duration_ms")
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    ARTIFACT_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_VERSION_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_SHA256_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    artifact_format: ArtifactFormat
    framework: str
    framework_version: str
    artifact_size_bytes: int
    artifact_sha256: str
    metrics: _containers.ScalarMap[str, float]
    training_duration_ms: int
    def __init__(self, artifact_format: _Optional[_Union[ArtifactFormat, str]] = ..., framework: _Optional[str] = ..., framework_version: _Optional[str] = ..., artifact_size_bytes: _Optional[int] = ..., artifact_sha256: _Optional[str] = ..., metrics: _Optional[_Mapping[str, float]] = ..., training_duration_ms: _Optional[int] = ...) -> None: ...

class RunFailed(_message.Message):
    __slots__ = ("error_message", "traceback")
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRACEBACK_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    traceback: str
    def __init__(self, error_message: _Optional[str] = ..., traceback: _Optional[str] = ...) -> None: ...

class RunCancelled(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...
