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

## Update senzingapi-RFC8927.json

1. Make changes to [senzingapi-RFC8927.json]
1. Analyse [senzingapi-RFC8927.json] after the changes.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make analyze

    ```

    1. Review analysis:
        1. **TEST 1:** Make sure JSON keys are in sorted order.
        1. **TEST 2:** Make sure "Features", "FeatureScores", "JsonData", "MatchInfoCandidateKeys", and "MatchScores" fields have the "mandatory" JSON keys.
        1. **TEST 3:** Determine if "Features", "FeatureScores", "JsonData", "MatchInfoCandidateKeys", or "MatchScores" field have extra JSON keys.
        There will be some extra keys, mostly in "JsonData".
        1. **TEST 4:** See if list have exactly the same JSON keys.
        This will detect duplication.
        There will be some that look like duplicates, but actually aren't.
        1. **TEST 5:** Determine of a JSON key has been unnecessarily duplicated.
        There will be many duplicates.
        JSON keys with a count of "1" are not displayed.
        1. **TEST 6:** Review JSON keys that have more than one datatype.

1. See if additional changes are needed.

    1. Pretty print JSON.
       Example:

        ```console
        cd ${GIT_REPOSITORY_DIR}
        make pretty-print

        ```

    1. Compare  `senzingapi-RFC8927-pretty.json` and `senzingapi-RFC8927.json`.
    Determine if any modifications need to be added to `senzingapi-RFC8927.json`.
    Example:

        ```console
        cd ${GIT_REPOSITORY_DIR}
        diff senzingapi-RFC8927-pretty.json senzingapi-RFC8927.json

        ```

1. Generate code.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean generate-code

    ```

1. Generate testcases.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make generate-tests

    ```

## Lint

1. Run linting.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make lint

    ```

## Test

1. Run tests.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean setup test

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

## Documentation

1. View documentation.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean documentation

    ```

1. If a web page doesn't appear, visit [localhost:6060].
1. Senzing documentation will be in the "Third party" section.
   `github.com` > `senzing-garage` > `template-go`

1. When a versioned release is published with a `v0.0.0` format tag,
the reference can be found by clicking on the following badge at the top of the README.md page.
Example:

    [![Go Reference Badge]][Go Reference]

1. To stop the `godoc` server, run

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make clean

    ```

## References

1. [JSON TypeDef]
1. [JSON TypeDef on Github]

[clone-repository]: https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/clone-repository.md
[docker]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/docker.md
[git]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/git.md
[Go Reference Badge]: https://pkg.go.dev/badge/github.com/senzing-garage/template-go.svg
[Go Reference]: https://pkg.go.dev/github.com/senzing-garage/template-go
[go]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/go.md
[JSON TypeDef on Github]: https://github.com/jsontypedef
[JSON TypeDef]: https://jsontypedef.com/
[jtg-codegen]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/jtd-codegen.md
[localhost:6060]: http://localhost:6060/pkg/github.com/senzing-garage/template-go/
[make]: https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/make.md
[senzingapi-RFC8927.json]: ../senzingapi-RFC8927.json
[testcoverage.yaml]: ../.github/coverage/testcoverage.yaml
