start:
	export INGESTION_OBJECT_STORE_PATH=$(shell pwd)/ingestion/object_store && \
	docker-compose up --build

stop:
	export INGESTION_OBJECT_STORE_PATH=$(shell pwd)/ingestion/object_store && \
	docker-compose down
