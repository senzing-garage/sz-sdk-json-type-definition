# Makefile for sz-sdk-json-type-definition.

# Detect the operating system and architecture.

include makefiles/osdetect.mk

# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------

# "Simple expanded" variables (':=')

# PROGRAM_NAME is the name of the GIT repository.
PROGRAM_NAME := $(shell basename `git rev-parse --show-toplevel`)
MAKEFILE_PATH := $(abspath $(firstword $(MAKEFILE_LIST)))
MAKEFILE_DIRECTORY := $(shell dirname $(MAKEFILE_PATH))
TARGET_DIRECTORY := $(MAKEFILE_DIRECTORY)/target
DIST_DIRECTORY := $(MAKEFILE_DIRECTORY)/dist
BUILD_TAG := $(shell git describe --always --tags --abbrev=0  | sed 's/v//')
BUILD_ITERATION := $(shell git log $(BUILD_TAG)..HEAD --oneline | wc -l | sed 's/^ *//')
BUILD_VERSION := $(shell git describe --always --tags --abbrev=0 --dirty  | sed 's/v//')
GIT_REMOTE_URL := $(shell git config --get remote.origin.url)
GIT_REPOSITORY_NAME := $(shell basename `git rev-parse --show-toplevel`)
GIT_VERSION := $(shell git describe --always --tags --long --dirty | sed -e 's/\-0//' -e 's/\-g.......//')
GO_PACKAGE_NAME := $(shell echo $(GIT_REMOTE_URL) | sed -e 's|^git@github.com:|github.com/|' -e 's|\.git$$||' -e 's|Senzing|senzing|')
PATH := $(MAKEFILE_DIRECTORY)/bin:$(PATH)

# Recursive assignment ('=')

GO_OSARCH = $(subst /, ,$@)
GO_OS = $(word 1, $(GO_OSARCH))
GO_ARCH = $(word 2, $(GO_OSARCH))

# Conditional assignment. ('?=')
# Can be overridden with "export"
# Example: "export LD_LIBRARY_PATH=/path/to/my/senzing/er/lib"

GOBIN ?= $(shell go env GOPATH)/bin

# Export environment variables.

.EXPORT_ALL_VARIABLES:

# -----------------------------------------------------------------------------
# The first "make" target runs as default.
# -----------------------------------------------------------------------------

.PHONY: default
default: help

# -----------------------------------------------------------------------------
# Operating System / Architecture targets
# -----------------------------------------------------------------------------

-include makefiles/$(OSTYPE).mk
-include makefiles/$(OSTYPE)_$(OSARCH).mk


.PHONY: hello-world
hello-world: hello-world-osarch-specific

# -----------------------------------------------------------------------------
# Dependency management
# -----------------------------------------------------------------------------

.PHONY: venv
venv: venv-osarch-specific


.PHONY: dependencies-for-development
dependencies-for-development: venv dependencies-for-development-osarch-specific
	@go install github.com/daixiang0/gci@latest
	@go install github.com/gotesttools/gotestfmt/v2/cmd/gotestfmt@latest
	@go install github.com/vladopajic/go-test-coverage/v2@latest
	@go install golang.org/x/tools/cmd/godoc@latest
	$(activate-venv); \
		python3 -m pip install --upgrade pip; \
		python3 -m pip install --requirement development-requirements.txt


.PHONY: dependencies
dependencies: venv
	@go get -u ./...
	@go get -t -u ./...
	@go mod tidy
	$(activate-venv); \
		python3 -m pip install --upgrade pip; \
		python3 -m pip install --requirement requirements.txt

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

.PHONY: setup
setup: setup-osarch-specific generate

# -----------------------------------------------------------------------------
# Lint
# -----------------------------------------------------------------------------

.PHONY: lint
lint: golangci-lint cspell

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Test
# -----------------------------------------------------------------------------

.PHONY: test
test: test-osarch-specific test-python test-go


.PHONY: test-go
test-go:
	@go run main.go
	@go test -v -p 1 ./...


.PHONY: test-python
test-python:
	$(activate-venv); \
		./bin/test_rfc8927_reconstitution.py; \
		./main.py; \
		pytest test.py --verbose

# -----------------------------------------------------------------------------
# Coverage
# -----------------------------------------------------------------------------

.PHONY: coverage
coverage: coverage-osarch-specific

# -----------------------------------------------------------------------------
# Documentation
# -----------------------------------------------------------------------------

.PHONY: documentation
documentation: documentation-osarch-specific

# -----------------------------------------------------------------------------
# Analyze
# -----------------------------------------------------------------------------

.PHONY: analyze
analyze:
	@./bin/analyze_rfc8927.py


.PHONY: pretty-print
pretty-print:
	@./bin/pretty_print.py

# -----------------------------------------------------------------------------
# Generate code
# -----------------------------------------------------------------------------

.PHONY: generate
generate: generate-code generate-tests


.PHONY: generate-code
generate-code: generate-csharp generate-go generate-java generate-python generate-ruby generate-rust generate-typescript


.PHONY: generate-csharp
generate-csharp: clean-csharp
	jtd-codegen \
		--csharp-system-text-namespace Senzing \
		--csharp-system-text-out ./csharp \
		--root-name senzingapi \
		senzingapi-RFC8927.json


.PHONY: generate-go
generate-go: clean-go
	jtd-codegen \
		--go-out ./go/typedef \
		--go-package typedef \
		--root-name senzingapi \
		senzingapi-RFC8927.json


.PHONY: generate-java
generate-java: clean-java
	jtd-codegen \
		--java-jackson-out ./java \
		--java-jackson-package com.senzing.schema \
		--root-name senzingapi \
		senzingapi-RFC8927.json


.PHONY: generate-python
generate-python: clean-python
	jtd-codegen \
		--python-out ./python/typedef \
		--root-name senzingapi \
		senzingapi-RFC8927.json


.PHONY: generate-ruby
generate-ruby: clean-ruby
	jtd-codegen \
		--root-name senzingapi \
		--ruby-module SenzingTypeDef \
		--ruby-out ./ruby \
		--ruby-sig-module SenzingSig \
		senzingapi-RFC8927.json


.PHONY: generate-rust
generate-rust: clean-rust
	jtd-codegen \
		--root-name senzingapi \
		--rust-out ./rust \
		senzingapi-RFC8927.json


.PHONY: generate-typescript
generate-typescript: clean-typescript
	jtd-codegen \
		--root-name senzingapi \
		--typescript-out ./typescript \
		senzingapi-RFC8927.json

# -----------------------------------------------------------------------------
# Generate tests
# -----------------------------------------------------------------------------

.PHONY: generate-tests
generate-tests: generate_typedef_test_go generate_testdata


.PHONY: generate_typedef_test_go
generate_typedef_test_go:
	@rm ./go/typedef/generated_typedef_test.go || true
	@./bin/generate_typedef_test_go.py


.PHONY: generate_testdata
generate_testdata:
	@rm $(MAKEFILE_DIRECTORY)/testdata/* || true
	@./bin/generate_testdata.py

# -----------------------------------------------------------------------------
# Clean
# -----------------------------------------------------------------------------

.PHONY: clean
clean: clean-osarch-specific
	@go clean -cache
	@go clean -testcache


.PHONY: clean-csharp
clean-csharp:
	@rm $(MAKEFILE_DIRECTORY)/csharp/* || true


.PHONY: clean-go
clean-go:
	@go clean -cache
	@go clean -testcache
	@rm -f $(GOPATH)/bin/$(PROGRAM_NAME) || true
	@rm $(MAKEFILE_DIRECTORY)/go/typedef/generated_typedef_test.go || true
	@rm $(MAKEFILE_DIRECTORY)/go/typedef/typedef.go || true


.PHONY: clean-java
clean-java:
	@rm $(MAKEFILE_DIRECTORY)/java/* || true


.PHONY: clean-python
clean-python:
	@rm -rf $(MAKEFILE_DIRECTORY)/python/typedef/* || true


.PHONY: clean-ruby
clean-ruby:
	@rm $(MAKEFILE_DIRECTORY)/ruby/* || true


.PHONY: clean-rust
clean-rust:
	@rm $(MAKEFILE_DIRECTORY)/rust/* || true


.PHONY: clean-typescript
clean-typescript:
	@rm $(MAKEFILE_DIRECTORY)/typescript/* || true


.PHONY: clean-generated
clean-generated: clean-csharp clean-go clean-java clean-python clean-ruby clean-rust clean-typescript

# -----------------------------------------------------------------------------
# Utility targets
# -----------------------------------------------------------------------------

.PHONY: help
help:
	$(info Build $(PROGRAM_NAME) version $(BUILD_VERSION)-$(BUILD_ITERATION))
	$(info Makefile targets:)
	@$(MAKE) -pRrq -f $(firstword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs


.PHONY: print-make-variables
print-make-variables:
	@$(foreach V,$(sort $(.VARIABLES)), \
		$(if $(filter-out environment% default automatic, \
		$(origin $V)),$(info $V=$($V) ($(value $V)))))


.PHONY: update-pkg-cache
update-pkg-cache:
	@GOPROXY=https://proxy.golang.org GO111MODULE=on \
		go get $(GO_PACKAGE_NAME)@$(BUILD_TAG)

# -----------------------------------------------------------------------------
# Specific programs
# -----------------------------------------------------------------------------

.PHONY: golangci-lint
golangci-lint:
	@${GOBIN}/golangci-lint run --config=.github/linters/.golangci.yaml
