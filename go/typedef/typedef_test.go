package typedef

import (
	"context"
	"encoding/json"
	"io/fs"
	"os"
	"path"
	"testing"

	"github.com/stretchr/testify/assert"
)

const (
	testDataPath = "../../testdata/senzing_responses"
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
		{
			name:      "SzEngineDeleteRecordResponse*.json",
			theStruct: SzEngineDeleteRecordResponse{},
		},
		{
			name:      "SzEngineFindInterestingEntitiesByEntityIdResponse*.json",
			theStruct: SzEngineFindInterestingEntitiesByEntityIDResponse{},
		},
		{
			name:      "SzEngineFindInterestingEntitiesByRecordIdResponse*.json",
			theStruct: SzEngineFindInterestingEntitiesByRecordIDResponse{},
		},
		{
			name:      "SzEngineFindNetworkByEntityIdResponse*.json",
			theStruct: SzEngineFindNetworkByEntityIDResponse{},
		},
		{
			name:      "SzEngineFindNetworkByRecordIdResponse*.json",
			theStruct: SzEngineFindNetworkByRecordIDResponse{},
		},
		{
			name:      "SzEngineFindPathByEntityIdResponse*.json",
			theStruct: SzEngineFindPathByEntityIDResponse{},
		},
		{
			name:      "SzEngineFindPathByRecordIdResponse*.json",
			theStruct: SzEngineFindPathByRecordIDResponse{},
		},
		{
			name:      "SzEngineGetEntityByEntityIdResponse*.json",
			theStruct: SzEngineGetEntityByEntityIDResponse{},
		},
		{
			name:      "SzEngineGetEntityByRecordIdResponse*.json",
			theStruct: SzEngineGetEntityByRecordIDResponse{},
		},
		{
			name:      "SzEngineGetRecordResponse*.json",
			theStruct: SzEngineGetRecordResponse{},
		},
		{
			name:      "SzEngineGetRecordPreviewResponse*.json",
			theStruct: SzEngineGetRecordPreviewResponse{},
		},
		{
			name:      "SzEngineGetVirtualEntityByRecordIdResponse*.json",
			theStruct: SzEngineGetVirtualEntityByRecordIDResponse{},
		},
		{
			name:      "SzEngineHowEntityByEntityIdResponse*.json",
			theStruct: SzEngineHowEntityByEntityIDResponse{},
		},
		{
			name:      "SzEngineGetRedoRecordResponse*.json",
			theStruct: SzEngineGetRedoRecordResponse{},
		},
		{
			name:      "SzEngineProcessRedoRecordResponse*.json",
			theStruct: SzEngineProcessRedoRecordResponse{},
		},
		{
			name:      "SzEngineReevaluateEntityResponse*.json",
			theStruct: SzEngineReevaluateEntityResponse{},
		},
		{
			name:      "SzEngineReevaluateRecordResponse*.json",
			theStruct: SzEngineReevaluateRecordResponse{},
		},
		{
			name:      "SzEngineSearchByAttributesResponse*.json",
			theStruct: SzEngineSearchByAttributesResponse{},
		},
		{
			name:      "SzDiagnosticGetRepositoryInfoResponse*.json",
			theStruct: SzDiagnosticGetRepositoryInfoResponse{},
		},
		{
			name:      "SzEngineGetStatsResponse*.json",
			theStruct: SzEngineGetStatsResponse{},
		},
		{
			name:      "SzProductGetLicenseResponse*.json",
			theStruct: SzProductGetLicenseResponse{},
		},
		{
			name:      "SzProductGetVersionResponse*.json",
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
