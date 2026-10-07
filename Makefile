# Makefile for sz-sdk-json-type-definition.

# Detect the operating system and architecture.

include makefiles/osdetect.mk

# Tool versions, shared across OS-specific makefiles.

include makefiles/versions.mk

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
# PATH := $(MAKEFILE_DIRECTORY)/bin:$(PATH)

# Recursive assignment ('=')

SHELL=/bin/bash
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
dependencies-for-development: venv dependencies-for-development-osarch-specific download-truthsets
	@go install github.com/bombsimon/wsl/v5/cmd/wsl@latest
	@go install github.com/daixiang0/gci@latest
	@go install github.com/gotesttools/gotestfmt/v2/cmd/gotestfmt@latest
	@go install github.com/vladopajic/go-test-coverage/v2@latest
	@go install golang.org/x/tools/cmd/godoc@latest
	@go install golang.org/x/vuln/cmd/govulncheck@latest
	@go install mvdan.cc/gofumpt@latest
	@sudo npm install -g cspell@latest
	$(activate-venv); \
		python3 -m pip install --upgrade pip; \
		python3 -m pip install --group all


.PHONY: dependencies
dependencies: venv
	@go get -u ./...
	@go get -t -u ./...
	@go mod tidy
	$(activate-venv); \
		python3 -m pip install --upgrade pip; \
		python3 -m pip install -e .

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

.PHONY: version
version: \
	clean \
	setup \
	documentation

# -----------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------

.PHONY: setup
setup: \
	setup-osarch-specific \
	load-database-with-truthsets \
	generate

# -----------------------------------------------------------------------------
# Lint
# -----------------------------------------------------------------------------

.PHONY: lint
lint: \
	pylint \
	golangci-lint \
	govulncheck \
	cspell \
	analyze-RFC8927 \
	pretty-print

# -----------------------------------------------------------------------------
# Build
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------------

.PHONY: run-java
run-java:
	java -jar target/example-0.0.1.jar

# -----------------------------------------------------------------------------
# Test
# -----------------------------------------------------------------------------

.PHONY: test
test: \
	test-go \
	test-csharp \
	test-java \
	test-python \
	test-osarch-specific \
	test-using-senzing \
	test-using-testdata-responses \
	test-rfc8927-reconstitution

# 	test-typescript \


.PHONY: test-verbose
test-verbose: test-verbose-osarch-specific


.PHONY: test-csharp
test-csharp:
	@dotnet run --project csharp || true


.PHONY: test-go
test-go: load-database-with-truthsets
	@go run main.go
	@go test -v -p 1 ./...


.PHONY: test-java
test-java:
	@mvn --file java/pom.xml install
	@mvn --file pom.xml package
	java -jar target/example-0.0.1.jar


.PHONY: test-python
test-python:
	$(activate-venv); \
		./main.py; \
		pytest test.py --verbose


.PHONY: test-typescript
test-typescript:
	@tsc main.ts || true
	@node main.js

# -----------------------------------------------------------------------------
# Coverage
# -----------------------------------------------------------------------------

.PHONY: coverage
coverage: coverage-osarch-specific


.PHONY: check-coverage
check-coverage: export SENZING_LOG_LEVEL=TRACE
check-coverage:
	@go test ./... -coverprofile=./cover.out -covermode=atomic -coverpkg=./...
	@${GOBIN}/go-test-coverage --config=.github/coverage/testcoverage.yaml

# -----------------------------------------------------------------------------
# Package
# -----------------------------------------------------------------------------

.PHONY: package
package: package-python


.PHONY: package-python
package-python:
	$(activate-venv); \
		python3 -m build

# -----------------------------------------------------------------------------
# Generate code
# -----------------------------------------------------------------------------

.PHONY: generate
generate: \
	generate-code \
	generate-tests


.PHONY: generate-code
generate-code: \
	generate-csharp \
	generate-go \
	generate-java \
	generate-python \
	generate-ruby \
	generate-rust \
	generate-typescript \
	go-typedef-generated-typedef-test-go


.PHONY: generate-csharp
generate-csharp: clean-csharp
	jtd-codegen \
		--csharp-system-text-namespace Senzing.Typedef \
		--csharp-system-text-out ./csharp/Senzing.Typedef \
		--root-name senzingsdk \
		senzingsdk-RFC8927.json
	@for file in $(MAKEFILE_DIRECTORY)/csharp/Senzing.Typedef/*; do \
		sed -i '2i #pragma warning disable CS8601, CS8618' "$$file"; \
	done


.PHONY: generate-go
generate-go: clean-go
	jtd-codegen \
		--go-out ./go/typedef \
		--go-package typedef \
		--root-name senzingsdk \
		senzingsdk-RFC8927.json


.PHONY: generate-java
generate-java: clean-java
	jtd-codegen \
		--java-jackson-out ./java/src/main/java/com/senzing/typedef \
		--java-jackson-package com.senzing.typedef \
		--root-name senzingsdk \
		senzingsdk-RFC8927.json


.PHONY: generate-python
generate-python: clean-python
	jtd-codegen \
		--python-out ./python/senzing_typedef \
		--root-name senzingsdk \
		senzingsdk-RFC8927.json


.PHONY: generate-ruby
generate-ruby: clean-ruby
	jtd-codegen \
		--root-name senzingsdk \
		--ruby-module SenzingTypedef \
		--ruby-out ./ruby \
		--ruby-sig-module SenzingSig \
		senzingsdk-RFC8927.json


.PHONY: generate-rust
generate-rust: clean-rust
	jtd-codegen \
		--root-name senzingsdk \
		--rust-out ./rust \
		senzingsdk-RFC8927.json


.PHONY: generate-typescript
generate-typescript: clean-typescript
	jtd-codegen \
		--root-name senzingsdk \
		--typescript-out ./typescript \
		senzingsdk-RFC8927.json

# -----------------------------------------------------------------------------
# Generate tests
# -----------------------------------------------------------------------------

.PHONY: go-typedef-generated-typedef-test-go
go-typedef-generated-typedef-test-go:
	@rm ./go/typedef/generated_typedef_test.go || true
	$(activate-venv); \
		./bin/make_go_typedef_generated_typedef_test_go.py


.PHONY: testdata-responses
testdata-responses: clean-testdata-responses
	$(activate-venv); \
		./bin/make_testdata_responses.py


.PHONY: testdata-responses-th4
testdata-responses-th4: clean-testdata-responses-th4
	$(activate-venv); \
		./bin/make_testdata_responses_th4.py


.PHONY: testdata-responses-truthsets
testdata-responses-truthsets: clean-testdata-responses-truthsets
	$(activate-venv); \
		./bin/make_testdata_responses_truthsets.py


.PHONY: generate-tests
generate-tests: \
	go-typedef-generated-typedef-test-go \
	testdata-responses-truthsets \
	testdata-responses

# -----------------------------------------------------------------------------
# Generate documentation
# -----------------------------------------------------------------------------

.PHONY: docs-json-key-descriptions
docs-json-key-descriptions:
	$(activate-venv); \
		./bin/make_docs_json_key_descriptions.py


.PHONY: docs-json-keys-used
docs-json-keys-used:
	$(activate-venv); \
		./bin/make_docs_json_keys_used.py


.PHONY: docs-labels-used
docs-labels-used:
	$(activate-venv); \
		./bin/make_docs_labels_used.py


.PHONY: docs-responses-html
docs-responses-html: clean-docs-responses-html
	$(activate-venv); \
		./bin/make_docs_responses_html.py


.PHONY: docs-responses-json
docs-responses-json: clean-docs-responses-json
	$(activate-venv); \
		./bin/make_docs_responses_json.py


.PHONY: unused-json-keys
unused-json-keys:
	$(activate-venv); \
		./bin/unused_json_keys.py


.PHONY: documentation
documentation: \
	docs-json-key-descriptions \
	docs-json-keys-used \
	docs-labels-used \
	docs-responses-html \
	docs-responses-json \
	unused-json-keys \
	documentation-osarch-specific

# -----------------------------------------------------------------------------
# Clean
# -----------------------------------------------------------------------------

.PHONY: clean
clean: clean-osarch-specific
	@go clean -cache
	@go clean -testcache


.PHONY: clean-csharp
clean-csharp:
	@dotnet clean $(MAKEFILE_DIRECTORY)/csharp
	@rm $(MAKEFILE_DIRECTORY)/csharp/Senzing.Typedef/* || true


.PHONY: clean-docs-responses-html
clean-docs-responses-html:
	@rm $(MAKEFILE_DIRECTORY)/docs/responses-html/* || true


.PHONY: clean-docs-responses-json
clean-docs-responses-json:
	@rm $(MAKEFILE_DIRECTORY)/docs/responses-json/* || true


.PHONY: clean-docs
clean-docs: clean-docs-responses-html clean-docs-responses-json
	@rm $(MAKEFILE_DIRECTORY)/docs/json_key_descriptions.json || true
	@rm $(MAKEFILE_DIRECTORY)/docs/json_keys_used.json || true
	@rm $(MAKEFILE_DIRECTORY)/docs/labels_used.json || true


.PHONY: clean-go
clean-go:
	@go clean -cache
	@go clean -testcache
	@rm -f $(GOPATH)/bin/$(PROGRAM_NAME) || true
	@rm $(MAKEFILE_DIRECTORY)/go/typedef/generated_typedef_test.go || true
	@rm $(MAKEFILE_DIRECTORY)/go/typedef/typedef.go || true


.PHONY: clean-java
clean-java:
	@mvn --file java/pom.xml clean
	@mvn --file pom.xml clean
	@rm java/src/main/java/com/senzing/typedef/*.java || true


.PHONY: clean-python
clean-python:
	@rm -rf $(MAKEFILE_DIRECTORY)/python/senzing_typedef/* || true


.PHONY: clean-ruby
clean-ruby:
	@rm $(MAKEFILE_DIRECTORY)/ruby/* || true


.PHONY: clean-rust
clean-rust:
	@rm $(MAKEFILE_DIRECTORY)/rust/* || true


.PHONY: clean-testdata-responses
clean-testdata-responses:
	@find $(MAKEFILE_DIRECTORY)/testdata/responses/ -type f -name "*.jsonl" -delete


.PHONY: clean-testdata-responses-th4
clean-testdata-responses-th4:
	@find $(MAKEFILE_DIRECTORY)/testdata/responses_th4/ -type f -name "*.jsonl" -delete


.PHONY: clean-testdata-responses-truthsets
clean-testdata-responses-truthsets:
	@find $(MAKEFILE_DIRECTORY)/testdata/responses_truthsets/ -type f -name "*.jsonl" -delete


.PHONY: clean-typescript
clean-typescript:
	@rm $(MAKEFILE_DIRECTORY)/typescript/* || true


.PHONY: clean-generated
clean-generated: clean-csharp clean-go clean-java clean-python clean-ruby clean-rust clean-typescript clean-docs


.PHONY: restore
restore:
	git restore testdata/responses_truthsets/*.jsonl
	git restore testdata/responses/*.jsonl

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

.PHONY: analyze-RFC8927
analyze-RFC8927:
	$(activate-venv); \
		./bin/analyze_rfc8927.py


.PHONY: bearer
bearer:
	@bearer scan --config-file .github/linters/bearer.yml .


.PHONY: black
black:
	$(info ${\n})
	$(info --- black ----------------------------------------------------------------------)
	@$(activate-venv); black $(shell git ls-files '*.py' ':!:docs/source/*')


.PHONY: cspell
cspell:
	@cspell lint --dot .


.PHONY: download-truthsets
download-truthsets:
	curl -X GET --output ./testdata/truthsets/customers.jsonl \
		https://raw.githubusercontent.com/Senzing/truth-sets/refs/heads/main/truthsets/demo/customers.jsonl
	curl -X GET --output ./testdata/truthsets/reference.jsonl \
		https://raw.githubusercontent.com/Senzing/truth-sets/refs/heads/main/truthsets/demo/reference.jsonl
	curl -X GET --output ./testdata/truthsets/watchlist.jsonl \
		https://raw.githubusercontent.com/Senzing/truth-sets/refs/heads/main/truthsets/demo/watchlist.jsonl


.PHONY: gofumpt
gofumpt:
	gofumpt -d ./**/*.go


.PHONY: golangci-lint
golangci-lint:
	@${GOBIN}/golangci-lint run --config=.github/linters/.golangci.yaml


.PHONY: govulncheck
govulncheck:
	@${GOBIN}/govulncheck ./...


.PHONY: load-database-with-truthsets
load-database-with-truthsets:
	$(activate-venv); \
		./bin/load_database_with_truthsets.py


.PHONY: pretty-print
pretty-print:
	@./bin/pretty_print.py
	diff -w senzingsdk-RFC8927-pretty.json senzingsdk-RFC8927.json


.PHONY: pylint
pylint:
	@$(activate-venv); \
		pylint $(shell git ls-files '*.py')


.PHONY: test-rfc8927-reconstitution
test-rfc8927-reconstitution:
	$(activate-venv); \
		./bin/test_rfc8927_reconstitution.py


.PHONY: test_using_senzing.py
test-using-senzing:
	$(activate-venv); \
		./bin/test_using_senzing.py


.PHONY: test-using-testdata-responses
test-using-testdata-responses:
	$(activate-venv); \
		./bin/test_using_testdata_responses.py

# -----------------------------------------------------------------------------
# Fixers
# -----------------------------------------------------------------------------

.PHONY: fix
fix: fix-asciicheck
fix: fix-bidichk
fix: fix-canonicalheader
# fix: fix-copyloopvar
fix: fix-cyclop
fix: fix-dupword
# fix: fix-durationcheck
# fix: fix-err113
fix: fix-errchkjson
fix: fix-errname
fix: fix-errorlint
# fix: fix-exhaustive
# fix: fix-exhaustruct
# fix: fix-exptostd
# fix: fix-fatcontext
# fix: fix-ginkgolinter
# fix: fix-gocheckcompilerdirectives
# fix: fix-gochecknoglobals
# fix: fix-godot
fix: fix-gofumpt
# fix: fix-grouper
# fix: fix-ifacecheck
# fix: fix-interfacebloat
fix: fix-inamedparam
# fix: fix-ireturn
fix: fix-loggercheck
# fix: fix-maintidx
# fix: fix-mirror
# fix: fix-mnd
fix: fix-nakedret
# fix: fix-nilerr
fix: fix-nilnesserr
fix: fix-nilnil
fix: fix-paralleltest
fix: fix-perfsprint
# fix: fix-predeclared
# fix: fix-protogetter
# fix: fix-rowserrcheck
fix: fix-tagalign
fix: fix-tagliatelle
# fix: fix-testableexamples
fix: fix-testifylint
# fix: fix-testpackage
# fix: fix-thelper
# fix: fix-usestdlibvars
fix: fix-usetesting
# fix: fix-whitespace
fix: fix-wrapcheck
fix: fix-wsl
	$(info fixes complete)


.PHONY: fix-asciicheck
fix-asciicheck:
	@asciicheck --fix ./...


.PHONY: fix-bidichk
fix-bidichk:
	@bidichk --fix ./...


.PHONY: fix-canonicalheader
fix-canonicalheader:
	@canonicalheader --fix ./...


.PHONY: fix-copyloopvar
fix-copyloopvar:
	@copyloopvar --fix ./...


.PHONY: fix-cyclop
fix-cyclop:
	@cyclop --fix ./...


.PHONY: fix-dupword
fix-dupword:
	@dupword --fix ./...


.PHONY: fix-durationcheck
fix-durationcheck:
	@durationcheck --fix ./...


.PHONY: fix-err113
fix-err113:
	@err113 --fix ./...


.PHONY: fix-errchkjson
fix-errchkjson:
	@errchkjson --fix ./...


.PHONY: fix-errname
fix-errname:
	@errname --fix ./...


.PHONY: fix-errorlint
fix-errorlint:
	@go-errorlint --fix ./...


.PHONY: fix-exhaustive
fix-exhaustive:
	@go-exhaustive --fix ./...


.PHONY: fix-exhaustruct
fix-exhaustruct:
	@go-exhaustruct --fix ./...


.PHONY: fix-exptostd
fix-exptostd:
	@go-exptostd --fix ./...


.PHONY: fix-fatcontext
fix-fatcontext:
	@go-fatcontext -fix ./...


.PHONY: fix-ginkgolinter
fix-ginkgolinter:
	@go-ginkgolinter --fix ./...


.PHONY: fix-gocheckcompilerdirectives
fix-gocheckcompilerdirectives:
	@go-gocheckcompilerdirectives --fix ./...


.PHONY: fix-gochecknoglobals
fix-gochecknoglobals:
	@go-gochecknoglobals --fix ./...


.PHONY: fix-godot
fix-godot:
	@go-godot --fix ./...


.PHONY: fix-gofumpt
fix-gofumpt:
	@gofumpt -w ./**/*.go


.PHONY: fix-grouper
fix-grouper:
	@grouper --fix ./...


.PHONY: fix-ifacecheck
fix-ifacecheck:
	@ifacecheck --fix ./...


.PHONY: fix-interfacebloat
fix-interfacebloat:
	@interfacebloat --fix ./...


.PHONY: fix-inamedparam
fix-inamedparam:
	@inamedparam --fix ./...


.PHONY: fix-ireturn
fix-ireturn:
	@ireturn --fix ./...


.PHONY: fix-loggercheck
fix-loggercheck:
	@loggercheck --fix ./...


.PHONY: fix-maintidx
fix-maintidx:
	@maintidx --fix ./...


.PHONY: fix-mirror
fix-mirror:
	@mirror --fix ./...


.PHONY: fix-mnd
fix-mnd:
	@mnd --fix ./...


.PHONY: fix-nakedret
fix-nakedret:
	@nakedret --fix ./...


.PHONY: fix-nilerr
fix-nilerr:
	@nilerr --fix ./...


.PHONY: fix-nilnesserr
fix-nilnesserr:
	@nilnesserr --fix ./...


.PHONY: fix-nilnil
fix-nilnil:
	@nilnil --fix ./...


.PHONY: fix-paralleltest
fix-paralleltest:
	@paralleltest --fix ./...


.PHONY: fix-perfsprint
fix-perfsprint:
	@perfsprint --fix ./...


.PHONY: fix-predeclared
fix-predeclared:
	@predeclared --fix ./...


.PHONY: fix-protogetter
fix-protogetter:
	@protogetter --fix ./...


.PHONY: fix-rowserrcheck
fix-rowserrcheck:
	@rowserrcheck --fix ./...


.PHONY: fix-tagalign
fix-tagalign:
	@tagalign --fix ./...


.PHONY: fix-tagliatelle
fix-tagliatelle:
	@tagliatelle --fix ./...


.PHONY: fix-testableexamples
fix-testableexamples:
	@testableexamples --fix ./...


.PHONY: fix-testifylint
fix-testifylint:
	@testifylint --fix ./...


.PHONY: fix-testpackage
fix-testpackage:
	@testpackage --fix ./...


.PHONY: fix-thelper
fix-thelper:
	@thelper --fix ./...


.PHONY: fix-usestdlibvars
fix-usestdlibvars:
	@usestdlibvars --fix ./...


.PHONY: fix-usetesting
fix-usetesting:
	@usetesting --fix ./...


.PHONY: fix-whitespace
fix-whitespace:
	@whitespace --fix ./...


.PHONY: fix-wrapcheck
fix-wrapcheck:
	@wrapcheck --fix ./...


.PHONY: fix-wsl
fix-wsl:
	@wsl --fix ./...
