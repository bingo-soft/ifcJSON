const fs = require('fs');
const xml2js = require('xml2js');

// Specify the path to your XML file and the output JSON file
const xmlFilePath = './psd/Pset_DoorCommon.xml';
const jsonFilePath = './psd_json/Pset_DoorCommon.json';

// Read the XML data from the file
fs.readFile(xmlFilePath, 'utf-8', (err, xmlData) => {
    if (err) {
        console.error(err);
    } else {
        // Create a parser instance
        const parser = new xml2js.Parser();

        // Parse the XML data
        parser.parseString(xmlData, (parseErr, result) => {
        if (parseErr) {
            console.error(parseErr);
        } else {
            // Convert the result to JSON
            const jsonData = JSON.stringify(result, null, 2);

            // Write the JSON data to a new file
            fs.writeFile(jsonFilePath, jsonData, 'utf-8', (writeErr) => {
                if (writeErr) {
                    console.error(writeErr);
                } else {
                    console.log(`JSON data saved to ${jsonFilePath}`);
                }
            });
        }
        });
    }
});

