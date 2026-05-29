.PHONY: generate

generate:
	buf generate
	sed -i 's/^import workers_pb2 as/from reggie_proto import workers_pb2 as/' \
		gen/python/reggie_proto/workers_pb2_grpc.py
	sed -i "s/^version = \".*\"/version = \"$$(cat VERSION)\"/" \
		gen/python/pyproject.toml
