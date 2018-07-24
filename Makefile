BUILD_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
DATA_DIR:=$(BUILD_DIR)/data

all: run

build:
	docker pull alephdata/memorious
	docker build -t alephdata/opensanctions .

run: build
	docker run -ti -v $(DATA_DIR):/data --name opensanctions alephdata/opensanctions /bin/bash
