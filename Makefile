# Makefile for nusprint project

# Convenience variables
DOCKER_IMAGE = nusprint:dev
CONTAINER_NAME = nusprint_dev
PROJECT_DIR = $(PWD)

.PHONY: up shell sanity train_cp eval_cp timing demo

up:
	docker build -t $(DOCKER_IMAGE) -f env/Dockerfile .

shell:
	docker run --rm --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) -it \
		--gpus all \
		-v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes \
		--env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache \
		$(DOCKER_IMAGE) bash

sanity:
	docker run --rm --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) \
		--gpus all \
		-v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes \
		--env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache \
		$(DOCKER_IMAGE) python3 scripts/sanity.py

train_cp:
	docker run --rm --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --gpus all -v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes --env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache $(DOCKER_IMAGE) \
		python3 scripts/train_centerpoint.py

eval_cp:
	docker run --rm --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --gpus all -v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes --env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache $(DOCKER_IMAGE) \
		python3 scripts/eval_centerpoint.py

timing:
	docker run --rm --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --gpus all -v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes --env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache $(DOCKER_IMAGE) \
		python3 scripts/timing.py

demo:

bev:
	docker run --rm --user $(shell id -u):$(shell id -g) --gpus all \
		-v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes \
		--env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache \
		$(DOCKER_IMAGE) python3 scripts/bev_preview.py
	docker run --rm --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --user $(shell id -u):$(shell id -g) --gpus all -v $(PROJECT_DIR):/workspace -v /home/deepak/data/sets/nuscenes:/data/nuscenes --env-file env/.env -e MPLCONFIGDIR=/workspace/.mplcache $(DOCKER_IMAGE) \
		python3 scripts/demo.py

