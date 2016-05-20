function myFunction() {
}

function ApendResponses() {
  var form = FormApp.openByUrl('https://docs.google.com/forms/d/1L7CbIrk5hYpVzQ4jWQHezFd6f-aVCtBpo5ybGAe7R2Q/edit?usp=forms_home&ths=true');
  var sheet = SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/1VtpPRT5kp7iS9fTuyHQ0FkEnW1MruhLMsuMxvhxRyuo/edit#gid=1312081245");
  var rows = sheet.getDataRange();
  var numRows = rows.getNumRows();
  var values = rows.getValues();
  for (var x = 1; x < numRows; x++) {
    var formResponse = form.createResponse();
    var items = form.getItems();
    var row = values[x];
    // Cluster Name
    var formItem = items[0.0].asTextItem();
    var response = formItem.createResponse(row[1]);
    formResponse.withItemResponse(response);
    // CPUs number
    var formItem = items[1.0].asTextItem();
    var response = formItem.createResponse(row[2]);
    formResponse.withItemResponse(response);
    // CPU type (list)
    var formItem = items[2.0].asListItem();
    var response = formItem.createResponse(row[3]);     
    formResponse.withItemResponse(response);
    // CPU clock 
    var formItem = items[3.0].asTextItem();   
    var response = formItem.createResponse(row[4]);     
    formResponse.withItemResponse(response);
    // Rocks version (list)
    var formItem = items[4.0].asListItem();
    var response = formItem.createResponse(row[5]);     
    formResponse.withItemResponse(response);
    // Organization
    var formItem = items[5.0].asTextItem();
    var response = formItem.createResponse(row[6]);     
    formResponse.withItemResponse(response);
    // Location (long text)
    var formItem = items[6.0].asTextItem();   
    var response = formItem.createResponse(row[7]);
    formResponse.withItemResponse(response);
    // Part of Rocks network (must choice)
    var formItem = items[7.0].asMultipleChoiceItem();
    var response = formItem.createResponse(row[8]);
    formResponse.withItemResponse(response);
    // Notes (long text)
    var formItem = items[8.0].asParagraphTextItem();
    var response = formItem.createResponse(row[9]);
    formResponse.withItemResponse(response);
    // FLOPs
    var formItem = items[9.0].asTextItem();
    var response = formItem.createResponse(row[10]);
    formResponse.withItemResponse(response);
    // Registration time, first column of existing spreadsheet
    var formItem = items[10.0].asDateItem();
    var response = formItem.createResponse(row[0]);
    formResponse.withItemResponse(response);


    formResponse.submit();
    Utilities.sleep(500);
  }
};
