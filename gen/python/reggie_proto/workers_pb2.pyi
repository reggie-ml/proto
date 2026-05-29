from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorkerUpdate(_message.Message):
    __slots__ = ("job_id", "started", "progress", "completed", "failed")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    started: JobStarted
    progress: TrainingProgress
    completed: JobCompleted
    failed: JobFailed
    def __init__(self, job_id: _Optional[str] = ..., started: _Optional[_Union[JobStarted, _Mapping]] = ..., progress: _Optional[_Union[TrainingProgress, _Mapping]] = ..., completed: _Optional[_Union[JobCompleted, _Mapping]] = ..., failed: _Optional[_Union[JobFailed, _Mapping]] = ...) -> None: ...

class JobCommand(_message.Message):
    __slots__ = ("cancel",)
    CANCEL_FIELD_NUMBER: _ClassVar[int]
    cancel: CancelJob
    def __init__(self, cancel: _Optional[_Union[CancelJob, _Mapping]] = ...) -> None: ...

class CancelJob(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class JobStarted(_message.Message):
    __slots__ = ("worker_id",)
    WORKER_ID_FIELD_NUMBER: _ClassVar[int]
    worker_id: str
    def __init__(self, worker_id: _Optional[str] = ...) -> None: ...

class TrainingProgress(_message.Message):
    __slots__ = ("epoch", "total_epochs", "loss", "metrics")
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EPOCHS_FIELD_NUMBER: _ClassVar[int]
    LOSS_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    epoch: int
    total_epochs: int
    loss: float
    metrics: _containers.ScalarMap[str, float]
    def __init__(self, epoch: _Optional[int] = ..., total_epochs: _Optional[int] = ..., loss: _Optional[float] = ..., metrics: _Optional[_Mapping[str, float]] = ...) -> None: ...

class JobCompleted(_message.Message):
    __slots__ = ("model_artifact", "metrics", "training_duration_ms")
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    MODEL_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    model_artifact: bytes
    metrics: _containers.ScalarMap[str, float]
    training_duration_ms: int
    def __init__(self, model_artifact: _Optional[bytes] = ..., metrics: _Optional[_Mapping[str, float]] = ..., training_duration_ms: _Optional[int] = ...) -> None: ...

class JobFailed(_message.Message):
    __slots__ = ("error_message", "traceback")
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRACEBACK_FIELD_NUMBER: _ClassVar[int]
    error_message: str
    traceback: str
    def __init__(self, error_message: _Optional[str] = ..., traceback: _Optional[str] = ...) -> None: ...
