package typedef

import (
	"bufio"
	"context"
	"encoding/json"
	"io/fs"
	"os"
	"path"
	"testing"

	"github.com/stretchr/testify/assert"
)

const (
	testDataPath = "../../testdata/responses_senzing"
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

func TestSz(test *testing.T) {
	ctx := context.TODO()
	root := os.DirFS(testDataPath)

	testCases := []struct {
		name      string
		theStruct any
	}{
		{
			name:      "SzConfigExportResponse*.jsonl",
			theStruct: SzConfigExportResponse{},
		},
		{
			name:      "SzConfigGetDataSourceRegistryResponse*.jsonl",
			theStruct: SzConfigGetDataSourceRegistryResponse{},
		},
		{
			name:      "SzConfigManagerGetConfigRegistryResponse*.jsonl",
			theStruct: SzConfigManagerGetConfigRegistryResponse{},
		},
		{
			name:      "SzConfigRegisterDataSourceResponse*.jsonl",
			theStruct: SzConfigRegisterDataSourceResponse{},
		},
		{
			name:      "SzConfigUnregisterDataSourceResponse*.jsonl",
			theStruct: SzConfigUnregisterDataSourceResponse{},
		},
		{
			name:      "SzDiagnosticCheckRepositoryPerformanceResponse*.jsonl",
			theStruct: SzDiagnosticCheckRepositoryPerformanceResponse{},
		},
		{
			name:      "SzDiagnosticGetFeatureResponse*.jsonl",
			theStruct: SzDiagnosticGetFeatureResponse{},
		},
		{
			name:      "SzEngineDeleteRecordResponse*.jsonl",
			theStruct: SzEngineDeleteRecordResponse{},
		},
		{
			name:      "SzEngineFindInterestingEntitiesByEntityIdResponse*.jsonl",
			theStruct: SzEngineFindInterestingEntitiesByEntityIDResponse{},
		},
		{
			name:      "SzEngineFindInterestingEntitiesByRecordIdResponse*.jsonl",
			theStruct: SzEngineFindInterestingEntitiesByRecordIDResponse{},
		},
		{
			name:      "SzEngineFindNetworkByEntityIdResponse*.jsonl",
			theStruct: SzEngineFindNetworkByEntityIDResponse{},
		},
		{
			name:      "SzEngineFindNetworkByRecordIdResponse*.jsonl",
			theStruct: SzEngineFindNetworkByRecordIDResponse{},
		},
		{
			name:      "SzEngineFindPathByEntityIdResponse*.jsonl",
			theStruct: SzEngineFindPathByEntityIDResponse{},
		},
		{
			name:      "SzEngineFindPathByRecordIdResponse*.jsonl",
			theStruct: SzEngineFindPathByRecordIDResponse{},
		},
		{
			name:      "SzEngineGetEntityByEntityIdResponse*.jsonl",
			theStruct: SzEngineGetEntityByEntityIDResponse{},
		},
		{
			name:      "SzEngineGetEntityByRecordIdResponse*.jsonl",
			theStruct: SzEngineGetEntityByRecordIDResponse{},
		},
		{
			name:      "SzEngineGetRecordResponse*.jsonl",
			theStruct: SzEngineGetRecordResponse{},
		},
		{
			name:      "SzEngineGetRecordPreviewResponse*.jsonl",
			theStruct: SzEngineGetRecordPreviewResponse{},
		},
		{
			name:      "SzEngineGetVirtualEntityByRecordIdResponse*.jsonl",
			theStruct: SzEngineGetVirtualEntityByRecordIDResponse{},
		},
		{
			name:      "SzEngineHowEntityByEntityIdResponse*.jsonl",
			theStruct: SzEngineHowEntityByEntityIDResponse{},
		},
		{
			name:      "SzEngineGetRedoRecordResponse*.jsonl",
			theStruct: SzEngineGetRedoRecordResponse{},
		},
		{
			name:      "SzEngineProcessRedoRecordResponse*.jsonl",
			theStruct: SzEngineProcessRedoRecordResponse{},
		},
		{
			name:      "SzEngineReevaluateEntityResponse*.jsonl",
			theStruct: SzEngineReevaluateEntityResponse{},
		},
		{
			name:      "SzEngineReevaluateRecordResponse*.jsonl",
			theStruct: SzEngineReevaluateRecordResponse{},
		},
		{
			name:      "SzEngineSearchByAttributesResponse*.jsonl",
			theStruct: SzEngineSearchByAttributesResponse{},
		},
		{
			name:      "SzDiagnosticGetRepositoryInfoResponse*.jsonl",
			theStruct: SzDiagnosticGetRepositoryInfoResponse{},
		},
		{
			name:      "SzEngineGetStatsResponse*.jsonl",
			theStruct: SzEngineGetStatsResponse{},
		},
		{
			name:      "SzProductGetLicenseResponse*.jsonl",
			theStruct: SzProductGetLicenseResponse{},
		},
		{
			name:      "SzProductGetVersionResponse*.jsonl",
			theStruct: SzProductGetVersionResponse{},
		},
	}

	for _, testCase := range testCases {
		test.Run(testCase.name, func(test *testing.T) {

			jsonStruct := testCase.theStruct

			entries, err := fs.Glob(root, testCase.name)
			testError(test, ctx, err)

			for _, entry := range entries {
				testFile := path.Join(testDataPath, entry)
				file, err := os.Open(testFile)
				testError(test, ctx, err)
				defer file.Close()
				scanner := bufio.NewScanner(file)
				for scanner.Scan() {
					line := scanner.Text()
					if len(line) > 0 {
						err = json.Unmarshal([]byte(line), &jsonStruct)
						testError(test, ctx, err)
						_, err = json.Marshal(jsonStruct)
						testError(test, ctx, err)
					}
				}
			}
		})
	}

}
