# sz-sdk-json-type-definition development

The following instructions are useful during development.

**Note:** This has been tested on Linux and Darwin/macOS.
It has not been tested on Windows.

## Prerequisites for development

:thinking: The following tasks need to be complete before proceeding.
These are "one-time tasks" which may already have been completed.

1. The following software programs need to be installed:
    1. [git]
    1. [make]
    1. [docker]
    1. [go]
    1. [jtg-codegen]

## Install Git repository

1. Identify git repository.

    ```console
    export GIT_ACCOUNT=senzing-garage
    export GIT_REPOSITORY=sz-sdk-json-type-definition
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"

    ```

1. Using the environment variables values just set, follow
   steps in [clone-repository] to install the Git repository.

## Dependencies

1. A one-time command to install dependencies needed for `make` targets.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make dependencies-for-development

    ```

1. Install dependencies needed for [Go] code.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make dependencies

    ```

## Update senzingsdk-RFC8927.json

1. Make changes to [senzingsdk-RFC8927.json]

### Version

1. Create artifacts for a version.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make version

    ```

## Lint

1. Run linting.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make lint

    ```

1. Review analysis:
    1. **TEST 1:** Make sure JSON keys are in sorted order.
    1. **TEST 2:**
    1. **TEST 3:** Report how many times a JSON key has been specified.
    1. **TEST 4:** Report JSON keys that have more than one datatype.
    1. **TEST 5:** Report any `ref` keys that have a bad value.
    1. **TEST 6:** Report JSON keys that are not used.

1. Address any issues in the `diff` between `senzingsdk-RFC8927.json` and the temporary `senzingsdk-RFC8927-pretty.json`.

## Test

1. Run tests.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make test

    ```

## Coverage

Create a code coverage map.

1. Run Go tests.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean setup coverage

    ```

   A web-browser will show the results of the coverage.
   The goal is to have over 80% coverage.
   Anything less needs to be reflected in [testcoverage.yaml].

## References

1. [JSON TypeDef]
1. [JSON TypeDef on Github]

[clone-repository]: https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/clone-repository.md
[docker]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/docker.md
[git]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/git.md
[go]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/go.md
[JSON TypeDef on Github]: https://github.com/jsontypedef
[JSON TypeDef]: https://jsontypedef.com/
[jtg-codegen]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/jtd-codegen.md
[make]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/make.md
[senzingsdk-RFC8927.json]: ../senzingsdk-RFC8927.json
[testcoverage.yaml]: ../.github/coverage/testcoverage.yaml
