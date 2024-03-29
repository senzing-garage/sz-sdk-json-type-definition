# sz-sdk-json-type-definition development

## Prerequisites

1. [git](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/git.md)
1. [go](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/go.md)
1. [jtg-codegen](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/jtd-codegen.md)
1. [make](https://github.com/senzing-garage/knowledge-base/blob/main/WHATIS/make.md)

## Install Git repository

1. Identify git repository.

    ```console
    export GIT_ACCOUNT=senzing
    export GIT_REPOSITORY=sz-sdk-json-type-definition
    export GIT_ACCOUNT_DIR=~/${GIT_ACCOUNT}.git
    export GIT_REPOSITORY_DIR="${GIT_ACCOUNT_DIR}/${GIT_REPOSITORY}"

    ```

1. Using the environment variables values just set, follow steps in
   [clone-repository](https://github.com/senzing-garage/knowledge-base/blob/main/HOWTO/clone-repository.md) to install the Git repository.

## Update senzingapi-RFC8927.json

1. Make changes to [senzingapi-RFC8927.json](../senzingapi-RFC8927.json)
1. Analyse [senzingapi-RFC8927.json](../senzingapi-RFC8927.json) after the changes.
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

1. Update dependencies.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make dependencies

    ```

1. Run test cases.
   Example:

    ```console
    cd ${GIT_REPOSITORY_DIR}
    make test

    ```

### References

1. <https://jsontypedef.com/>
1. <https://github.com/jsontypedef/>
