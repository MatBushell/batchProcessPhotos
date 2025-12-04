#target photoshop

// Read the queue.json file created in python(watcher.py)

// assign the queue to a variable
var queueFile = new File("queue.json"); 

// open the file
queueFile.open("r");

// read the content of the json file and assign it to a variable
var jsonContent = queueFile.read();

// close the file
queueFile.close();

// Parse the JSON
var data = eval("(" + jsonContent + ")");
// Note: ExtendScript doesn't have JSON.parse, so we use evel()

// get he array of files
var fileList = data.files;

// Loop through each file path
for (var i = 0; i < fileList.length; i++) {
    var filePath = fileList[i];
    // create a file object
    var fileToOpen = new File(filePath);
    
    // check if file exists
    if (fileToOpen.exists) {
        var doc = app.open(fileToOpen);

        // file manipulation here, filters, export to jpg etc...

        // close the file without saving
        doc.close(SaveOptions.DONOTSAVECHANGES);
        
    } else {
        alert("File not found: " + filePath);
    }
}


