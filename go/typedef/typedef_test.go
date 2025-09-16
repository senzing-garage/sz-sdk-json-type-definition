package typedef

import (
	"context"
	"encoding/json"
	"fmt"
	"io/fs"
	"os"
	"path"
	"testing"

	"github.com/stretchr/testify/assert"
)

const (
	testDataPath = "../../testdata/example_responses"
)

func testError(test *testing.T, ctx context.Context, err error) {
	_ = ctx
	if err != nil {
		test.Log("Error:", err.Error())
		assert.FailNow(test, err.Error())
	}
}

// ----------------------------------------------------------------------------
// --- Test cases
// ----------------------------------------------------------------------------

func TestSzConfigExportResponse(test *testing.T) {
	ctx := context.TODO()
	root := os.DirFS(testDataPath)
	filter := "SzConfigExport*.json"
	jsonStruct := SzConfigExportResponse{}

	entries, err := fs.Glob(root, filter)
	testError(test, ctx, err)

	for _, entry := range entries {
		testFile := path.Join(testDataPath, entry)
		fileBytes, err := os.ReadFile(testFile)
		testError(test, ctx, err)

		err = json.Unmarshal(fileBytes, &jsonStruct)
		testError(test, ctx, err)
		_, err = json.Marshal(jsonStruct)
		testError(test, ctx, err)
	}
}

func TestSz(test *testing.T) {
	ctx := context.TODO()
	root := os.DirFS(testDataPath)

	testCases := []struct {
		name      string
		theStruct any
	}{
		{
			name:      "SzConfigExportResponse*.json",
			theStruct: SzConfigExportResponse{},
		},
		{
			name:      "SzConfigGetDataSourceRegistryResponse*.json",
			theStruct: SzConfigGetDataSourceRegistryResponse{},
		},
		{
			name:      "SzConfigManagerGetConfigRegistryResponse*.json",
			theStruct: SzConfigManagerGetConfigRegistryResponse{},
		},
		{
			name:      "SzConfigRegisterDataSourceResponse*.json",
			theStruct: SzConfigRegisterDataSourceResponse{},
		},
		{
			name:      "SzConfigUnregisterDataSourceResponse*.json",
			theStruct: SzConfigUnregisterDataSourceResponse{},
		},
		{
			name:      "SzDiagnosticCheckRepositoryPerformanceResponse*.json",
			theStruct: SzDiagnosticCheckRepositoryPerformanceResponse{},
		},
		{
			name:      "SzDiagnosticGetFeatureResponse*.json",
			theStruct: SzDiagnosticGetFeatureResponse{},
		},
	}

	for _, testCase := range testCases {
		test.Run(testCase.name, func(test *testing.T) {

			jsonStruct := testCase.theStruct

			entries, err := fs.Glob(root, testCase.name)
			testError(test, ctx, err)

			count := 0
			for _, entry := range entries {
				count += 1
				fmt.Println(count)
				testFile := path.Join(testDataPath, entry)
				fileBytes, err := os.ReadFile(testFile)
				testError(test, ctx, err)
				if len(fileBytes) > 0 {
					err = json.Unmarshal(fileBytes, &jsonStruct)
					testError(test, ctx, err)
					_, err = json.Marshal(jsonStruct)
					testError(test, ctx, err)
				}
			}

		})
	}

}
